#!/usr/bin/env python3
"""
EZFile Hook: Block Network Commands
Type: PreToolUse (Bash)

Prevents any network-related commands from executing.
Tax data must NEVER leave the local machine.
"""

import json
import sys
import re


# Network commands and patterns to block
BLOCKED_COMMANDS = [
    r'\bcurl\b',
    r'\bwget\b',
    r'\bfetch\b',
    r'\bhttp\b',
    r'\bssh\b',
    r'\bscp\b',
    r'\bsftp\b',
    r'\brsync\b',
    r'\bnc\b',
    r'\bnetcat\b',
    r'\bncat\b',
    r'\bsocat\b',
    r'\btelnet\b',
    r'\bftp\b',
    r'\bnslookup\b',
    r'\bdig\b',
    r'\bping\b',
    r'\btraceroute\b',
    r'\baws\s',
    r'\bgcloud\s',
    r'\baz\s',
    r'\bdocker\s+push\b',
    r'\bgit\s+push\b',
    r'\bnpm\s+publish\b',
    r'\bpip\s+install\b',
    r'\bopen\s+https?://',
    r'\bpython.*requests\.',
    r'\bpython.*urllib\.',
    r'\bpython.*http\.',
    r'\bnode.*fetch\(',
    r'\bruby.*net/http',
]


def main():
    try:
        input_data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        # If we can't parse input, allow by default (fail open for non-Bash tools)
        sys.exit(0)

    tool_name = input_data.get("tool_name", "")

    # Only check Bash commands
    if tool_name != "Bash":
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")

    if not command:
        sys.exit(0)

    # Check command against blocked patterns
    for pattern in BLOCKED_COMMANDS:
        if re.search(pattern, command, re.IGNORECASE):
            # Deny the command
            result = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": (
                        "EZFile: Network commands are blocked. "
                        "Tax data must never leave your local machine. "
                        f"Blocked pattern: {pattern}"
                    )
                }
            }
            print(json.dumps(result))
            sys.exit(0)

    # Command is allowed
    sys.exit(0)


if __name__ == "__main__":
    main()
