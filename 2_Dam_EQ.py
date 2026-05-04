'''
Disclaimer: This script is provided "as is", without any warranties, expressed or implied.
It is intended to support learning and demonstration of concepts. 
it is not a substitute for engineering judgment or professional verification.
The author assumes no liability for any errors, omissions, or consequences arising from the use of this script.
Users must independently verify all results before applying them in analysis, design, or decision-making processes.
'''

# Script for creating an Embankment Dam model under Seismic loading

from plxscripting.easy import *
import matplotlib.pyplot as plt

# Getting PLAXIS scripting server and global objects
# Modify Port Numbers and Passwords as entered for RSS configuration
s_i, g_i = new_server("localhost", 10000, password = "mypassword")
s_o, g_o = new_server("localhost", 10001, password = "mypassword")

# Creating a new project
s_i.new()

# Setting PLAXIS project settings and units
g_i.setproperties("Title", "Embankment Dam Seismic Loading",
                        "Company", "",
                        "Comments", "",
                        "UnitForce", "kN",
                        "UnitLength", "m",
                        "UnitTime", "day",
                        "WaterWeight", 10,
                        "ModelType", "Plane strain",
                        "ElementType", "15-Noded")

# Setting up soil profile and material properties
g_i.SoilContour.initializerectangular(-150, -70, 150, 50)

# Creating Soil materials
g_i.soilmat("Identification", "DamBody",
                "SoilModel", "Mohr-Coulomb",
                "Colour", 8638971,
                "gammaSat", 18,
                "gammaUnsat", 16,
                "ERef", 25000,
                "nu", 0.28,
                "cRef", 10,
                "phi", 33,
                "psi", 2,
                "GroundwaterClassificationType", "Hypres",
                "GroundwaterSoilClassStandard", "Coarse",
                "GwUseDefaults", False,
                "PermHorizontalPrimary", 1,
                "PermVertical", 1,
                "RayleighDampingInputMethod", "SDOF equivalent",
                "TargetDamping1", 1,
                "TargetFrequency1", 1,
                "TargetDamping2", 3,
                "TargetFrequency2", 5) 
                
g_i.soilmat("Identification", "DamFoundation",
                "SoilModel", "Mohr-Coulomb",
                "Colour", 6581619,
                "gammaSat", 21,
                "gammaUnsat", 19,
                "ERef", 65000,
                "nu", 0.3,
                "cRef", 25,
                "phi", 37,
                "psi", 5,
                "GroundwaterClassificationType", "Hypres",
                "GroundwaterSoilClassStandard", "Coarse",
                "GwUseDefaults", False,
                "PermHorizontalPrimary", 0.01,
                "PermVertical", 0.01,
                "RayleighDampingInputMethod", "SDOF equivalent",
                "TargetDamping1", 1,
                "TargetFrequency1", 1,
                "TargetDamping2", 2,
                "TargetFrequency2", 5)
                              
g_i.soilmat("Identification", "Core",
                "SoilModel", "Mohr-Coulomb",
                "Colour", 2253703,
                "DrainageType", "Undrained B",
                "gammaSat", 18,
                "gammaUnsat", 16,
                "ERef", 3000,
                "nu", 0.3,
                "sURef", 5,
                "GroundwaterClassificationType", "Hypres",
                "GroundwaterSoilClassStandard", "Very fine",
                "GwUseDefaults", False,
                "PermHorizontalPrimary", 0.0001,
                "PermVertical", 0.0001,
                "RayleighDampingInputMethod", "SDOF equivalent",
                "TargetDamping1", 3,
                "TargetFrequency1", 1,
                "TargetDamping2", 5,
                "TargetFrequency2", 5)

# Creating borehole and soil layer
g_i.borehole(0)
g_i.soillayer(0)
g_i.Soillayer_1.Zones[0].Top.set(0)
g_i.Soillayer_1.Zones[0].Bottom.set(-70)
g_i.Soillayer_1.Soil.Material.set(g_i.DamFoundation)

g_i.gotostructures()
g_i.polygon((-80,0),(92.5,0.0),(2.5,30.0),(-2.5,30.0))
g_i.cutpoly((-10,0),(-2.5,30))
g_i.cutpoly((10,0), (2.5,30))

g_i.Soil_2.Material.set(g_i.Core)
g_i.Soil_3.Material.set(g_i.DamBody)
g_i.Soil_4.Material.set(g_i.DamBody)

# Creating dynamic displacement multiplier
g_i.displmultiplier()
g_i.DisplacementMultiplier_1.Signal.set("Table")
g_i.DisplacementMultiplier_1.DataType.set("Accelerations")

#Reading EQ acceleration data from a text file
EQacc = []
with open("E:/EQ.txt", "r") as file:
    next(file)  # skip first row (header)
    for line in file:
        values = line.strip().split()
        EQacc.extend(float(v) for v in values)

# Assigning EQ acceleration data to displacement multiplier
g_i.DisplacementMultiplier_1.Table.set(EQacc)
g_i.DisplacementMultiplier_1.DriftCorrection.set(True)

# Creating a line displacement at model bottom boundary and assigning multiplier to it
g_i.linedispl((-150, -70), (150, -70))
g_i.LineDisplacement_1.Displacement_y.set("Fixed")
g_i.LineDisplacement_1.Displacement_x.set("Prescribed")
g_i.LineDisplacement_1.ux_start.set(0.5)
g_i.Line_1.LineDisplacement.LineDisplacement.Multiplierx.set(g_i.DisplacementMultiplier_1)

# Creating interfaces at model boundaries
g_i.neginterface((150,0), (150,-70))
g_i.neginterface((150,-70), (-150,-70))
g_i.neginterface((-150,-70), (-150,0))

# Generating FE mesh and selecting curvepoint
g_i.gotomesh()
g_i.mesh(0.0402)
g_i.selectmeshpoints()
g_o.addcurvepoint("node", (0,30))
g_o.update()

# Defining model conditions for the Initial Phase
g_i.gotowater()
g_i.InitialPhase.Identification.set("FullReservoir")
g_i.InitialPhase.DeformCalcType.set("Gravity loading")
g_i.InitialPhase.PorePresCalcType.set("Steady state groundwater flow")
g_i.waterlevel((-155,25), (-10,25), (93,-10), (155,-10))
g_i.UserWaterLevel_1.rename("FullReservoirWL")
g_i.setglobalwaterlevel(g_i.FullReservoirWL, g_i.InitialPhase)
g_i.Polygons.activate(g_i.InitialPhase)

# Defining a new phase for seismic loading
g_i.gotostages()
g_i.phase(g_i.InitialPhase)
g_i.Phase_1.Identification.set("Earthquake Loading")
g_i.Phase_1.DeformCalcType.set("Dynamics")
g_i.setcurrentphase(g_i.Phase_1)
g_i.LineDisplacement_1.activate(g_i.Phase_1)
g_i.Dynamics.BoundaryXMin.set(g_i.Phase_1, "Free-field")
g_i.Dynamics.BoundaryXMax.set(g_i.Phase_1, "Free-field")
g_i.Dynamics.BoundaryYMin.set(g_i.Phase_1, "Compliant base")
g_i.Phase_1.Deform.UseDefaultIterationParams.set(False)
g_i.Phase_1.Deform.TimeIntervalSeconds.set(50)
g_i.Phase_1.Deform.TimeStepDetermType.set("Manual")
g_i.Phase_1.Deform.MaxSteps.set(1000)
g_i.Phase_1.Deform.SubSteps.set(10)
g_i.apply(g_i.Phases, "setproperties", "ShouldCalculate", True)

# Saving the project
# Path should be modified to ensure that specified folders already exist
g_i.save(r"E:\PLAXIS2D\Dam_EQ.p2dx")

# Calculating and open PLAXIS Output to view results
g_i.calculate()
g_i.view(g_i.Phase_1)

# Creating curves for input acceleration and crest acceleration and saving to file
# Plotting applied accelerogram
mult = EQacc[1::2]
rec_time = EQacc[::2]
plt.plot(rec_time, mult)

# Plotting Dam crest acceleration
crest_acc = g_o.getcurveresultspath(g_o.CN_1,
                                                      g_o.Phase_1,
                                                      g_o.Phase_1,
                                                      g_o.ResultTypes.Soil.Ax)
dtimes = [step.Reached.DynamicTime.value for step in g_o.Phase_1.Steps]
plt.plot(dtimes, crest_acc)
plt.title("Acceleration Time History")
plt.xlabel("Time (s)")
plt.ylabel("x-Acceleration (m/s^2)")
plt.grid()
plt.savefig(r"E:\PLAXIS2D\DamEQaccelerations.png")
plt.show()

g_o.close()