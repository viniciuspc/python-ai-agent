# Python AI Agent

Python AI Agent project from [Boot.dev](https://www.boot.dev)!

# Prerequesites
- Python 3.10 + installed
- The [uv](https://github.com/astral-sh/uv) project/package manager ([installation docs](https://docs.astral.sh/uv/getting-started/installation/))
- Access to a Unix-like shell (e.g. ```zsh``` or ```bash```)
- A [Google AI Studio](https://aistudio.google.com/app/welcome) account

# How to run it
Create a ```.env``` file with ```GEMINI_API_KEY``` in it.
 
Create a venv
```bash
uv venv
```

Activate the .venv
```bash
source .venv/bin/activate
```

Sync depencies:
```bash
uv sync
```

Run the project:
```bash
uv run main.py "fix my calculator app, it's not starting correctly"
```

