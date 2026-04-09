# JSBSim Python Examples

A collection of Jupyter notebooks showcasing examples of the [JSBSim](https://github.com/JSBSim-Team/jsbsim) Python API, including integration with [PathSim](https://github.com/pathsim/pathsim), [PathView](https://view.pathsim.org/), and [pathsim-flight](https://github.com/pathsim/pathsim-flight).

The repository also hosts a [Sphinx](https://www.sphinx-doc.org/)-based static documentation site that is automatically built and deployed to GitHub Pages on every push.

## Overview (Work in Progress)

| Notebook | Description |
|----------|-------------|
| [01 – JSBSim Hello World](notebooks/01_jsbsim_hello_world.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agodemar/jsbsim-python-examples/blob/main/notebooks/01_jsbsim_hello_world.ipynb) | Loading an aircraft model, initialising initial conditions, stepping the simulation, and reading JSBSim properties. |
| [02 – JSBSim Flight Simulation](notebooks/02_jsbsim_flight_simulation.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agodemar/jsbsim-python-examples/blob/main/notebooks/02_jsbsim_flight_simulation.ipynb) | A longer trimmed flight simulation with time-history plots of altitude, airspeed, and attitude. |
| [03 – PathSim Introduction](notebooks/03_pathsim_intro.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agodemar/jsbsim-python-examples/blob/main/notebooks/03_pathsim_intro.ipynb) | Block-diagram modelling with PathSim: sources, integrators, amplifiers, adders, and scopes. |
| [04 – JSBSim Trim & Elevator Doublet](notebooks/04_pathsim_jsbsim_trim_elevator_doublet.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agodemar/jsbsim-python-examples/blob/main/notebooks/04_pathsim_jsbsim_trim_elevator_doublet.ipynb) | Trimming a JSBSim FDM and applying a doublet elevator input using a PathSim `DynamicalFunction` block. |
| [05 – pathsim-flight Integration](notebooks/05_pathsim_flight.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agodemar/jsbsim-python-examples/blob/main/notebooks/05_pathsim_flight.ipynb) | Using `pathsim-flight`'s `JSBSimWrapper` to embed JSBSim as a PathSim block, and the `ISAtmosphere` utility. |
| [06 – AoA vs CAS](notebooks/06_aoa_vs_cas.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agodemar/jsbsim-python-examples/blob/main/notebooks/06_aoa_vs_cas.ipynb) | Trimmed angle-of-attack vs calibrated airspeed curves for a Bombardier Global 5000 over a range of altitudes and weights. |
| [07 – Rudder Kick](notebooks/07_rudder_kick.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agodemar/jsbsim-python-examples/blob/main/notebooks/07_rudder_kick.ipynb) | Simulating a pilot's rudder-kick test with a ramp rudder input and coordinated aileron, plotting sideslip angle time history. |
| [08 – Thrust Vectoring Analysis](notebooks/08_thrust_vectoring_analysis.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agodemar/jsbsim-python-examples/blob/main/notebooks/08_thrust_vectoring_analysis.ipynb) | Comparing the effect of varying the thrust-vector angle on fuel burn for cruise and climb conditions, following a NASA report. |
| [09 – Trim Envelope](notebooks/09_trim_envelope.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agodemar/jsbsim-python-examples/blob/main/notebooks/09_trim_envelope.ipynb) | Computing the trim envelope over a range of airspeeds and flight-path angles, visualising required thrust and AoA via a colour map. |
| [10 – Trim Envelope and Climb Analysis](notebooks/10_trim_envelope_climb.ipynb) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/agodemar/jsbsim-python-examples/blob/main/notebooks/10_trim_envelope_climb.ipynb) | Generating a trim envelope across a range of altitudes, analysing required throttle and elevator settings, and simulating a climb using both fixed and interpolated trim settings. |

## Documentation

The rendered documentation is automatically published to GitHub Pages:
**https://agodemar.github.io/jsbsim-python-examples/**

## GitHub Codespaces

The easiest way to get started is with [GitHub Codespaces](https://github.com/features/codespaces).
Click the button below to open the repository in a ready-to-use cloud environment with Python 3.11, JupyterLab, JSBSim, and PathSim already installed:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/agodemar/jsbsim-python-examples)

Once the Codespace is ready, launch JupyterLab from the terminal:

```bash
jupyter lab
```

Then open any notebook from the `notebooks/` folder.

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
