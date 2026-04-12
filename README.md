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
