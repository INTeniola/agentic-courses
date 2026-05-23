#!/usr/bin/env bash
set -euo pipefail

# SageMaker Studio JupyterLab lifecycle config for the AI Beginner Bootcamp.
# Attach this script to the instructor's Studio space so dependencies are ready
# before each live session.

BOOTCAMP_DIR="${BOOTCAMP_DIR:-$HOME/ai-beginner-bootcamp-outline}"
REPO_URL="${BOOTCAMP_REPO_URL:-}"

python -m pip install --upgrade pip

if [ -n "$REPO_URL" ]; then
  if [ -d "$BOOTCAMP_DIR/.git" ]; then
    git -C "$BOOTCAMP_DIR" pull --ff-only
  elif [ ! -d "$BOOTCAMP_DIR" ]; then
    git clone "$REPO_URL" "$BOOTCAMP_DIR"
  fi
fi

if [ -f "$BOOTCAMP_DIR/requirements.txt" ]; then
  python -m pip install -r "$BOOTCAMP_DIR/requirements.txt"
fi

python -m ipykernel install --user --name ai-beginner-bootcamp --display-name "Python (AI Beginner Bootcamp)"

echo "AI Beginner Bootcamp environment is ready at $BOOTCAMP_DIR"
