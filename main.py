#main.py will be the pygame menu to select (through GUI) the requested simulation
from gravitycalculations import Body

simulationlist = ["gravity", "collisions"]
print(simulationlist)

indexSimulation = input("Wich simulation to start? ")

#if user wants to evoke gravity simulation:
if indexSimulation == "gravity":
    with open("gravityevent.py", "r") as file:
        gravityEvent = file.read()
        exec(gravityEvent)

