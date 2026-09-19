#!/bin/bash
# Edu network 1-Command Universal Launcher

# 1. Load Node/NVM environment
if [ -s "$HOME/.nvm/nvm.sh" ]; then
  export NVM_DIR="$HOME/.nvm"
  source "$HOME/.nvm/nvm.sh"
fi

# Fallback path if nvm not sourced
export PATH="$HOME/.nvm/versions/node/v24.20.0/bin:$PATH"

# 2. Navigate to project
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$SCRIPT_DIR/viewer-platform" || exit 1

# 3. Kill any existing instance on port 5001
lsof -ti:5001 | xargs kill -9 2>/dev/null || true

echo "========================================================"
echo "   🌟 Starting Edu network Platform..."
echo "========================================================"
echo ""
echo "🚀 Web is running on: http://localhost:5001"
echo "Press Ctrl+C to stop."
echo ""

# Automatically open in default browser after 1.5 seconds
(sleep 1.5 && open "http://localhost:5001") &

# Start Node server
node server/index.js
