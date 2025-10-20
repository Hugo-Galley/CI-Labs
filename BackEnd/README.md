# BackEnd (Phantom) - CI Lab

This small Python package `Phantom` is a testbed for the CI workflow defined in `.github/workflows/CI.yml`.

What's included:
- `Phantom/` : package with small utilities
- `tests/` : pytest tests
- `requirements.txt` : test/runtime dependencies used by the CI
- `.flake8` : flake8 configuration used by CI

Quick local setup (macOS, zsh):

```bash
# create and activate a venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# run flake8
flake8

# run tests with coverage and produce coverage.xml for Sonar
pytest --cov=Phantom --cov-report=xml
```

Next steps:
- add dependency scanning (pip-audit or safety)
- expand tests and edge-cases
