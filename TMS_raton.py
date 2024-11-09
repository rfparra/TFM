""" How to run a SimNIBS TMS simulation in Python
    Run with:

    simnibs_python TMS.py
    Copyright (C) 2018 Guilherme B Saturnino
"""
import os
from simnibs import sim_struct, run_simnibs

### General Information
S = sim_struct.SESSION()
S.fnamehead = 'Mouse_Digimouse.msh'  # m2m-folder of the subject
S.pathfem = 'tms_simu'  # Directory for the simulation
S.fields = 'eE' #Fields to calculate

## Define the TMS simulation
tms = S.add_tmslist()
tms.fnamecoil = os.path.join('legacy_and_other','EstimuladorS05.tcd')  # Choose a coil model

# Define the coil position
pos = tms.add_position()
pos.centre = [0.0,15.0,28.0] #Place the coil in a determinated position
pos.pos_ydir = [1.0,0.0,1.0]  #Orientation of the coil
pos.distance = 4  #Distance from coil surface to head surface (mm)
pos.didt = 6.283185307 #Define the value of didt

# Run Simulation
run_simnibs(S)
