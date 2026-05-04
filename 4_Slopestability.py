'''
Disclaimer: This script is provided "as is", without any warranties, expressed or implied.
It is intended to support learning and demonstration of concepts. 
it is not a substitute for engineering judgment or professional verification.
The author assumes no liability for any errors, omissions, or consequences arising from the use of this script.
Users must independently verify all results before applying them in analysis, design, or decision-making processes.
'''

# Script for creating a Slope Stability Model

from plxscripting.easy import *
import matplotlib.pyplot as plt

# Getting PLAXIS scripting server and global objects
# Modify Port Numbers and Passwords as entered for RSS configuration
s_i, g_i = new_server("localhost", 10000, password = "mypassword")
s_o, g_o = new_server("localhost", 10001, password = "mypassword")

# Creating a new project
s_i.new()

# Setting PLAXIS project settings and units
g_i.setproperties("Title", "Slope Stability Analysis",
                        "Company", "",
                        "Comments", "",
                        "UnitForce", "kN",
                        "UnitLength", "m",
                        "UnitTime", "day",
                        "WaterWeight", 10,
                        "ModelType", "Plane strain",
                        "ElementType", "15-Noded")

# Setting up soil profile and material properties
g_i.SoilContour.initializerectangular(0, 0, 125.5, 100)

# Creating Soil materials
g_i.soilmat("Identification", "Rock",
                "SoilModel", "Hoek-Brown",
                "Colour", 8638971,
                "gammaSat", 27,
                "gammaUnsat", 26,
                "Erm", 1500000,
                "nu", 0.25,
                "AbsSigmaCI", 35000,
                "HoekBrownParameterDetermination", "Derived",
                "mi", 12,
                "GSI", 35,
                "Disturbance", 0,
                "psiMax", 2)

g_i.gotostructures()
g_i.polygon((0,0), (125.5,0), (125.5,100), (75.5,100), (73,90),
                  (70,90), (67.5,80), (64.5,80), (62,70), (59,70),
                  (56.5,60), (53.5,60), (51,50), (48,50), (45.5,40),
                  (42.5,40), (40,30), (0,30), (0,0))

g_i.Polygon_1.Soil.Material.set(g_i.Rock)

# Generating FE mesh
g_i.gotomesh()
g_i.mesh(0.06)

# Defining model conditions for the Initial Phase
g_i.gotostages()
g_i.InitialPhase.DeformCalcType.set("Gravity loading")
g_i.Polygon_1_1.activate(g_i.InitialPhase)

# Creating a new phase after Initial Phase
g_i.phase(g_i.InitialPhase)
g_i.setcurrentphase(g_i.Phase_1)
g_i.Phase_1.Identification.set("Slope Stability")
g_i.Phase_1.DeformCalcType.set("Safety")

# Marking phases for calculation
g_i.apply(g_i.Phases, "setproperties", "ShouldCalculate", True)

# Saving the project
# Path should be modified to ensure that specified folders already exist
g_i.save(r"E:\PLAXIS2D\SlopeStability.p2dx")

# Calculating and open PLAXIS Output to view results
g_i.calculate()
g_i.view(g_i.Phase_1)

# Plotting Total displacement contours and exporting the plot to file
g_o.Plot_1.ResultType.set(g_o.ResultTypes.Soil.Utot)
g_o.Plot_1.PlotType.set("shadings")
g_o.Plot_1.setproperties(
    "DrawFrame", True,
    "DrawProjectDirectory", True,
    "DrawTitle", True,
    "DrawLegend", True,
    "DrawRulers", True,
    "DrawAxes", True,
    "DrawLogo", True,
    "ProjectDescription", "Slope Stability Failure Plane")

g_o.Plot_1.export(r"E:\PLAXIS2D\SlopeStability_Failureplane.png")

#Plotting Plastic Points and exporting the plot to file
g_o.Plot_1.ResultType.set(g_o.ResultTypes.Soil.PlasticPoint)
g_o.Plot_1.PlotType.set("PlasticPoints")
g_o.Plot_1.setproperties(
    "DrawFrame", True,
    "DrawProjectDirectory", True,
    "DrawTitle", True,
    "DrawLegend", True,
    "DrawRulers", True,
    "DrawAxes", True,
    "DrawLogo", True,
    "ProjectDescription", "Slope Stability Plastic Points")

g_o.Plot_1.export(r"E:\PLAXIS2D\Slopestability_PlasticPoints.png")

# Creating FoS curve and saving to file
loadsteps = [step.ID.value for step in g_o.Steps]
fos = [step.Reached.SumMsf.value for step in g_o.Steps]
plt.plot(loadsteps, fos)
plt.title("Factor of Safety with Strength Reduction Method")
plt.xlabel("Load Steps")
plt.ylabel("Factor of Safety")
plt.grid()
plt.savefig(r"E:\PLAXIS2D\SlopeStability_FoS.png")
plt.show()

g_o.close()