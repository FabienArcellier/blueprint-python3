# Maintain this blueprint

This blueprint is a python project template. It may need to be rebuilt regularly, especially to update the stack dependencies.

### 1. choose a python version

I am using the version of python present in the latest LTS of ubuntu.

### 2. update the dependencies

```bash
poetry add python-dotenv@latest

poetry add --dev alfred-cli@latest
poetry add --dev mypy@latest
poetry add --dev pytest@latest
poetry add --dev ruff@latest
```

