# Doruk Village

Doruk Village is an autonomous multi-agent development environment for building and testing Godot 4 game projects.

## Overview

- Python FastAPI backend with a real orchestration layer
- Multi-agent task system and message bus
- NVIDIA NIM provider integration via the OpenAI-compatible endpoint
- Safe sandboxed tool system with real file, command, git, and project operations
- Moderator dashboard and live events
- Godot 4 demo project for a small 3D car football game

## Features

- Agent roles: Director, Programmer, Level Designer, Asset Designer, Tester, Improver
- Task queue with statuses: PENDING, ASSIGNED, RUNNING, BLOCKED, FAILED, COMPLETED
- Secure file and command policies
- Persistent agent memory and logs
- Real Git support and benchmark tracking
- Demo project generation under `workspace/game`

## Quick start

1. Install dependencies
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Set environment variables
   ```bash
   cp .env.example .env
   # then populate
   ```
3. Start the Village
   ```bash
   ./start.sh
   ```
4. Open the dashboard
   - `http://localhost:8000/`

## Demo

Use the dashboard or POST to `/api/demo/start` to generate the Godot car football demo project.

## Project structure

```text
.
├── agents/
├── backend/
├── benchmarks/
├── frontend/
├── logs/
├── tasks/
├── tests/
├── workspace/
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
├── start.sh
└── ...
```

## Environment variables

- `NVIDIA_API_KEY`
- `NVIDIA_MODEL`

## Notes

The NVIDIA provider uses the OpenAI-compatible endpoint:

`https://integrate.api.nvidia.com/v1`

The application reads credentials from the environment and never hard-codes them.
