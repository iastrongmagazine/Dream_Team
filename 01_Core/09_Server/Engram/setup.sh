#!/usr/bin/env bash

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
Skills_SOURCE="${REPO_ROOT}/Skills"

if [ ! -d "${Skills_SOURCE}" ]; then
  echo "Skills directory not found at ${Skills_SOURCE}" >&2
  exit 1
fi

link_Skills() {
  local agent_dir="$1"
  local target_dir="${agent_dir}/Skills"
  local source_path=""
  local skill_name=""
  local link_path=""

  mkdir -p "${target_dir}"

  # Remove legacy aggregate link if present.
  if [ -L "${target_dir}/engram" ]; then
    rm -f "${target_dir}/engram"
  fi

  for source_path in "${Skills_SOURCE}"/*; do
    skill_name="$(basename "${source_path}")"
    link_path="${target_dir}/${skill_name}"
    ln -sfn "${source_path}" "${link_path}"
    echo "linked ${link_path} -> ${source_path}"
  done
}

link_Skills "${REPO_ROOT}/.claude"
link_Skills "${REPO_ROOT}/.codex"
link_Skills "${REPO_ROOT}/.gemini"

echo
echo "Done. Skills linked for project .claude, .codex, and .gemini"
