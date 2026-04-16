Concepts
========

This is a work in progress!

The concepts documentation covers the fundamental ideas and principles behind JSBSim, such as the structure of aircraft models, the physics of flight simulation, and the design of the API. 
It will also include explanations of key concepts such as frames of reference, coordinate systems, and units of measurement.

Simulation
----------

While the JSBSim user does not need to know some of the finer details of the flight simulator operation, it can be helpful to understand basically how JSBSim works. Some of the most important concepts are described in this section.

- Frames of reference are used to describe the placement and location of various items in a vehicle model.

- There is flexibility in how the units of measure can be specified when defining a vehicle model – both English and metric units are supported.

- The use of "Properties" permits JSBSim to be a generic simulator, providing a way to interface the various systems with parameters (or variables). Properties are used throughout the configuration files that describe aircraft and engine characteristics.

- Obviously, math plays a big part in modeling flight physics. JSBSim makes use of data tables, as flight dynamics characteristics are often stored in tables. Arbitrary algebraic functions can also be set up in JSBSim, allowing broad freedom for describing aerodynamic and flight control characteristics.

- Users have to have, at least a basic knowledge, of conventional forces and moments acting on an airplane in flight.

- The understanding of flight controls and of how system modelling can be achieved in JSBSim are the keys for successful and effective simulations.

.. toctree::
   :maxdepth: 1

   frames_of_reference
   units
   properties
   math

Forces and moments
--------
TBD.

Flight Control and System Modelling
--------
TBD.