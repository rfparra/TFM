import os
from simnibs import sim_struct, run_simnibs


S = sim_struct.SESSION()
S.subpath = 'm2m_ernie'  # m2m-folder of the subject
S.pathfem = 'tms_simu'  # Directory for the simulation
S.fields = 'eE'
## Define the TMS simulation
tms = S.add_tmslist()
tms.fnamecoil = os.path.join('legacy_and_other','ModeladoL1052.tcd')  # Choose a coil model
# Define the coil position
pos = tms.add_position()
pos.centre = [0.0,15.0,99.0]  
pos.pos_ydir = [1.0,0.0,1.0]  
pos.distance = 4  #  4 mm distance from coil surface to head surface
pos.didt = 6.283185307

# Run Simulation
run_simnibs(S)

