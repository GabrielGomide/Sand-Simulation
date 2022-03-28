# Sand Simulation

The falling-sand algorithm is pretty simple:
<br>
1 - If there's not sand below the sand cell, the sand cell falls directly down.
<br>
2 - If there's sand below the sand cell, the sand looks at the diagonals, if they are both empty it chooses one randomly, if only one diagonal is empty is goes to that diagonal, if none of the diagonals are empty, the sand cell stops moving.


![Screenshot of the simulation](https://github.com/GabrielGomide/Sand-Simulation/blob/master/sand_simulation.png)

