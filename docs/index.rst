.. Little helper documentation master file, created by
   sphinx-quickstart on Thu Jan 12 12:18:52 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Little helper's documentation!
=========================================

In the context of our final year project, we are working on an autonomous vehicle.
Our project is to build a car that will be able to autonomously transport food in a closed or quiet environment,
such as a hospital or a retirement home.
The hospital staff will have choices between different preloaded paths between the hospital kitchen and
the other buildings in the area, and the car will avoid collisions and going off the road.

You will find here the complete documentation of the code for the Raspberry pi part.


The code is divide in two main folder model_ and controllers_.
At the end of this page you will also find a classdiagram_ and a diagram of all threads_ used.

.. _model:

Model
-----

The model folder contains all the module usefull to represent the environment of the project.

.. toctree::
   :maxdepth: 3

   model

.. _controllers:

Controllers
-----------

The controllers folder contains all the module usefull to control the car.

.. toctree::
  :maxdepth: 3

  controllers


Diagramm
---------

.. _classdiagram:

Class diagram
_____________

.. image:: diagram.png
   :align: center

.. _threads:

Thread diagram
______________

.. image:: threads.png
    :align: center


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
