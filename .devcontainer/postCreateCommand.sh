#!/usr/bin/env bash
set -euo pipefail

pip install --upgrade pip

pip install -r requirements/codespaces.txt

python -m ipykernel install --user --name jsbsim-python-examples --display-name "JSBSim Python Examples"
