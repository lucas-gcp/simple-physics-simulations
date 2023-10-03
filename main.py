#essa pagina sera um menu do pygame onde o user podera escolher qual simulacao ele deseja invocar
#se ele quiser invocar o evento da gravidade:
from gravitycalculations import Body

simulationlist = ["gravity", "collisions"]
print(simulationlist)

indexSimulation = input("Wich simulation to start? ")

if indexSimulation == "gravity":
    with open("gravityevent.py", "r") as file:
        gravityEvent = file.read()
        exec(gravityEvent)

