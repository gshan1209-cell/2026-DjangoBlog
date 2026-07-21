#!/bin/bash
# =====================================================================
# Downloading Database from Google Drive (Linux Version)
# =====================================================================

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}==========================================${NC}"
echo -e "${GREEN}Downloading Database from Google Drive...${NC}"
echo -e "${GREEN}==========================================${NC}"

# Load parameters from config.sh
CONFIG_FILE="$(dirname "${BASH_SOURCE[0]}")/config.sh"
if [ -f "$CONFIG_FILE" ]; then
    source "$CONFIG_FILE"
else
    echo -e "${RED}[ERROR] config.sh not found.${NC}"
    exit 1
fi

echo "Target DB Path: $DB_PATH"

DOWNLOAD_SUCCESS=1

if command -v curl >/dev/null 2>&1; then
    echo "Using curl to download..."
    curl -L "$DOWNLOAD_URL" -o "$DB_PATH"
    DOWNLOAD_SUCCESS=$?
elif command -v wget >/dev/null 2>&1; then
    echo "curl not found. Falling back to wget..."
    wget -O "$DB_PATH" "$DOWNLOAD_URL"
    DOWNLOAD_SUCCESS=$?
else
    echo -e "${RED}[ERROR] Neither curl nor wget was found on the system.${NC}"
    echo "Please install curl or wget and try again."
    exit 1
fi

if [ $DOWNLOAD_SUCCESS -ne 0 ]; then
    echo ""
    echo -e "${RED}[ERROR] Failed to download the database file.${NC}"
    exit $DOWNLOAD_SUCCESS
fi

if [ ! -f "$DB_PATH" ]; then
    echo ""
    echo -e "${RED}[ERROR] Database file was not created successfully.${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}==========================================${NC}"
echo -e "${GREEN}Database downloaded successfully!${NC}"
echo "Saved as: $DB_PATH"
echo -e "${GREEN}==========================================${NC}"
