#!/bin/bash
# Edu network Local Launcher
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR/viewer-platform"

# Load node from nvm if present
if [ -s "$HOME/.nvm/nvm.sh" ]; then
  source "$HOME/.nvm/nvm.sh"
fi

echo "========================================================"
echo "   🌟 Starting Edu network Platform..."
echo "========================================================"
echo ""
echo "🚀 Opening server on http://localhost:5001"
echo "Press Ctrl+C to stop the server anytime."
echo ""

# Open in browser automatically
sleep 2 && open "http://localhost:5001" &

npm start
