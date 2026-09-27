#!/usr/bin/env sh
# Apply the About description, website and topics recorded in
# portable/repository_metadata.json to each public repository.
#
# Dry-run by default: prints the exact `gh repo edit` commands.
# Pass --apply to execute them. Needs `gh` authenticated as the owner
# (or an admin) of d6g8k5htny-coder; App tokens used by cloud agents
# cannot change repository settings, which is why this file exists.
#
# Scientific effect: NONE. Metadata is routing text only.

set -eu

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
json="$here/repository_metadata.json"
mode=${1:-}

python3 - "$json" "$mode" <<'PY'
import json, shlex, subprocess, sys
data = json.load(open(sys.argv[1]))
apply = sys.argv[2] == "--apply"
owner = "d6g8k5htny-coder"
for name, meta in data["repositories"].items():
    if not meta.get("description"):
        print(f"# {name}: skipped ({meta.get('change')})")
        continue
    cmd = ["gh", "repo", "edit", f"{owner}/{name}", "--description", meta["description"]]
    if meta.get("homepage"):
        cmd += ["--homepage", meta["homepage"]]
    for topic in meta.get("topics", []):
        cmd += ["--add-topic", topic]
    print(" ".join(shlex.quote(c) for c in cmd))
    if apply:
        subprocess.run(cmd, check=True)
if not apply:
    print("\n# dry-run only; re-run with --apply to execute", file=sys.stderr)
PY
