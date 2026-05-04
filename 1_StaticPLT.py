'''
Disclaimer: This script is provided "as is", without any warranties, expressed or implied.
It is intended to support learning and demonstration of concepts. 
it is not a substitute for engineering judgment or professional verification.
The author assumes no liability for any errors, omissions, or consequences arising from the use of this script.
Users must independently verify all results before applying them in analysis, design, or decision-making processes.
'''

# Script for creating a Pile Load Test Model

from plxscripting.easy import *
import matplotlib.pyplot as plt

# Getting PLAXIS scripting server and global objects
# Modify Port Numbers and Passwords as entered for RSS configuration
s_i, g_i = new_server("localhost", 10000, password = "mypassword")
s_o, g_o = new_server("localhost", 10001, password = "mypassword")

# Creating a new project
s_i.new()

# Setting PLAXIS project settings and units
g_i.setproperties("Title", "Static Pile Load Test Simulation",
                        "Company", "",
                        "Comments", "",
                        "UnitForce", "kN",
                        "UnitLength", "m",
                        "UnitTime", "day",
                        "WaterWeight", 10,
                        "ModelType", "axisymmetry",
                        "ElementType", "15-Noded")

# Setting up soil profile and material properties
g_i.SoilContour.initializerectangular(0, -40, 15, 0)

# Creating Soil materials
g_i.soilmat("Identification", "Sand",
                "SoilModel", "Mohr-Coulomb",
                "Colour", 8638971,
                "gammaSat", 19,
                "gammaUnsat", 17,
                "ERef", 15000,
                "nu", 0.28,
                "cRef", 5,
                "phi", 30)
                
g_i.soilmat("Identification", "Pile",
                "SoilModel", "Linear Elastic",
                "Colour", 8750469,
                "DrainageType", "Non-porous",
                "gammaUnsat", 25,
                "ERef", 40000000,
                "nu", 0.2) 

# Creating borehole and soil layer
g_i.borehole(0)
g_i.soillayer(0)
g_i.Soillayer_1.Zones[0].Top.set(0)
g_i.Soillayer_1.Zones[0].Bottom.set(-40)
g_i.Borehole_1.Head.set(-40)
g_i.Soillayer_1.Soil.Material.set(g_i.Sand)

g_i.gotostructures()
g_i.polygon((0,0), (0.5,0), (0.5,-20), (0,-20))
g_i.lineload((0,0), (0.5,0))
g_i.neginterface((0.5,-20), (0.5,0))

# Generating FE mesh with local refinement for the pile
g_i.gotomesh()
g_i.BoreholePolygon_1_Polygon_1_1.CoarsenessFactor.set(0.75)
g_i.mesh(0.06)
g_i.selectmeshpoints()
g_o.addcurvepoint("node", (0.25,0))
g_o.update()

# Defining construction staging
# Creating a new phase after Initial Phase
# Using for loop to create pile loading and unloading stages
load_dist = [0, -636, -1272, -1909, -2545, -3181, -3818,
                  -4454, -5090, -3818, -2545, -1272, 0]

stages = ["Loadingstage_0", "Loadingstage_1", "Loadingstage_2", "Loadingstage_3", "Loadingstage_4",
               "Loadingstage_5", "Loadingstage_6", "Loadingstage_7", "Loadingstage_8", "Unloadingstage_1", 
               "Unloadingstage_2", "Unloadingstage_3", "Unloadingstage_4"]
             
g_i.gotostages()
g_i.phase(g_i.InitialPhase)
g_i.setcurrentphase(g_i.Phase_1)
g_i.Phase_1.Identification.set("Pile Installation")
g_i.Phase_1.DeformCalcType.set("Plastic")
g_i.Soil_1_Soil_2_1.Material.set(g_i.Phase_1, g_i.Pile)
g_i.Line_2_1.activate(g_i.Phase_1)

for stage in stages:
    g_i.phase(g_i.Phases[-1])
    g_i.setcurrentphase(g_i.Phases[-1])
    g_i.Phases[-1].Identification.set(stage)
    g_i.Line_1_1.activate(g_i.Phases[-1])
    g_i.LineLoad_1_1.qy_start.set(g_i.Phases[-1], load_dist[stages.index(stage)])

# Marking all phases for calculation and running the calculation
g_i.Phase_2.Deform.ResetDisplacementsToZero.set(True)
g_i.apply(g_i.Phases, "setproperties", "ShouldCalculate", True)
g_i.calculate()
g_i.view(g_i.Phases[-1])

# Plotting Vertical  displacement contours and exporting the plot to file
g_o.Plot_1.ResultType.set(g_o.ResultTypes.Soil.Uy)
g_o.Plot_1.PlotType.set("shadings")
g_o.Plot_1.setproperties(
    "DrawFrame", True,
    "DrawProjectDirectory", True,
    "DrawTitle", True,
    "DrawLegend", True,
    "DrawRulers", True,
    "DrawAxes", True,
    "DrawLogo", True,
    "ProjectDescription", "Static Pile Load Test")

g_o.Plot_1.export(r"E:\PLAXIS2D\staticPLT_VerticalDisplacement.png")

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
    "ProjectDescription", "Static Pile Load Test")

g_o.Plot_1.export(r"E:\PLAXIS2D\PLT_PlasticPoints.png")

# Creating Pile head displacement curve and saving to file
load_positive = [-x for x in load_dist]
ydisp = [g_o.getsingleresult(phase, g_o.ResultTypes.Soil.Uy, g_o.CN_1,True) for phase in g_o.Phases]
plt.plot(load_positive, ydisp[2:])
plt.title("StaticPLT Pile Head Displacement")
plt.xlabel("Load (kPa)")
plt.ylabel("Pile Head Displacement (m)")
plt.grid()
plt.savefig(r"E:\PLAXIS2D\Pilehead_displacement.png")
plt.show()

g_o.close()