#!/usr/bin/env python3
"""
Sync all git submodules to their configured branches.

Reads .gitmodules, and for each submodule:
  1. git fetch origin
  2. git checkout <branch>
  3. git pull origin <branch>

After syncing, updates README.md index.
"""

import os
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent

def run(cmd, cwd=None, check=True):
    """Run a shell command."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if check and result.returncode != 0:
        return None, result.stderr.strip()
    return result.stdout.strip(), result.stderr.strip()

def parse_gitmodules():
    """Parse .gitmodules and return list of {name, path, url, branch} dicts."""
    gitmodules_path = REPO_ROOT / ".gitmodules"
    if not gitmodules_path.exists():
        print("ERROR: .gitmodules not found", file=sys.stderr)
        sys.exit(1)

    content = gitmodules_path.read_text()
    submodules = []
    current = {}

    for line in content.splitlines():
        # Match [submodule "name"]
        m = re.match(r'\[submodule\s+"(.+)"\]', line)
        if m:
            if current:
                submodules.append(current)
            current = {"name": m.group(1)}
            continue

        # Match key = value
        m = re.match(r'\s*(path|url|branch)\s*=\s*(.+)', line)
        if m and current:
            current[m.group(1)] = m.group(2).strip()

    if current:
        submodules.append(current)

    return submodules

def sync_submodule(sm):
    """Sync a single submodule to its configured branch."""
    path = sm.get("path", "")
    url = sm.get("url", "")
    branch = sm.get("branch", "")
    name = sm.get("name", path)

    if not branch:
        print(f"  ⚠ {name}: no branch configured, skipping")
        return "skipped"

    full_path = REPO_ROOT / path
    if not full_path.exists():
        print(f"  ⚠ {name}: path {path} does not exist, skipping")
        return "skipped"

    print(f"  Syncing {name} -> {branch} ...")

    # Fetch
    out, err = run(f"git fetch origin", cwd=full_path)
    if out is None:
        print(f"    ✗ fetch failed: {err}")
        return "failed"

    # Checkout branch
    out, err = run(f"git checkout {branch}", cwd=full_path)
    if out is None:
        print(f"    ✗ checkout failed: {err}")
        return "failed"

    # Pull (merge)
    out, err = run(f"git pull origin {branch}", cwd=full_path)
    if out is None:
        print(f"    ✗ pull failed: {err}")
        return "failed"

    # Get current commit for reporting
    commit, _ = run(f"git rev-parse --short HEAD", cwd=full_path)
    print(f"    ✓ {branch} @ {commit}")
    return "ok"

def main():
    os.chdir(REPO_ROOT)

    submodules = parse_gitmodules()
    print(f"Found {len(submodules)} submodules in .gitmodules\n")

    results = {"ok": 0, "skipped": 0, "failed": 0}

    for sm in submodules:
        status = sync_submodule(sm)
        results[status] = results.get(status, 0) + 1

    print(f"\n{'='*50}")
    print(f"Sync complete: {results['ok']} ok, {results['skipped']} skipped, {results['failed']} failed")

    # Update README
    update_script = REPO_ROOT / ".agents/skills/submodule-manager/scripts/update_readme.py"
    if update_script.exists():
        print("\nUpdating README.md index...")
        run(f"python3 {update_script}", cwd=REPO_ROOT)
        print("✓ README.md updated.")

    if results["failed"] > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
