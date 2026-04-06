#!/usr/bin/env bash
set -euo pipefail

pip install --upgrade pip

pip install \
  "jupyterlab>=4.0" \
  "notebook>=7.0" \
  "nbconvert>=7.0" \
  "matplotlib>=3.7" \
  "numpy>=1.24" \
  "pandas>=2.0" \
  "scipy>=1.11" \
  "ipykernel" \
  "ipython" \
  "jsbsim>=1.2" \
  "pathsim>=0.20" \
  "git+https://github.com/pathsim/pathsim-flight.git"

python -m ipykernel install --user --name jsbsim-python-examples --display-name "JSBSim Python Examples"
