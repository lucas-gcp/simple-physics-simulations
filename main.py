#main.py will be the pygame menu to select (through GUI) the requested simulation
import gravityevent

simulationlist = ["gravity", "collisions"]
print(simulationlist)

indexSimulation = input("Which simulation to start? ").lower()

#if user wants to evoke gravity simulation:
if indexSimulation == "gravity":
    gravityevent.gravity_run()
else:
    print('No simulation with this name')