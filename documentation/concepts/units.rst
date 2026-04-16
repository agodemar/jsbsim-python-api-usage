Units
=====

JSBSim uses English units for internal calculations almost exclusively. However, it is possible
to input some parameters in the configuration file using different units. In fact, to avoid
confusion, it is recommended that the unit always be specified. Units are specified using the
``unit`` attribute. For instance, the specification for the wingspan looks like this:

.. code-block:: xml

   <wingspan unit="FT"> 35.8 </wingspan>

The above statement specifies a wingspan of 35.8 feet. The following statement specifying the
wingspan in meters would result in the wingspan being converted to 35.8 feet as it was read in:

.. code-block:: xml

   <wingspan unit="M"> 10.91 </wingspan>

The two statements for wingspan are effectively equivalent.

The following units are currently supported in JSBSim:

**Length**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``FT``
     - ft
   * - ``IN``
     - in
   * - ``M``
     - m
   * - ``KM``
     - km

**Area**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``M2``
     - m²
   * - ``FT2``
     - ft²

**Volume**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``FT3``
     - ft³
   * - ``CC``
     - cm³
   * - ``M3``
     - m³
   * - ``LTR``
     - l

**Mass and Weight**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``LBS``
     - lbm
   * - ``KG``
     - kg

**Moments of Inertia**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``SLUG*FT2``
     - slug ft²
   * - ``KG*M2``
     - kg m²

**Angles**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``RAD``
     - rad
   * - ``DEG``
     - deg

**Spring Force**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``N/M``
     - N/m
   * - ``LBS/FT``
     - lb/ft

**Damping Force**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``N/M/SEC``
     - N/(m s)
   * - ``LBS/FT/SEC``
     - lb/(ft s)

**Power**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``WATTS``
     - W
   * - ``HP``
     - Hp

**Force**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``LBS``
     - lb
   * - ``N``
     - N

**Velocity**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``KTS``
     - kts
   * - ``FT/SEC``
     - ft/s
   * - ``M/S``
     - m/s

**Torque**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``N*M``
     - N m
   * - ``FT*LBS``
     - lb ft

**Pressure**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - ``unit=``
     - unit
   * - ``PSF``
     - lb/ft²
   * - ``PSI``
     - lb/in²
   * - ``ATM``
     - atm
   * - ``PA``
     - N/m²
   * - ``INHG``
     - in HG
