# JSBSim Python API Usage

A collection of Jupyter notebooks showcasing examples of the [JSBSim](https://github.com/JSBSim-Team/jsbsim) Python API, including integration with [PathSim](https://github.com/pathsim/pathsim), [PathView](https://view.pathsim.org/), and [pathsim-flight](https://github.com/pathsim/pathsim-flight).

The repository also hosts a [Sphinx](https://www.sphinx-doc.org/)-based static documentation site that is automatically built and deployed to GitHub Pages on every push.

## Overview

| Notebook | Description |
|----------|-------------|
| [01 – JSBSim Hello World](notebooks/01_jsbsim_hello_world.ipynb) | Loading an aircraft model, initialising initial conditions, stepping the simulation, and reading JSBSim properties. |
| [02 – JSBSim Flight Simulation](notebooks/02_jsbsim_flight_simulation.ipynb) | A longer trimmed flight simulation with time-history plots of altitude, airspeed, and attitude. |
| [03 – PathSim Introduction](notebooks/03_pathsim_intro.ipynb) | Block-diagram modelling with PathSim: sources, integrators, amplifiers, adders, and scopes. |
| [04 – JSBSim Trim & Elevator Doublet](notebooks/04_pathsim_jsbsim_trim_elevator_doublet.ipynb) | Trimming a JSBSim FDM and applying a doublet elevator input using a PathSim `DynamicalFunction` block. |
| [05 – pathsim-flight Integration](notebooks/05_pathsim_flight.ipynb) | Using `pathsim-flight`'s `JSBSimWrapper` to embed JSBSim as a PathSim block, and the `ISAtmosphere` utility. |

## Documentation

The rendered documentation is automatically published to GitHub Pages:
**https://agodemar.github.io/jsbsim-python-api-usage/**

## Setting up the Conda Environment

All examples can be run inside a dedicated [conda](https://docs.conda.io/) environment.

### Prerequisites

Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) if you have not done so already.

### Create the environment

```bash
conda env create -f environment.yml
```

This creates an environment called **`jsbsim-api`** with all required packages.

### Activate the environment

```bash
conda activate jsbsim-api
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
conda env remove -n jsbsim-api
```

## Building the documentation locally

```bash
conda activate jsbsim-api

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
jsbsim-python-api-usage/
├── environment.yml          # Conda environment definition
├── notebooks/               # Jupyter notebooks
│   ├── 01_jsbsim_hello_world.ipynb
│   ├── 02_jsbsim_flight_simulation.ipynb
│   ├── 03_pathsim_intro.ipynb
│   ├── 04_pathsim_jsbsim_trim_elevator_doublet.ipynb
│   └── 05_pathsim_flight.ipynb
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
