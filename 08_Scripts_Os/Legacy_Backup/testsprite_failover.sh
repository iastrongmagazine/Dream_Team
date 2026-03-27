#!/bin/bash
# Failover wrapper for TestSprite MCP server
# Needs environment variables TESTSPRITE_PRIMARY and TESTSPRITE_BACKUP

# Set API_KEY based on available variables.
# This script should be invoked by .mcp.json

if [ -z "$TESTSPRITE_PRIMARY" ]; then
    echo "ERROR: TESTSPRITE_PRIMARY not set" >&2
    exit 1
fi

# Attempt to run with primary
export API_KEY=$TESTSPRITE_PRIMARY
echo "Starting TestSprite MCP with Primary API Key" >&2
npx.cmd -y @testsprite/testsprite-mcp@latest
exit_code=$?

# If failed (non-zero exit code), retry with backup
if [ $exit_code -ne 0 ]; then
    if [ -z "$TESTSPRITE_BACKUP" ]; then
        echo "ERROR: TESTSPRITE_BACKUP not set" >&2
        exit $exit_code
    fi
    echo "Primary failed, retrying with Backup API Key" >&2
    export API_KEY=$TESTSPRITE_BACKUP
    npx.cmd -y @testsprite/testsprite-mcp@latest
fi
