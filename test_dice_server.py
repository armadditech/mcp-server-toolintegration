#!/usr/bin/env python3
"""Test script to verify the dice server works"""
import subprocess
import json

# Test 1: List tools
print("Test 1: Listing available tools...")
result = subprocess.run(
    ["docker", "run", "-i", "--rm", "dice-mcp-server"],
    input='{"jsonrpc":"2.0","method":"tools/list","id":1}\n',
    capture_output=True,
    text=True,
    timeout=10
)

print("STDOUT:", result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
print()

# Test 2: Roll a simple die
print("Test 2: Rolling 1d20...")
roll_request = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "id": 2,
    "params": {
        "name": "roll_dice",
        "arguments": {
            "notation": "1d20"
        }
    }
}

result = subprocess.run(
    ["docker", "run", "-i", "--rm", "dice-mcp-server"],
    input=json.dumps(roll_request) + '\n',
    capture_output=True,
    text=True,
    timeout=10
)

print("STDOUT:", result.stdout)
if result.stderr:
    print("STDERR:", result.stderr)
