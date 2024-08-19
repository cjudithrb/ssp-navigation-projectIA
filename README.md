# SSP Navigation Project

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## 🚀 Overview

The SSP Navigation Project is an implementation focused on developing and testing advanced navigation algorithms using sensor data fusion and intelligent pathfinding. This project aims to enhance autonomous systems' capabilities in navigating complex environments.

## 🛠️ Features

- **Sensor Data Integration:** Seamlessly integrates data from multiple sensors for accurate navigation.
- **Pathfinding Algorithms:** Implements and tests various algorithms for efficient route planning.
- **Environment Simulation:** Simulates different environmental conditions to evaluate the robustness of the navigation system.

## 📦 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/cjudithrb/ssp-navigation-projectIA.git
    cd ssp-navigation-projectIA
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## 🚶‍♂️ Usage

To run the navigation algorithms: ``` bash python src/main.py --config=config.yaml

## 📁 Project Structure 

```plaintext
ssp-navigation-projectIA/
│
├── src/                    # Source code for navigation algorithms
│   ├── data/               # Sensor data handling
│   ├── algorithms/         # Pathfinding algorithms implementations
│   └── utils/              # Utility scripts and helpers
│
├── tests/                  # Unit and integration tests
│   ├── data_tests/         # Tests for data processing
│   ├── algorithm_tests/    # Tests for pathfinding algorithms
│   └── utils_tests/        # Tests for utility functions
│
├── docs/                   # Documentation and resources
│   ├── api/                # API documentation
│   └── usage/              # Usage guidelines and examples
│
└── README.md               # Project overview and instructions
