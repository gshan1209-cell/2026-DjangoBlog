#!/bin/bash
# =====================================================================
# Setting up Python Virtual Environment (Linux Version)
# =====================================================================

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}==========================================${NC}"
echo -e "${GREEN}Setting up Python Virtual Environment...${NC}"
echo -e "${GREEN}==========================================${NC}"

# Check if Python 3 is installed
PYTHON_CMD=""
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
fi

if [ -z "$PYTHON_CMD" ]; then
    echo -e "${RED}[ERROR] Python is not installed or not in PATH.${NC}"
    echo "Please install Python 3 and try again."
    exit 1
fi

echo -e "Using Python command: ${GREEN}$PYTHON_CMD${NC} ($( $PYTHON_CMD --version 2>&1 ))"

# Create virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment in .venv..."
    $PYTHON_CMD -m venv .venv
    if [ $? -ne 0 ]; then
        echo -e "${RED}[ERROR] Failed to create virtual environment.${NC}"
        exit 1
    fi
    echo -e "${GREEN}Virtual environment created successfully.${NC}"
else
    echo ".venv already exists. Skipping creation."
fi

# Upgrade pip
echo "Upgrading pip..."
if [ -f ".venv/bin/python" ]; then
    .venv/bin/python -m pip install --upgrade pip
else
    echo -e "${RED}[ERROR] Virtual environment Python binary not found at .venv/bin/python.${NC}"
    exit 1
fi

# Install dependencies
if [ -f "requirement.txt" ]; then
    echo "Installing dependencies from requirement.txt..."
    .venv/bin/python -m pip install -r requirement.txt
    if [ $? -ne 0 ]; then
        echo -e "${RED}[ERROR] Failed to install dependencies.${NC}"
        exit 1
    fi
else
    echo -e "${YELLOW}[WARNING] requirement.txt not found. Skipping installation.${NC}"
fi

echo -e "${GREEN}==========================================${NC}"
echo -e "${GREEN}Setup completed successfully!${NC}"
echo -e "${GREEN}==========================================${NC}"
