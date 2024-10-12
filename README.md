# workflow

## Install

Clone the repository.

```
git clone git@github.com:anatolethien/workflow.git project
```

Destroy the current git repository and the sample data.

```
rm -rf .git/
rm -rf data/* downloads/*
```

Initiate a Python virtual environment and install dependencies.

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
