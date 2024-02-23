# python-project

Python project template for when setting up a new repository.

Set up a virtual environment with the following commands:

```bash
python3 -m venv venv
source venv/bin/activate
```

Contains a requirements.txt file with the following packages for general Python development:

- [loguru](https://loguru.readthedocs.io/en/stable/) for easy logging without the hassle of setting up the python logger
- [mypy](https://mypy-lang.org/) for static type checking
- [pre-commit](https://pre-commit.com/) for running checks before committing and enforcing a consistent code style
- [pytest](https://docs.pytest.org/en/stable/) for unit testing

Install with the following command:

```bash
pip install -r requirements.txt
```

To install pre-commit hooks, run the following command:

```bash
pre-commit install
```

Pre-commit hooks include ruff for linting and formatting of Python code, and prettier for other files.

GitHub Actions are set up to run checks and tests on every push to the repository. You can find the workflow file [here](.github/workflows/check.yml).
