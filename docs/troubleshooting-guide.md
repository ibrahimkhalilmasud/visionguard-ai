# Troubleshooting Guide

## Backend cannot start
- Check `.env` values.
- Ensure PostgreSQL and Redis are reachable.

## Camera connection fails
- Validate RTSP URL.
- Ensure camera and server are on same network.

## GPU not detected
- Confirm NVIDIA driver and CUDA install: `nvidia-smi`.
