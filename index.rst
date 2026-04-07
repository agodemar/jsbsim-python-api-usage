.. JSBSim Python Examples documentation master file

.. _index:

Overview
========

.. image:: docs/_static/logo_jsbsim_globe.svg
   :width: 360px
   :align: center
   :alt: JSBSim logo

JSBSim is a lightweight, data-driven, non-linear, six-degree-of-freedom (6DoF), batch simulation application aimed at modeling flight dynamics and control for aircraft. 
Since the earliest versions, JSBSim has benefited from the open source development environment it has grown within and from the wide variety of users that have contributed ideas for its continued improvement.

The `JSBSim online reference manual`_ is a community effort to keep the users and developers up-to-date with all the functionalities of the software.
Yet the manual is not meant to be a tutorial or a user guide, and it does not include examples of how to use the software in practice.
This repository acts as a side project to JSBSim and demonstrates real-world usage of the `JSBSim`_ Python API through fully executable Jupyter notebooks.
Eventually the collection of notebooks will grow to cover a wide range of use cases, from basic API usage to advanced analysis and integration with other tools, 
and will be integrated into the online reference manual as a companion resource.

The notebooks in this repository are here to serve as an example-based user guide of `JSBSim`_ for Python users.
For instance, this documentation serves as a reference for how to use the API for common tasks such as loading aircraft models, setting initial conditions, running flight simulations, and analyzing results. 

The examples include demos of how JSBSim can be integrated with interesting Python libraries, such as `PathSim`_, and `pathsim-flight`_, and `PathView`_.

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


.. _JSBSim online reference manual: https://jsbsim-team.github.io/jsbsim-reference-manual/
.. _JSBSim: https://github.com/JSBSim-Team/jsbsim
.. _PathSim: https://github.com/pathsim/pathsim
.. _PathView: https://view.pathsim.org
.. _pathsim-flight: https://github.com/pathsim/pathsim-flight

.. toctree::
   :maxdepth: 1
   :caption: JSBSim Basics

   notebooks/01_jsbsim_hello_world
   notebooks/02_jsbsim_flight_simulation

.. toctree::
   :maxdepth: 1
   :caption: PathSim Integration

   notebooks/03_pathsim_intro
   notebooks/04_pathsim_jsbsim_trim_elevator_doublet
   notebooks/05_pathsim_flight

.. toctree::
   :maxdepth: 1
   :caption: Advanced Analysis

   notebooks/06_aoa_vs_cas
   notebooks/07_rudder_kick
   notebooks/08_thrust_vectoring_analysis
   notebooks/09_trim_envelope
   notebooks/10_trim_envelope_climb

.. toctree::
   :maxdepth: 1
   :caption: Resources

   resources

Quick start
-----------

.. code-block:: bash

   # 1. Create and activate the conda environment
   conda env create -f environment.yml
   conda activate jsbsim-python-examples

   # 2. Launch JupyterLab
   jupyter lab

Indices and tables
------------------

* :ref:`genindex`
* :ref:`search`
