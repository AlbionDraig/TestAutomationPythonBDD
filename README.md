# Python Project Setup Guide

Here are the steps to configure and run a Python project using a virtual environment. Make sure you have Python installed on your system before starting.

## Step 1: Activate the Virtual Environment

```bash
.\TestEnv\Scripts\Activate
```

This command will activate the virtual environment named "TestEnv". Ensure that you are in the correct directory before running it.

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This command will install the project dependencies from the `requirements.txt` file. Make sure the requirements file is present in the project directory.

## Step 3: Install Playwright

```bash
playwright install
```

This command will install Playwright, a tool for automating web browsers. Ensure you have Node.js installed on your system before running this command.

## Step 4: Run Tests with Pytest

```bash
pytest .\tests\steps\Number_Test.py
```

This command will execute tests using Pytest. Ensure the path to the test file is correct, and you have activated the virtual environment before running the tests.

Now you are ready to run your Python project! Make sure to follow these steps in the specified order to avoid configuration issues.