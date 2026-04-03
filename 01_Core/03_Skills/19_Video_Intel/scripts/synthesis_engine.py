"""
Synthesis Engine - Methodology Extraction and Implementation Plan Generation

Combines video transcripts, repo code maps, and OS capabilities to generate
actionable implementation plans.
"""

import json
import os
import re
import shutil
import subprocess
import tempfile
from typing import Dict, List, Optional

from .video_analyzer import VideoAnalyzer
from .repo_scanner import RepoScanner


class SynthesisEngine:
    """Synthesizes video + repo data into implementation plans."""

    # NLP patterns for methodology extraction
    METHODOLOGY_PATTERNS = [
        r"(?:step|phase|stages?)\s+\d+[:\.]?\s*(.*?)(?=\n|$)",
        r"(?:first|then|next|finally)\s+(.*?)(?=\n|$)",
        r"(?:how to|method|technique|approach)\s*(?:to|for)?\s*(.*?)(?=\n|$)",
        r"(?:use|using|utilize)\s+(?:the|an?)?\s*(\w+)\s+(?:to|for)\s*(.*?)(?=\n|$)",
    ]

    # URL patterns for demo environments
    DEMO_URL_PATTERNS = [
        r"https?://(?:www\.)?(?:codepen|codesandbox|stackblitz|replit|jsfiddle|playground)\.com/[^\s]*",
        r"https?://(?:github\.com|www\.youtube)\.+/[^\s]*",
        r"https?://[a-zA-Z0-9-]+\.[a-zA-Z]{2,}/[^\s]*",
    ]

    def __init__(self, workspace_dir: Optional[str] = None):
        """
        Initialize the synthesis engine.

        Args:
            workspace_dir: Working directory for temp files.
        """
        self.workspace_dir = workspace_dir or tempfile.mkdtemp(prefix="synthesis_")
        self.video_analyzer = VideoAnalyzer(self.workspace_dir)
        self.repo_scanner = RepoScanner(self.workspace_dir)

    def extract_methodologies(self, transcript: str) -> List[dict]:
        """
        Extract methodologies from transcript using NLP patterns.

        Args:
            transcript: Video transcript text

        Returns:
            List of methodology dictionaries
        """
        if not transcript:
            return []

        methodologies = []
        lines = transcript.split("\n")

        # Simple pattern matching for methodology indicators
        current_methodology = None

        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            # Check for methodology indicators
            lower_line = line.lower()

            # Pattern: numbered steps
            step_match = re.match(r"^(\d+)[\.\)]\s*(.+)", line)
            if step_match:
                step = int(step_match.group(1))
                content = step_match.group(2)

                if not current_methodology:
                    current_methodology = {
                        "name": f"Methodology {len(methodologies) + 1}",
                        "type": "technique",
                        "steps": [],
                        "code_examples": [],
                        "tools": [],
                    }

                current_methodology["steps"].append(
                    {"step": step, "description": content}
                )
                continue

            # Pattern: sequential indicators
            seq_patterns = ["first:", "then:", "next:", "finally:"]
            for pattern in seq_patterns:
                if lower_line.startswith(pattern):
                    if not current_methodology:
                        current_methodology = {
                            "name": f"Methodology {len(methodologies) + 1}",
                            "type": "technique",
                            "steps": [],
                            "code_examples": [],
                            "tools": [],
                        }
                    current_methodology["steps"].append(
                        {
                            "step": len(current_methodology["steps"]) + 1,
                            "description": line,
                        }
                    )
                    break
            else:
                # End of current methodology
                if current_methodology and len(current_methodology["steps"]) > 0:
                    # Check if this line might be a new methodology name
                    if ":" not in line and len(line) < 80:
                        current_methodology["name"] = line
                    else:
                        methodologies.append(current_methodology)
                        current_methodology = None

        # Don't forget the last one
        if current_methodology and current_methodology["steps"]:
            methodologies.append(current_methodology)

        # Extract code examples and tools
        for method in methodologies:
            method["code_examples"] = self._extract_code_examples(transcript)
            method["tools"] = self._extract_tool_references(transcript)

        return methodologies

    def _extract_code_examples(self, text: str) -> List[str]:
        """Extract code-like patterns from text."""
        code_patterns = [
            r"`([^`]+)`",  # Inline code
            r"```[\s\S]*?```",  # Code blocks
        ]

        examples = []
        for pattern in code_patterns:
            matches = re.findall(pattern, text)
            examples.extend(matches)

        return examples[:5]  # Limit to 5 examples

    def _extract_tool_references(self, text: str) -> List[str]:
        """Extract tool/technology references from text."""
        common_tools = [
            "python",
            "javascript",
            "typescript",
            "node",
            "nodejs",
            "react",
            "vue",
            "angular",
            "nextjs",
            "nuxt",
            "docker",
            "kubernetes",
            "k8s",
            "git",
            "github",
            "gitlab",
            "postgresql",
            "mysql",
            "mongodb",
            "redis",
            "aws",
            "gcp",
            "azure",
            "vercel",
            "netlify",
            "openai",
            "claude",
            "anthropic",
            "gpt",
            "whisper",
            "yt-dlp",
            "ffmpeg",
        ]

        text_lower = text.lower()
        found_tools = []

        for tool in common_tools:
            if re.search(rf"\b{tool}\b", text_lower):
                found_tools.append(tool)

        return list(set(found_tools))

    def extract_demo_urls(self, transcript: str) -> List[dict]:
        """
        Extract demo environment URLs from transcript.

        Args:
            transcript: Video transcript text

        Returns:
            List of demo URL dictionaries
        """
        if not transcript:
            return []

        demo_urls = []

        for pattern in self.DEMO_URL_PATTERNS:
            matches = re.findall(pattern, transcript)
            for url in matches:
                # Classify demo type
                demo_type = self._classify_demo_url(url)
                demo_urls.append(
                    {
                        "url": url,
                        "type": demo_type,
                        "context": self._get_url_context(transcript, url),
                    }
                )

        # Deduplicate by URL
        seen = set()
        unique_demos = []
        for demo in demo_urls:
            if demo["url"] not in seen:
                seen.add(demo["url"])
                unique_demos.append(demo)

        return unique_demos

    def _classify_demo_url(self, url: str) -> str:
        """Classify demo URL type."""
        url_lower = url.lower()

        if "codepen" in url_lower:
            return "sandbox"
        elif "codesandbox" in url_lower:
            return "sandbox"
        elif "stackblitz" in url_lower:
            return "sandbox"
        elif "replit" in url_lower:
            return "playground"
        elif "jsfiddle" in url_lower:
            return "playground"
        elif "youtube" in url_lower or "youtu.be" in url_lower:
            return "video"
        elif "github" in url_lower:
            return "repository"
        else:
            return "documentation"

    def _get_url_context(self, text: str, url: str) -> str:
        """Get text context around a URL."""
        # Find the URL in text and get surrounding text
        idx = text.find(url)
        if idx == -1:
            return ""

        start = max(0, idx - 100)
        end = min(len(text), idx + len(url) + 100)

        return text[start:end].replace("\n", " ").strip()

    def verify_os_capabilities(self, required_tools: List[str]) -> dict:
        """
        Verify required tools against OS capabilities.

        Args:
            required_tools: List of tool names to check

        Returns:
            Dictionary with available, missing, and version info
        """
        result = {"available": [], "missing": [], "versions": {}}

        for tool in required_tools:
            # Check if tool is available
            cmd = ["where" if os.name == "nt" else "which", tool]

            try:
                check_result = subprocess.run(
                    cmd, capture_output=True, text=True, timeout=5
                )

                if check_result.returncode == 0:
                    result["available"].append(tool)

                    # Get version if possible
                    version_cmd = [tool, "--version"]
                    try:
                        version_result = subprocess.run(
                            version_cmd, capture_output=True, text=True, timeout=5
                        )
                        if version_result.returncode == 0:
                            # Extract version number
                            version_match = re.search(
                                r"(\d+\.\d+(?:\.\d+)?)", version_result.stdout
                            )
                            if version_match:
                                result["versions"][tool] = version_match.group(1)
                            else:
                                result["versions"][tool] = version_result.stdout.split(
                                    "\n"
                                )[0][:50]
                    except:
                        pass
                else:
                    result["missing"].append(tool)

            except FileNotFoundError:
                result["missing"].append(tool)
            except subprocess.TimeoutExpired:
                result["missing"].append(tool)

        return result

    def generate_implementation_plan(
        self, video_data: dict, repo_data: Optional[dict] = None
    ) -> dict:
        """
        Generate complete implementation plan from video and repo data.

        Args:
            video_data: Output from video_analyzer.analyze()
            repo_data: Output from repo_scanner.scan_repo() (optional)

        Returns:
            Structured implementation plan
        """
        plan = {
            "prerequisites": [],
            "steps": [],
            "verification": [],
            "complexity": "medium",
            "components": {
                "video": video_data.get("metadata", {}),
                "transcript": video_data.get("transcript", "")[:500]
                if video_data.get("transcript")
                else "",
                "methodologies": [],
                "demo_urls": [],
                "repo": None,
                "os_verification": {},
            },
        }

        # Extract methodologies from transcript
        if video_data.get("transcript"):
            methodologies = self.extract_methodologies(video_data["transcript"])
            plan["components"]["methodologies"] = methodologies

            # Build steps from methodologies
            for method in methodologies:
                for step in method.get("steps", []):
                    plan["steps"].append(
                        {
                            "description": step["description"],
                            "category": method["type"],
                            "methodology": method["name"],
                        }
                    )

        # Extract demo URLs
        if video_data.get("transcript"):
            demo_urls = self.extract_demo_urls(video_data["transcript"])
            plan["components"]["demo_urls"] = demo_urls

            # Add demo verification to plan
            if demo_urls:
                for demo in demo_urls:
                    plan["verification"].append(
                        {
                            "type": "demo",
                            "url": demo["url"],
                            "description": f"Verify {demo['type']}: {demo['url']}",
                        }
                    )
            else:
                plan["verification"].append(
                    {"type": "note", "description": "No demo environments detected"}
                )

        # Add repo data if available
        if repo_data:
            plan["components"]["repo"] = {
                "path": repo_data.get("repo_path"),
                "files": repo_data.get("summary", {}).get("python_files", 0),
                "imports": repo_data.get("summary", {}).get("total_imports", [])[:20],
            }

            # Add repo-specific steps
            plan["steps"].append(
                {
                    "description": "Review cloned repository structure",
                    "category": "setup",
                    "methodology": "Repository Analysis",
                }
            )

        # Verify OS capabilities
        all_tools = []
        for method in plan["components"]["methodologies"]:
            all_tools.extend(method.get("tools", []))

        if all_tools:
            os_verification = self.verify_os_capabilities(list(set(all_tools)))
            plan["components"]["os_verification"] = os_verification

            # Add missing tools as prerequisites
            for tool in os_verification.get("missing", []):
                plan["prerequisites"].append(
                    {
                        "tool": tool,
                        "action": "install",
                        "description": f"Install {tool} to proceed",
                    }
                )

        # Determine complexity
        total_steps = len(plan["steps"])
        if total_steps <= 3:
            plan["complexity"] = "low"
        elif total_steps <= 8:
            plan["complexity"] = "medium"
        else:
            plan["complexity"] = "high"

        # Add final verification step
        plan["verification"].append(
            {
                "type": "completion",
                "description": "Verify all steps completed successfully",
            }
        )

        return plan

    def synthesize(self, video_url: str, repo_url: Optional[str] = None) -> dict:
        """
        Full synthesis pipeline: video + repo → implementation plan.

        Args:
            video_url: YouTube video URL
            repo_url: Optional GitHub repository URL

        Returns:
            Complete implementation plan
        """
        # Step 1: Analyze video
        video_data = self.video_analyzer.analyze(video_url, include_transcript=True)

        # Step 2: Optionally scan repo
        repo_data = None
        if repo_url:
            try:
                repo_data = self.repo_scanner.scan_repo(repo_url)
            except ValueError as e:
                video_data["repo_error"] = str(e)

        # Step 3: Generate implementation plan
        plan = self.generate_implementation_plan(video_data, repo_data)

        # Cleanup
        self.cleanup()

        return plan

    def cleanup(self):
        """Clean up temporary files."""
        if os.path.exists(self.workspace_dir):
            shutil.rmtree(self.workspace_dir, ignore_errors=True)
