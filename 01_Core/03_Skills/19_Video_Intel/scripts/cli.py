"""
Video Intel CLI - Command-line interface for video analysis.

Usage:
    video-intel analyze <video_url> [--repo <repo_url>] [--output <file>] [--format json|markdown] [--verbose]
    video-intel --help
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

import click

from synthesis_engine import SynthesisEngine
from video_registry import VideoRegistry

# Root of the PersonalOS repo (4 levels up from scripts/)
_REPO_ROOT = Path(__file__).resolve().parents[4]


def _default_output(video_title: str) -> str:
    """Generate Video_Analysis_{date}_{slug}.md filename in repo root."""
    date = datetime.now().strftime("%Y-%m-%d")
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", video_title or "Video")[:40].strip("_")
    return str(_REPO_ROOT / f"Video_Analysis_{date}_{slug}.md")


@click.group()
@click.version_option(version="0.1.0")
def cli():
    """Video Intel - Extract structured knowledge from YouTube videos and GitHub repos."""
    pass


@cli.command()
@click.argument("video_url")
@click.option("--repo", "-r", help="GitHub repository URL for code analysis")
@click.option(
    "--output", "-o", default=None, help="Output file path (default: Video_Analysis_{date}_{title}.md in repo root)"
)
@click.option(
    "--format",
    "-f",
    type=click.Choice(["json", "markdown"]),
    default="markdown",
    help="Output format",
)
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
@click.option(
    "--no-transcript", is_flag=True, help="Skip transcript extraction (faster)"
)
def analyze(video_url, repo, output, format, verbose, no_transcript):
    """
    Analyze a YouTube video and optional GitHub repository to generate an implementation plan.

    VIDEO_URL: YouTube video URL to analyze

    Examples:

        video-intel analyze https://www.youtube.com/watch?v=xxx

        video-intel analyze https://www.youtube.com/live/xxx --repo https://github.com/user/repo

        video-intel analyze https://www.youtube.com/watch?v=xxx -o plan.json -f json
    """
    if verbose:
        click.echo(f"[*] Starting analysis for: {video_url}")
        if repo:
            click.echo(f"[*] Repository: {repo}")

    try:
        # Initialize synthesis engine
        engine = SynthesisEngine()

        # Run synthesis
        if verbose:
            click.echo("[*] Extracting video metadata and transcript...")

        result = engine.synthesize(video_url, repo)

        # Resolve output path — default to repo root with auto name
        video_title = result.get("components", {}).get("video", {}).get("title", "")
        resolved_output = output or _default_output(video_title)

        # Output results
        if format == "json":
            output_data = json.dumps(result, indent=2)
            Path(resolved_output).write_text(output_data, encoding="utf-8")
            click.echo(f"[+] Results saved to: {resolved_output}")

        else:
            # Generate markdown output
            markdown = generate_markdown(result)
            Path(resolved_output).write_text(markdown, encoding="utf-8")
            click.echo(f"[+] Implementation plan saved to: {resolved_output}")

            # Log to registry
            if result.get("components", {}).get("video"):
                try:
                    registry_path = Path(__file__).parent.parent.parent.parent.parent / "02_Knowledge" / "06_Unicorn" / "video_analysis_registry.md"
                    video_registry = VideoRegistry(str(registry_path))
                    abs_output = str(Path(resolved_output).resolve())
                    video_registry.append_to_registry(result["components"]["video"], abs_output)
                    if verbose:
                        click.echo(f"[+] Added entry to Video Registry")
                except Exception as reg_err:
                    click.echo(f"[!] Warning: Failed to update registry: {reg_err}", err=True)

        # Summary
        if verbose:
            metadata = result.get("components", {}).get("video", {})
            methodologies = result.get("components", {}).get("methodologies", [])
            demo_urls = result.get("components", {}).get("demo_urls", [])

            click.echo(f"\n[+] Analysis complete!")
            click.echo(f"    Video: {metadata.get('title', 'Unknown')}")
            click.echo(f"    Channel: {metadata.get('channel', 'Unknown')}")
            click.echo(f"    Methodologies found: {len(methodologies)}")
            click.echo(f"    Demo URLs found: {len(demo_urls)}")
            click.echo(f"    Complexity: {result.get('complexity', 'unknown')}")

    except Exception as e:
        click.echo(f"[!] Error: {str(e)}", err=True)
        sys.exit(1)


def generate_markdown(result: dict) -> str:
    """Generate markdown output from result."""
    md = []
    md.append("# Implementation Plan\n")

    # Video info
    video = result.get("components", {}).get("video", {})
    if video:
        md.append(f"## Video Information\n")
        md.append(f"- **Title**: {video.get('title', 'Unknown')}")
        md.append(f"- **Channel**: {video.get('channel', 'Unknown')}")
        md.append(f"- **Duration**: {video.get('duration', 0)} seconds")
        md.append(f"- **URL**: {video.get('url', '')}\n")

    # Methodologies
    methodologies = result.get("components", {}).get("methodologies", [])
    if methodologies:
        md.append(f"## Methodologies ({len(methodologies)})\n")
        for i, method in enumerate(methodologies, 1):
            md.append(f"### {i}. {method.get('name', 'Unnamed')}")
            md.append(f"- **Type**: {method.get('type', 'technique')}")

            steps = method.get("steps", [])
            if steps:
                md.append(f"- **Steps**:")
                for step in steps:
                    md.append(
                        f"  {step.get('step', '?')}. {step.get('description', '')}"
                    )

            tools = method.get("tools", [])
            if tools:
                md.append(f"- **Tools**: {', '.join(tools)}")

            md.append("")  # Blank line

    # Demo URLs
    demo_urls = result.get("components", {}).get("demo_urls", [])
    if demo_urls:
        md.append(f"## Demo Environments ({len(demo_urls)})\n")
        for demo in demo_urls:
            md.append(f"- **{demo.get('type', 'link')}**: {demo.get('url', '')}")
        md.append("")
    else:
        md.append("## Demo Environments\n")
        md.append("No demo environments detected.\n")

    # Prerequisites
    prerequisites = result.get("prerequisites", [])
    if prerequisites:
        md.append(f"## Prerequisites ({len(prerequisites)})\n")
        for prereq in prerequisites:
            md.append(
                f"- **{prereq.get('tool', '')}**: {prereq.get('description', '')}"
            )
        md.append("")

    # Implementation steps
    steps = result.get("steps", [])
    if steps:
        md.append(f"## Implementation Steps ({len(steps)})\n")
        for i, step in enumerate(steps, 1):
            category = step.get("category", "")
            description = step.get("description", "")
            methodology = step.get("methodology", "")

            md.append(f"{i}. {description}")
            if category:
                md.append(f"   - Category: {category}")
            if methodology:
                md.append(f"   - From: {methodology}")
        md.append("")

    # Verification
    verification = result.get("verification", [])
    if verification:
        md.append(f"## Verification Checklist ({len(verification)})\n")
        for item in verification:
            vtype = item.get("type", "")
            desc = item.get("description", "")

            md.append(f"- [{' '}] {desc}")
        md.append("")

    # OS Verification
    os_verification = result.get("components", {}).get("os_verification", {})
    if os_verification:
        available = os_verification.get("available", [])
        missing = os_verification.get("missing", [])
        versions = os_verification.get("versions", {})

        md.append("## OS Capabilities\n")

        if available:
            md.append("### Available Tools\n")
            for tool in available:
                version = versions.get(tool, "")
                md.append(f"- **{tool}**: {version or 'installed'}")
            md.append("")

        if missing:
            md.append("### Missing Tools\n")
            for tool in missing:
                md.append(f"- **{tool}**: needs installation")
            md.append("")

    # Complexity
    complexity = result.get("complexity", "unknown")
    md.append(f"**Complexity**: {complexity}\n")

    return "\n".join(md)


if __name__ == "__main__":
    cli()
