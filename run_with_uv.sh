#!/bin/bash
# Script to run MCP server using uv instead of Python venv

# Create a uv environment if it doesn't exist
if [ ! -d ".uv" ]; then
    echo "Creating uv environment..."
    uv venv .uv
fi

# Activate the uv environment
source .uv/bin/activate

# Install required packages
echo "Installing required packages..."
uv pip install boto3 "mcp[cli]" requests fastmcp httpx python-dotenv

# Run the MCP server
echo "Starting MCP server..."
python mcp_server.py