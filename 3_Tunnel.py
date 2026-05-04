'''
Disclaimer: This script is provided "as is", without any warranties, expressed or implied.
It is intended to support learning and demonstration of concepts. 
it is not a substitute for engineering judgment or professional verification.
The author assumes no liability for any errors, omissions, or consequences arising from the use of this script.
Users must independently verify all results before applying them in analysis, design, or decision-making processes.
'''

# Script for creating a simple Tunnel Model 

from plxscripting.easy import *
import matplotlib.pyplot as plt

# Getting PLAXIS scripting server and global objects
# Modify Port Numbers and Passwords as entered for RSS configuration
s_i, g_i = new_server("localhost", 10000, password = "mypassword")
s_o, g_o = new_server("localhost", 10001, password = "mypassword")

# Creating a new project
s_i.new()

# Setting PLAXIS project settings and units
g_i.setproperties("Title", "Tunnel Support Design",
                        "Company", "",
                        "Comments", "",
                        "UnitForce", "kN",
                        "UnitLength", "m",
                        "UnitTime", "day",
                        "WaterWeight", 10,
                        "ModelType", "Plane strain",
                        "ElementType", "15-Noded")

# Setting up soil profile and material properties
g_i.SoilContour.initializerectangular(-70, -60, 70, 70)

# Creating Soil material
g_i.soilmat("Identification", "Rock",
                "SoilModel", "Hoek-Brown",
                "Colour", 8638971,
                "gammaSat", 27,
                "gammaUnsat", 26,
                "Erm", 750000,
                "nu", 0.25,
                "AbsSigmaCI", 20000,
                "HoekBrownParameterDetermination", "Derived",
                "mi", 12,
                "GSI", 25,
                "Disturbance", 0,
                "psiMax", 2) 

# Creating borehole and soil layer
g_i.borehole(0)
g_i.soillayer(0)
g_i.Soillayer_1.Zones[0].Top.set(70)
g_i.Soillayer_1.Zones[0].Bottom.set(-60)
g_i.Borehole_1.Head.set(-60)
g_i.Soillayer_1.Soil.Material.set(g_i.Rock)

# Creating plate material for shotcrete shell
g_i.platemat("Identification", "Shotcrete",
                  "MaterialType", "Elastic",
                  "Colour", 16716032,
                  "w", 6,
                  "EA1", 6250000,
                  "EI", 32000,
                  "StructNu", 0.2)
                  
# Creating embedded beam material for rock bolts
g_i.embeddedbeammat("Identification", "Rockbolt",
                                   "MaterialType", "Elastic",
                                   "Colour", 16716032,
                                   "Gamma", 77,
                                   "LSpacing", 1.3,
                                   "CrossSectionType", "Predefined",
                                   "PredefinedCrossSectionType", "Solid circular beam",
                                   "Diameter", 0.032,
                                   "E", 210000000,
                                   "AxialSkinResistance", "Linear",
                                   "TSkinStartMax", 100,
                                   "TSkinEndMax", 100)

# Generating tunnel geometry through PLAXIS Tunnel Designer
g_i.gotostructures()
g_i.tunnel(0,0)
g_i.Tunnels[-1].CrossSection.ShapeType.set("Free")
g_i.Tunnels[-1].CrossSection.WholeHalfMode.set("Whole")
g_i.Tunnels[-1].CrossSection.add("arc", 0, 21.3, 12)
g_i.Tunnels[-1].CrossSection.add("arc", 33.6, 35.1, 9)
g_i.Tunnels[-1].CrossSection.add("arc", 0, 20, 6)
g_i.Tunnels[-1].CrossSection.extendtosymmetryaxis()
g_i.Tunnels[-1].CrossSection.symmetricclose()

# Creating Plate elements for tunnel slice segments
# Assigning relevant plate material to the created plates
segments = [seg for seg in g_i.Tunnel_1.SliceSegments]
g_i.plate(segments)
g_i.neginterface(segments)
for seg in segments:
        seg.Plate.Material.set(g_i.Shotcrete)

# Creating rock bolts around tunnel periphery at specified spacing
g_i.reinforcement(g_i.Tunnels[-1].SliceSegments[0:6])
chain = g_i.Tunnels[-1].SlicePolycurveChains[-1].Reinforcements
chain.FirstPart.ElementType.set("Rockbolt")
chain.FirstPart.Length.set(8)
chain.FirstPart.RockBoltProperties.Material.set(g_i.Rockbolt)
chain.Breadth.DistributionMethod.set("Spacing")
chain.Breadth.Spacing.set(1.3)

# Generating Tunnel in PLAXIS Model
g_i.generatetunnel(g_i.Tunnels[-1])

#Creating box around tunnel for mesh refinement
g_i.line((-20,-14), (20,-14), (20,26), (-20,26), (-20,-14))

# Generating FE mesh with local refinement around the tunnel
g_i.gotomesh()
g_i.BoreholePolygon_1_1.CoarsenessFactor.set(0.2)
g_i.BoreholePolygon_1_2.CoarsenessFactor.set(0.2)
g_i.mesh(0.06)

# Defining model conditions for the Initial Phase
g_i.gotostages()
g_i.InitialPhase.DeformCalcType.set("Field stress")
g_i.Deformations.BoundaryXMin.set(g_i.InitialPhase, "Normally Fixed")
g_i.Deformations.BoundaryYMin.set(g_i.InitialPhase, "Normally Fixed")
g_i.Deformations.BoundaryXMax.set(g_i.InitialPhase, "Normally Fixed")
g_i.Deformations.BoundaryYMax.set(g_i.InitialPhase, "Normally Fixed")
 
# Specifying Field Stress for Initial Phase
g_i.FieldStress.sig1.set(g_i.InitialPhase, -3120)
g_i.FieldStress.sig2.set(g_i.InitialPhase, -4056)
g_i.FieldStress.sig3.set(g_i.InitialPhase, -4056)

# Creating a new phase after Initial Phase
# Excavating the tunnel in Phase_1 and installing support elements
g_i.phase(g_i.InitialPhase)
g_i.setcurrentphase(g_i.Phase_1)
g_i.Phase_1.Identification.set("Tunnel Excavation and Support")
g_i.Phase_1.DeformCalcType.set("Plastic")
g_i.BoreholePolygon_1_2.deactivate(g_i.Phase_1)
g_i.Plates.activate(g_i.Phase_1)
g_i.EmbeddedBeams.activate(g_i.Phase_1)
g_i.Interfaces.activate(g_i.Phase_1)

# Selecting mesh points for plotting curves
g_i.gotomesh()
g_i.selectmeshpoints()
g_o.addcurvepoint("node", (0,12))
g_o.addcurvepoint("node", (6,6.23))
g_o.update()

# Marking phases for calculation
g_i.gotostages()
g_i.InitialPhase.ShouldCalculate.set(True)
g_i.Phase_1.ShouldCalculate.set(True)

# Saving the project
# Path should be modified to ensure that specified folders already exist
g_i.save(r"E:\PLAXIS2D\Tunnel.p2dx")

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
    "ProjectDescription", "Tunnel Excavation Stability")

g_o.Plot_1.export(r"E:\PLAXIS2D\tunnel_Totaldeformation.png")

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
    "ProjectDescription", "Tunnel Excavation Stability")

g_o.Plot_1.export(r"E:\PLAXIS2D\tunnel_PlasticPoints.png")

# Creating crown and wall displacement curves and saving to file
loadsteps = [step.ID.value for step in g_o.Steps]
disp_c = g_o.getcurveresultspath(g_o.CN_1, g_o.InitialPhase, g_o.Phase_1.Steps[-1], g_o.ResultTypes.Soil.Utot)
plt.plot(loadsteps, disp_c)
plt.title("Tunnel Crown Deformation")
plt.xlabel("Load Steps")
plt.ylabel("Crown Displacement (m)")
plt.grid()
plt.savefig(r"E:\PLAXIS2D\tunnel_crowndisp.png")
plt.show()

disp_w = g_o.getcurveresultspath(g_o.CN_2, g_o.InitialPhase, g_o.Phase_1.Steps[-1], g_o.ResultTypes.Soil.Utot)
plt.clf()
plt.plot(loadsteps, disp_w)
plt.title("Tunnel Wall Deformation")
plt.xlabel("Load Steps")
plt.ylabel("Wall Displacement (m)")
plt.grid()
plt.savefig(r"E:\PLAXIS2D\tunnel_walldisp.png")
plt.show()

g_o.close()