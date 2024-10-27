#!/bin/bash

# Get the current directory
CURRENT_DIR=$(pwd)
echo "\n===== Current Directory ====="
echo "$CURRENT_DIR"
echo "==============================\n"

# Determine the Python command to use
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ No Python installation found."
    exit 1
fi

# Get Python version
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)

# Print the Python command and its version
echo "🔍 Using Python command: '$PYTHON_CMD'"
echo "   Python version: '$PYTHON_VERSION'"
echo "==============================\n"

# Make the script executable
chmod +x "$CURRENT_DIR/quicklaunch.py"
echo "✅ Created executable: '$CURRENT_DIR/quicklaunch.py'"
echo "==============================\n"

# Define the alias
ALIAS_NAME="ql"
ALIAS_COMMAND="$CURRENT_DIR/quicklaunch.py"

# Check for the --force flag
FORCE=false
for arg in "$@"; do
    if [[ $arg == "--force" ]]; then
        FORCE=true
    fi
done

# Add the alias to ~/.zshrc
if ! grep -q "alias $ALIAS_NAME=" ~/.zshrc || [ "$FORCE" = true ]; then
    if [ "$FORCE" = true ]; then
        sed -i.bak "/alias $ALIAS_NAME=/d" ~/.zshrc  # Remove existing alias if --force is used
        echo "⚠️ Forcefully removed existing alias '$ALIAS_NAME' from ~/.zshrc"
    fi
    echo "alias $ALIAS_NAME='$ALIAS_COMMAND'" >> ~/.zshrc
    echo "✅ Alias '$ALIAS_NAME' added to ~/.zshrc"

    # Reload the zsh configuration
    echo "\n🔄 Reloading zsh configuration..."
    source ~/.zshrc
    echo "✅ zsh configuration reloaded."
    echo "==============================\n"
else
    echo "⚠️ Alias '$ALIAS_NAME' already exists in ~/.zshrc. Use --force to overwrite."
fi
