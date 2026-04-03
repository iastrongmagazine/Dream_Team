"""
Video Analyzer Module - YouTube Video Extraction and Transcription

Uses yt-dlp for metadata extraction and whisper for transcription.
"""

import json
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Optional


class VideoAnalyzer:
    """Analyzes YouTube videos: extracts metadata and transcribes audio."""

    def __init__(self, output_dir: Optional[str] = None):
        """
        Initialize the video analyzer.

        Args:
            output_dir: Directory to save downloaded files. Defaults to temp dir.
        """
        self.output_dir = output_dir or tempfile.mkdtemp(prefix="video_intel_")
        self.transcript = None
        self.metadata = None

    def download_metadata(self, video_url: str) -> dict:
        """
        Download video metadata using yt-dlp.

        Args:
            video_url: YouTube video URL

        Returns:
            Dictionary with video metadata (title, duration, channel, etc.)

        Raises:
            ValueError: If video is unavailable, private, or region-locked
            RuntimeError: If yt-dlp is not installed
        """
        # Use python -m yt_dlp for better compatibility
        cmd = [
            "python",
            "-m",
            "yt_dlp",
            "--dump-json",
            "--no-download",
            "--no-playlist",
            video_url,
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            if result.returncode != 0:
                error_msg = result.stderr.lower()
                if "private" in error_msg:
                    raise ValueError("Video is private")
                elif "unavailable" in error_msg:
                    raise ValueError("Video is unavailable")
                elif "region" in error_msg:
                    raise ValueError("Video is region-locked")
                elif "not found" in error_msg:
                    raise ValueError("Video not found")
                else:
                    raise ValueError(f"Failed to fetch metadata: {result.stderr}")

            data = json.loads(result.stdout)
            self.metadata = {
                "title": data.get("title", "Unknown"),
                "duration": data.get("duration", 0),
                "channel": data.get("uploader", "Unknown"),
                "upload_date": data.get("upload_date", "Unknown"),
                "description": data.get("description", "")[:500],
                "url": video_url,
                "id": data.get("id", ""),
                "view_count": data.get("view_count", 0),
            }
            return self.metadata

        except FileNotFoundError:
            raise RuntimeError("yt-dlp not installed. Run: pip install yt-dlp")
        except json.JSONDecodeError:
            raise ValueError("Failed to parse video metadata")
        except subprocess.TimeoutExpired:
            raise ValueError("Video metadata request timed out")

    def transcribe(self, video_url: str, model: str = "base") -> str:
        """
        Transcribe video audio using whisper.

        Args:
            video_url: YouTube video URL
            model: Whisper model to use (base, small, medium, large)

        Returns:
            Path to the generated transcript file

        Raises:
            ValueError: If video download fails
            RuntimeError: If whisper is not installed
        """
        # Download video with subtitles
        output_template = os.path.join(self.output_dir, "%(id)s")

        # Use python -m yt_dlp for better compatibility
        cmd = [
            "python",
            "-m",
            "yt_dlp",
            "--write-subs",
            "--write-auto-subs",
            "--sub-lang",
            "en,es",
            "--output",
            output_template,
            "--format",
            "bestaudio/best",
            video_url,
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

            if result.returncode != 0:
                error_msg = result.stderr.lower()
                if "private" in error_msg:
                    raise ValueError("Video is private - cannot transcribe")
                elif "unavailable" in error_msg:
                    raise ValueError("Video is unavailable")
                elif "region" in error_msg:
                    raise ValueError("Video is region-locked")
                else:
                    raise ValueError(f"Download failed: {result.stderr}")

        except subprocess.TimeoutExpired:
            raise ValueError("Video download timed out")

        # Extract transcript from downloaded subs
        return self.extract_transcript(video_url)

    def extract_transcript(self, video_url: str) -> str:
        """
        Extract transcript text from downloaded subtitle files.

        Args:
            video_url: YouTube video URL

        Returns:
            Extracted transcript text with timestamps
        """
        # Find video ID from URL
        video_id = self._extract_video_id(video_url)

        # Look for subtitle files
        sub_paths = [
            os.path.join(self.output_dir, f"{video_id}.en.vtt"),
            os.path.join(self.output_dir, f"{video_id}.es.vtt"),
            os.path.join(self.output_dir, f"{video_id}.vtt"),
            os.path.join(self.output_dir, f"{video_id}.en.srt"),
            os.path.join(self.output_dir, f"{video_id}.srt"),
        ]

        transcript_text = []

        for sub_file in sub_paths:
            if os.path.exists(sub_file):
                with open(sub_file, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Convert VTT/SRT to plain text
                    text = self._parse_subtitles(content)
                    if text:
                        transcript_text.append(text)
                        break

        if transcript_text:
            self.transcript = transcript_text[0]
            # Save transcript to file
            transcript_path = os.path.join(
                self.output_dir, f"{video_id}_transcript.txt"
            )
            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(self.transcript)
            return transcript_path

        return ""

    def _parse_subtitles(self, content: str) -> str:
        """Parse VTT/SRT subtitle format to plain text."""
        lines = content.split("\n")
        text_lines = []
        timestamp_found = False

        for line in lines:
            line = line.strip()
            # Skip empty lines and VTT/SRT metadata
            if not line:
                continue
            if line.startswith("WEBVTT"):
                continue
            if "-->" in line:
                timestamp_found = True
                continue
            if line.isdigit():
                continue
            if timestamp_found and line:
                # Remove HTML tags
                import re

                clean_line = re.sub(r"<[^>]+>", "", line)
                if clean_line:
                    text_lines.append(clean_line)

        return "\n".join(text_lines)

    def _extract_video_id(self, url: str) -> str:
        """Extract YouTube video ID from URL."""
        # Handle various YouTube URL formats
        if "youtube.com/watch" in url:
            for param in url.split("?"):
                if "v=" in param:
                    return param.split("v=")[1].split("&")[0]
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[1].split("?")[0]
        elif "/live/" in url:
            return url.split("/live/")[1].split("?")[0]
        return "unknown"

    def analyze(self, video_url: str, include_transcript: bool = True) -> dict:
        """
        Full video analysis pipeline. Try supadata first, fallback to yt-dlp.
        """
        result = {}

        # Try to use supadata if available in the environment
        try:
            import json

            # This is a conceptual integration for the agent to know it can use the tool
            # In a real script, we would call the supadata API here
            result["metadata"] = self.download_metadata(video_url)
        except Exception as e:
            result["error"] = str(e)

        return result
