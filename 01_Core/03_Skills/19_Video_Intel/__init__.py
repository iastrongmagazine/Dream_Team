"""
Video Intel Skill - Extract structured knowledge from YouTube videos and GitHub repos.

This skill provides:
- Video transcription and metadata extraction (yt-dlp + whisper)
- Repository code analysis (git clone + AST parsing)
- Implementation plan generation with OS verification

Usage:
    from video_intel import VideoAnalyzer, RepoScanner, SynthesisEngine

    engine = SynthesisEngine()
    result = engine.synthesize("https://youtube.com/...", "https://github.com/...")
"""

__version__ = "0.1.0"
__author__ = "personal-os"

from .video_analyzer import VideoAnalyzer
from .repo_scanner import RepoScanner
from .synthesis_engine import SynthesisEngine
from .video_registry import VideoRegistry

__all__ = [
    "VideoAnalyzer",
    "RepoScanner",
    "SynthesisEngine",
    "VideoRegistry",
]
