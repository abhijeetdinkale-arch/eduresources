#!/bin/bash
# 🌟 Edu network Native Desktop App Launcher (Mac)

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$SCRIPT_DIR/viewer-platform" || exit 1

# Load Node environment
if [ -s "$HOME/.nvm/nvm.sh" ]; then
  export NVM_DIR="$HOME/.nvm"
  source "$HOME/.nvm/nvm.sh"
fi
export PATH="$HOME/.nvm/versions/node/v24.20.0/bin:$PATH"

echo "========================================================"
echo "   🌟 Launching Edu network Desktop App (DRM Protected)..."
echo "========================================================"

# Launch Electron with native window protection
npx electron desktop/main.js
