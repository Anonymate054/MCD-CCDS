# Data Science Project Template

This repository aims to provide a template for data science projects, inspired by [cookiecutter-conda-data-science](https://github.com/jvelezmagic/cookiecutter-conda-data-science/tree/main) and [cookiecutter-data-science](https://github.com/drivendataorg/cookiecutter-data-science).

## Overview

The goal of this template is to standardize the structure of data science projects, making it easier to manage, share, and collaborate on data analysis and machine learning projects. The template is generated using Python and Cookiecutter, ensuring consistency and reproducibility across different projects.

## Features

- Standardized project structure
- Environment management with Conda
- Pre-configured directories for data, notebooks, scripts, and results
- Easy-to-use setup with Cookiecutter

## Requirements

- [Anaconda](https://www.anaconda.com/download/) >= 4.x
- [git](https://git-scm.com/) >= 2.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
    This can be installed with `pip` or `conda` depending on how you manage your Python packages:

## Usage

To generate a new project using this template, you need to have Python, fs and Cookiecutter installed. You can install Cookiecutter using pip:

```bash
pip install cookiecutter
pip install fs
```

or

```bash
conda install -c conda-forge cookiecutter
conda install -c conda-forge fs
```

Then, generate a new project:
```bash
cookiecutter https://github.com/Anonymate054/MCD-CCDS.git
```

If the template is from a branch use:
```bash
cookiecutter https://github.com/Anonymate054/MCD-CCDS.git -c < branch >
```

Follow the prompts to customize your project.

# Contributing
We welcome contributions to improve this template. Please fork the repository and submit a pull request with your changes.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
