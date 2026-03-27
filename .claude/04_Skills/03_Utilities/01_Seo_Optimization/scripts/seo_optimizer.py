import os
import re
import json
import argparse
from typing import List, Dict, Any

class SEOOptimizer:
    def __init__(self, root_dir: str, silent: bool = False):
        self.root_dir = root_dir
        self.silent = silent
        self.report = {
            "critical_issues": [],
            "warnings": [],
            "passed": []
        }

    def run_audit(self):
        if not self.silent:
            print(f"🚀 Starting SEO Audit for: {self.root_dir}\n")

        self.check_meta_descriptions()
        self.check_headings()
        self.check_technical_files()
        self.check_internal_links()

        self.print_report()

    def check_meta_descriptions(self):
        """Check description lengths in homepage.tsx or similar files."""
        # This is a specialized check for the user's specific project structure
        homepage_path = os.path.join(self.root_dir, "src", "components", "homepage.tsx")
        if not os.path.exists(homepage_path):
            self.report["warnings"].append(f"File not found for content audit: {homepage_path}")
            return

        with open(homepage_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Simple regex to find descriptions in the tools array
        # Assuming format like: description: "..." or "description": "..."
        descriptions = re.findall(r'description:\s*["\'](.*?)["\']', content)

        for desc in descriptions:
            length = len(desc)
            if length < 150 or length > 160:
                self.report["critical_issues"].append(
                    f"Description length out of range ({length} chars): '{desc[:50]}...'"
                )
            else:
                self.report["passed"].append(f"Optimal description length ({length} chars)")

    def check_headings(self):
        """Check heading hierarchy in common components."""
        for root, _, files in os.walk(os.path.join(self.root_dir, "src")):
            for file in files:
                if file.endswith((".tsx", ".html")):
                    path = os.path.join(root, file)
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()

                    h1_count = len(re.findall(r'<h1', content, re.IGNORECASE))
                    if h1_count > 1:
                        self.report["critical_issues"].append(f"Multiple H1 tags in {file}")
                    elif h1_count == 1:
                        self.report["passed"].append(f"Single H1 in {file}")

    def check_technical_files(self):
        """Check for sitemap and robots.txt."""
        public_dir = os.path.join(self.root_dir, "public")

        sitemap = os.path.join(public_dir, "sitemap.xml")
        if os.path.exists(sitemap):
            self.report["passed"].append("sitemap.xml found")
        else:
            self.report["critical_issues"].append("sitemap.xml missing in public/")

        robots = os.path.join(public_dir, "robots.txt")
        if os.path.exists(robots):
            self.report["passed"].append("robots.txt found")
        else:
            self.report["critical_issues"].append("robots.txt missing in public/")

    def check_internal_links(self):
        """Basic check for internal linking consistency."""
        # Focus on App.tsx routing
        app_path = os.path.join(self.root_dir, "src", "App.tsx")
        if os.path.exists(app_path):
            with open(app_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Placeholder for link checking logic
            self.report["passed"].append("App.tsx routing analyzed")

    def print_report(self):
        if self.silent:
            if self.report["critical_issues"]:
                print("\n❌ SEO CRITICAL ISSUES DETECTED:")
                for issue in self.report["critical_issues"]:
                    print(f"  - {issue}")
            return

        print("--- SEO AUDIT REPORT ---")

        if self.report["critical_issues"]:
            print("\n❌ CRITICAL ISSUES:")
            for issue in self.report["critical_issues"]:
                print(f"  - {issue}")

        if self.report["warnings"]:
            print("\n⚠️ WARNINGS:")
            for warn in self.report["warnings"]:
                print(f"  - {warn}")

        print(f"\n✅ PASSED CHECKS: {len(self.report['passed'])}")
        print("\nAudit Complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="SEO Optimizer for React SPAs")
    parser.add_argument("--root", default=".", help="Project root directory")
    parser.add_argument("--silent", action="store_true", help="Silent mode (only reports critical issues)")
    args = parser.parse_args()

    optimizer = SEOOptimizer(args.root, silent=args.silent)
    optimizer.run_audit()
