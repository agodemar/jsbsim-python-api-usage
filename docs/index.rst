.. JSBSim Python API Usage documentation master file

.. _index:

JSBSim Python API Usage
=======================

A collection of Jupyter notebooks showcasing examples of the `JSBSim`_ Python API,
including integration with `PathSim`_, `PathView`_, and `pathsim-flight`_.

.. _JSBSim: https://github.com/JSBSim-Team/jsbsim
.. _PathSim: https://github.com/pathsim/pathsim
.. _PathView: https://view.pathsim.org
.. _pathsim-flight: https://github.com/pathsim/pathsim-flight

.. toctree::
   :maxdepth: 2
   :caption: Notebooks

   notebooks

.. toctree::
   :maxdepth: 1
   :caption: Resources

   resources

Overview
--------

This repository acts as a side project to JSBSim and demonstrates real-world
usage of the JSBSim Python API through fully executable Jupyter notebooks.

The notebooks cover:

* **Basic API usage** – creating an FDM executor, loading aircraft models,
  setting initial conditions, trimming, and reading properties.
* **Flight simulation** – running trimmed flight, recording time histories,
  plotting altitude, airspeed, attitude, and ground track.
* **PathSim** – block-diagram simulation with integrators, amplifiers, adders,
  scopes, and custom function blocks.
* **pathsim-flight** – embedding JSBSim inside a PathSim block diagram,
  using the International Standard Atmosphere model, and building a
  simple pitch-hold autopilot.

Quick start
-----------

.. code-block:: bash

   # 1. Create and activate the conda environment
   conda env create -f environment.yml
   conda activate jsbsim-api

   # 2. Launch JupyterLab
   jupyter lab

Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`
