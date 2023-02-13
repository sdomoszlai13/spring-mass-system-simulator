# Spring Mass System Simulation

This progam simulates a system of an arbitrary number of masses, fixtures and springs in a gravity field.

When the fixtures, masses and spings are set up, the forces acting on the masses are calculated. This in turn allows to calculate their velocity and position. These steps are repeated for every time step. At the end, a plausibility check is performed by looking at the conservation of energy. At the beginning and at the end of the process, the total energy of the system is calculated and the values are compared. The total energy of the system at a given point in time is the sum of the kinetic and potential energies of all the masses and the potential energy of the springs (we assume massless springs). Ideally, the total energy of the system should not change with time. At the end, the trajectories of the masses are plotted.

**V1.0:**
As of today, you can do the following in the program:

* set up an arbitrary number of fixtures, masses and springs
* run the simulation for a desired time with a desired number of time steps (temporary resolution)
* perform a plausibility check by looking at the conservation of energy (known bug: sometimes wrong final point in trajectory and therefore wrong final energy)
* plot the trajectories of the masses
* save the trajectories of the masses in a text file

