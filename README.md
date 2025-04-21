# Pytest Robotics Lab

[![codecov](https://codecov.io/gh/LucaMac1/pytest-robotics-lab/branch/master/graph/badge.svg)](https://codecov.io/gh/LucaMac1/pytest-robotics-lab)

This project demonstrates how to use **pytest** to write tests for robotics systems. It includes various types of tests such as unit tests, integration tests, simulation tests, and hardware tests.

## Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/LucaMac1/pytest-robotics-lab.git
   cd pytest-robotics-lab
   ```

2. **Create and activate a virtual environment**  
   It's recommended to use a Python virtual environment to manage dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run tests**  
   You can run specific sets of tests using pytest markers:

   ```bash
   pytest tests/unit
   pytest -m integration
   pytest -m bdd
   ```

5. **Configure CI/CD (Optional)**  
   This project includes a GitHub Actions workflow at `.github/workflows/python-tests.yml` for automated test execution on pushes and pull requests.

## Test Structure

- **Unit tests**: Test individual components like logic or functions.
- **Integration tests**: Test how components interact.
- **System tests**: Test robot behaviour in environments.

## Project Structure

```
pytest-robotics-lab/
├── robot/                          # Robot logic (controllers, sensors, etc.)
│   ├── __init__.py                 # Marks the folder as a package
│   ├── controller.py               # Simulated controller code
│   ├── sensor.py                   # Simulated sensor code
│   └── hardware.py                 # Hardware abstraction
├── tests/                          # Well-separated tests
│   ├── unit/                       # Pure logic tests
│   │   └── test_speed_calculator.py
│   ├── integration/                # Multiple modules interacting
│   │   └── test_controller_with_sensor.py
│   ├── simulation/                 # Sim-based environments
│   │   └── test_simulated_environment.py
│   ├── hardware/                   # Real robot/hardware tests
│   │   └── test_real_motor.py
│   └── conftest.py                # Shared fixtures/mocks
├── requirements.txt               # List of dependencies (pytest, pytest-cov, etc.)
├── .github/
│   └── workflows/
│       └── python-tests.yml       # GitHub Actions config
├── pytest.ini                     # Pytest markers and settings
└── README.md                      # Project overview
```

## Contributions

Feel free to open issues or submit PRs if you'd like to contribute or add new tests.