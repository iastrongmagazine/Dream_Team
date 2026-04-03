"""
Repository Scanner Module - GitHub Repository Analysis

Clones GitHub repositories and analyzes code structure using AST parsing.
"""

import ast
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Optional


class RepoScanner:
    """Scans GitHub repositories: clones, parses AST, generates code map."""

    def __init__(self, workspace_dir: Optional[str] = None):
        """
        Initialize the repo scanner.

        Args:
            workspace_dir: Directory for cloned repos. Defaults to temp dir.
        """
        self.workspace_dir = workspace_dir or tempfile.mkdtemp(prefix="repo_scan_")
        self.cloned_path = None
        self.code_map = None

    def clone_repo(self, repo_url: str, branch: Optional[str] = None) -> str:
        """
        Clone a GitHub repository to temporary directory.

        Args:
            repo_url: GitHub repository URL (https://github.com/user/repo or git@github.com:user/repo.git)
            branch: Branch to clone. Defaults to main/master.

        Returns:
            Path to cloned repository

        Raises:
            ValueError: If repository is invalid, private, or requires auth
            RuntimeError: If git is not installed
        """
        # Clean URL
        repo_url = self._clean_repo_url(repo_url)

        # Determine output path
        repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")
        output_path = os.path.join(self.workspace_dir, repo_name)

        # Build git clone command
        cmd = ["git", "clone", "--depth", "1"]

        if branch:
            cmd.extend(["--branch", branch])

        cmd.extend([repo_url, output_path])

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

            if result.returncode != 0:
                error_msg = result.stderr.lower()
                if "authentication" in error_msg or "permission" in error_msg:
                    raise ValueError(
                        "Repository requires authentication. Run: gh auth login"
                    )
                elif "not found" in error_msg:
                    raise ValueError("Repository not found")
                elif "private" in error_msg:
                    raise ValueError(
                        "Repository is private and requires authentication"
                    )
                else:
                    raise ValueError(f"Failed to clone: {result.stderr}")

            self.cloned_path = output_path
            return output_path

        except FileNotFoundError:
            raise RuntimeError("git not installed")
        except subprocess.TimeoutExpired:
            raise ValueError("Repository clone timed out")

    def _clean_repo_url(self, url: str) -> str:
        """Normalize GitHub URL format."""
        # Remove trailing .git
        url = url.rstrip("/").replace(".git", "")

        # Convert git@ URLs to https
        if url.startswith("git@github.com:"):
            user_repo = url.replace("git@github.com:", "")
            return f"https://github.com/{user_repo}"

        return url

    def parse_ast(self, file_path: str) -> dict:
        """
        Parse a Python file using AST to extract structure.

        Args:
            file_path: Path to Python file

        Returns:
            Dictionary with imports, classes, functions
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                source = f.read()

            tree = ast.parse(source)

            result = {
                "imports": [],
                "from_imports": [],
                "classes": [],
                "functions": [],
                "docstring": ast.get_docstring(tree) or "",
            }

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        result["imports"].append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    for alias in node.names:
                        result["from_imports"].append(
                            f"{node.module}.{alias.name}" if node.module else alias.name
                        )
                elif isinstance(node, ast.ClassDef):
                    methods = [
                        n.name for n in node.body if isinstance(n, ast.FunctionDef)
                    ]
                    result["classes"].append(
                        {
                            "name": node.name,
                            "methods": methods,
                            "docstring": ast.get_docstring(node) or "",
                        }
                    )
                elif isinstance(node, ast.FunctionDef):
                    result["functions"].append(
                        {
                            "name": node.name,
                            "args": [arg.arg for arg in node.args.args],
                            "docstring": ast.get_docstring(node) or "",
                        }
                    )

            return result

        except SyntaxError as e:
            return {
                "error": f"Syntax error: {e}",
                "imports": [],
                "classes": [],
                "functions": [],
            }
        except Exception as e:
            return {"error": str(e), "imports": [], "classes": [], "functions": []}

    def generate_code_map(self, repo_path: Optional[str] = None) -> dict:
        """
        Generate a complete code map of the repository.

        Args:
            repo_path: Path to cloned repository. Uses self.cloned_path if None.

        Returns:
            Structured code map with file tree, imports, functions, classes
        """
        repo_path = repo_path or self.cloned_path

        if not repo_path or not os.path.exists(repo_path):
            raise ValueError("No repository cloned. Call clone_repo() first.")

        code_map = {
            "repo_path": repo_path,
            "files": [],
            "file_tree": {},
            "summary": {
                "total_files": 0,
                "python_files": 0,
                "total_imports": set(),
                "total_classes": 0,
                "total_functions": 0,
            },
        }

        # Walk through directory
        for root, dirs, files in os.walk(repo_path):
            # Skip hidden and common non-code directories
            dirs[:] = [
                d
                for d in dirs
                if not d.startswith(".")
                and d not in ("node_modules", "__pycache__", "venv", "env")
            ]

            rel_path = os.path.relpath(root, repo_path)

            for file in files:
                file_path = os.path.join(root, file)
                rel_file_path = os.path.relpath(file_path, repo_path)

                file_info = {"path": rel_file_path, "size": os.path.getsize(file_path)}

                # Parse Python files
                if file.endswith(".py"):
                    code_map["summary"]["python_files"] += 1
                    ast_result = self.parse_ast(file_path)
                    file_info.update(ast_result)

                    # Update summary
                    code_map["summary"]["total_imports"].update(
                        ast_result.get("imports", [])
                    )
                    code_map["summary"]["total_imports"].update(
                        ast_result.get("from_imports", [])
                    )
                    code_map["summary"]["total_classes"] += len(
                        ast_result.get("classes", [])
                    )
                    code_map["summary"]["total_functions"] += len(
                        ast_result.get("functions", [])
                    )

                code_map["files"].append(file_info)

        code_map["summary"]["total_files"] = len(code_map["files"])
        code_map["summary"]["total_imports"] = list(
            code_map["summary"]["total_imports"]
        )

        self.code_map = code_map
        return code_map

    def scan_repo(self, repo_url: str) -> dict:
        """
        Full repository scan pipeline.

        Args:
            repo_url: GitHub repository URL

        Returns:
            Complete code map of the repository
        """
        self.clone_repo(repo_url)
        return self.generate_code_map()

    def cleanup(self):
        """Remove cloned repository to free disk space."""
        if self.cloned_path and os.path.exists(self.cloned_path):
            shutil.rmtree(self.cloned_path, ignore_errors=True)
        if os.path.exists(self.workspace_dir):
            shutil.rmtree(self.workspace_dir, ignore_errors=True)

    def __del__(self):
        """Cleanup on deletion."""
        self.cleanup()
