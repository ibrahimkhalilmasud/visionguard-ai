#!/usr/bin/env bash
set -euo pipefail

sudo apt update
sudo apt install -y python3.11 python3.11-venv python3-pip git ffmpeg redis postgresql postgresql-contrib
