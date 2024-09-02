''' Example on how to run a SimNIBS TMS simulation in Python
    Run with:

    simnibs_python TMS.py

    Copyright (C) 2018 Guilherme B Saturnino
'''
import os
from simnibs import sim_struct, run_simnibs
#print("paso1")
### General Information
S = sim_struct.SESSION()
#print("paso2")
S.fnamehead = 'Mouse_Digimouse.msh'  # m2m-folder of the subject
#print("paso3")
S.pathfem = 'tms_simu'  # Directory for the simulation
#print("paso4")
S.fields = 'eE'
#print("paso5")
## Define the TMS simulation
tms = S.add_tmslist()
#print("paso6")
tms.fnamecoil = os.path.join('legacy_and_other','EstimuladorS05.tcd')  # Choose a coil model
#print("paso7")
# Define the coil position
pos = tms.add_position()
#print("paso8")
pos.centre = [0.0,15.0,28.0]  # Place the coil over C3
#print("paso9")
pos.pos_ydir = [1.0,0.0,1.0]  # Polongation of coil handle (see documentation)
#print("paso10")
pos.distance = 4  #  4 mm distance from coil surface to head surface
pos.didt = 6.283185307
#print("paso11")

# Run Simulation
run_simnibs(S)
print("paso12")
