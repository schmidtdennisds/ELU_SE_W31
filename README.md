# Shopping Cart – GitHub Actions CI

This project uses **GitHub Actions** to automate static code analysis and unit testing for a Python shopping cart application.

## CI Workflow

The workflow is defined in `.github/workflows/ci.yml` and runs automatically on every push to the repository.

It consists of two jobs:

### 1. Static Analysis (Build)

- Sets up Python and installs dependencies.
- Runs **Pylint** to check Python code quality and coding standards.
- The workflow fails if Pylint reports errors.

### 2. Automated Testing (Test)

- Runs after the build job succeeds.
- Installs **pytest** and **pytest-cov**.
- Executes `test_shopping_cart.py` to verify:
  - Correct calculation of shopping cart totals.
  - Correct logging of the total price.

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
pip install pylint pytest pytest-cov
```

Run static analysis and tests:

```bash
pylint shopping_cart.py test_shopping_cart.py
pytest test_shopping_cart.py
```

## Results

Workflow results can be viewed in the repository's **Actions** tab.

The CI pipeline helps ensure code quality and functionality are automatically verified with every push.

## Documentation

[GitHub Actions Documentation](https://docs.github.com/en/actions)