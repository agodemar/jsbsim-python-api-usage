# JSBSim Python Examples

A collection of Jupyter notebooks showcasing examples of the [JSBSim](https://github.com/JSBSim-Team/jsbsim) Python API, including integration with [PathSim](https://github.com/pathsim/pathsim), [PathView](https://view.pathsim.org/), and [pathsim-flight](https://github.com/pathsim/pathsim-flight).

The repository also hosts a [Sphinx](https://www.sphinx-doc.org/)-based static documentation site that is automatically built and deployed to GitHub Pages on every push.

See the [notebooks/README.md](notebooks/README.md) for a list of notebooks (work in progress).

## Documentation

The rendered documentation is automatically published to GitHub Pages:
**https://agodemar.github.io/jsbsim-python-examples/**

## GitHub Codespaces

The easiest way to get started is with [GitHub Codespaces](https://github.com/features/codespaces).
Click the button below to open the repository in a ready-to-use cloud environment with Python 3.11, JupyterLab, JSBSim, and PathSim already installed:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/agodemar/jsbsim-python-examples)

Once in Codespaces, wait for the environments to initialize.
Actually you have to wait for `postCreateCommand.sh` to complete its task before starting any interaction with the system. Watch the terminal.

Codespace provides an instance of [VS Code](https://code.visualstudio.com/) working in the browser with all the extensions you needed to render and run the Jupyter notebooks within the editor.
So, Just wait that the environement fully comes alive then with VS Code browse through the notebooks in the `notebooks/` folder, and run them.

## Setting up the Conda Environment

All examples can be run inside a dedicated [conda](https://docs.conda.io/) environment.

### Prerequisites

Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) if you have not done so already.

### Create the environment

```bash
conda env create -f environment.yml
```

This creates an environment called **`jsbsim-python-examples`** with all required packages.

### Activate the environment

```bash
conda activate jsbsim-python-examples
```

### Launch JupyterLab

```bash
jupyter lab
```

Then open any notebook from the `notebooks/` folder.

### Update the environment

If `environment.yml` changes after you have already created the environment, update it with:

```bash
conda env update -f environment.yml --prune
```

### Remove the environment

```bash
conda deactivate
conda env remove -n jsbsim-python-examples
```

## Updating the JSBSim Python API to the latest GitHub snapshot

> **Tested environment:** This procedure has been verified in a
> [GitHub Codespaces](https://github.com/features/codespaces) instance of this
> repository (Python 3.11, Debian Trixie, April 2026). Results may vary in
> other environments.

The conda environment installs the **stable JSBSim release** from PyPI.
If you need the very latest development code straight from the
[JSBSim-Team/jsbsim](https://github.com/JSBSim-Team/jsbsim) repository,
use the helper script provided at the repository root:

```bash
./update_jsbsim_from_github.sh
```

By default the script targets `/usr/local/bin/python` (the interpreter used
by the Jupyter kernel in Codespaces). To point it at a different interpreter,
set the `PYTHON` environment variable:

```bash
PYTHON=$(conda run -n jsbsim-python-examples which python) \
    ./update_jsbsim_from_github.sh
```

### What the script does

| Step | Action |
|------|--------|
| 1 | Clones `JSBSim-Team/jsbsim` into `/tmp/jsbsim_build` (shallow clone). On subsequent runs it fast-forwards to the latest `HEAD` instead of re-cloning. |
| 2 | Generates `pyproject.toml` from the CMake template in the repository, embedding the current version string. |
| 3 | Ensures the `python/__init__.pyi` type-stub required by the CMake install step is present, copying it from an existing installation if available. |
| 4 | Runs `pip install --user --upgrade` to build the Cython extension with CMake/scikit-build-core and install the resulting wheel. |

After a successful run the script prints the installed version and the exact
Git commit hash so you always know what you are running:

```
=== Installed package ===
  JSBSim version : 1.3.1.dev1
  Module path    : /home/vscode/.local/lib/python3.11/site-packages/jsbsim/__init__.py
  Git commit     : 027c1414  (2026-04-15 08:08:48 +0200)
```

> **Note:** The script performs a C++ compilation step (Cython → shared
> library). On a standard Codespace it takes roughly 2–3 minutes. The clone is
> reused on subsequent runs so only changed source files are recompiled.

## Building the documentation locally

```bash
conda activate jsbsim-python-examples

# Run all notebooks (optional – re-executes and saves outputs in-place)
jupyter nbconvert --to notebook --execute --inplace notebooks/*.ipynb

# Build HTML docs
cd docs
make html

# Open the result
open _build/html/index.html   # macOS
xdg-open _build/html/index.html  # Linux
```

## Project structure

```
jsbsim-python-examples/
├── .devcontainer/           # GitHub Codespaces / Dev Container configuration
│   ├── devcontainer.json
│   └── postCreateCommand.sh
├── environment.yml          # Conda environment definition
├── notebooks/               # Jupyter notebooks
│   ├── 01_jsbsim_hello_world.ipynb
│   ├── 02_jsbsim_flight_simulation.ipynb
│   ├── 03_pathsim_intro.ipynb
│   ├── 04_pathsim_jsbsim_trim_elevator_doublet.ipynb
│   ├── 05_pathsim_flight.ipynb
│   ├── 06_aoa_vs_cas.ipynb
│   ├── 07_rudder_kick.ipynb
│   ├── 08_thrust_vectoring_analysis.ipynb
│   ├── 09_trim_envelope.ipynb
│   └── 10_trim_envelope_climb.ipynb
└── docs/                    # Sphinx documentation source
    ├── conf.py
    ├── index.rst
    ├── notebooks.rst
    └── Makefile
```

## Related projects

- [JSBSim](https://github.com/JSBSim-Team/jsbsim) – Open-source flight dynamics model
- [PathSim](https://github.com/pathsim/pathsim) – Block-based time-domain simulation framework
- [PathView](https://view.pathsim.org/) – Graphical editor for PathSim
- [pathsim-flight](https://github.com/pathsim/pathsim-flight) – Flight-dynamics blocks for PathSim

## License

This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.
