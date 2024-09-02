
import numpy as np
from simnibs.simulation.tms_coil.tms_coil import TmsCoil

from simnibs.simulation.tms_coil.tms_coil_element import LineSegmentElements
from simnibs.simulation.tms_coil.tms_stimulator import TmsStimulator

def spiral(radio: float, wire_diam: float, segment_count: int):

    N=3.5 #Numero de vueltas
    h=2.625 #Altura de la bobina en mm

    phi = np.linspace(0, 2*np.pi*N, segment_count)
    paso=-h/(2*np.pi*N) 
    path = np.array(
        [radio * np.cos(phi), radio * np.sin(phi), paso*phi]
    )

    return path

def spiral2(radio2: float, wire_diam2: float, segment_count2: int):

    N2=68.5 #Numero de vueltas
    h2=15 #Altura de la bobina en mm

    phi = np.linspace(2*np.pi*N2, 0, segment_count)#El numero que multiplica el 2*pi del segundo parametro equivale al numero de vueltas
    paso2=-h2/(2*np.pi*N2) #Este valor es la altura de la bobina (h) entre 2*pi por el numero de vueltas(N). -h/(2*pi*N) el menos es para que la espira "crezca" hacia afuera y no hacia el craneo
    path = np.array(
        [outer_diam2 * np.cos(phi), outer_diam2 * np.sin(phi), paso2*phi]
    )

    return path

def figure_of_wire_path(
    wire_diam: float,
    wire_diam2: float,
    segment_count: int,
    segment_count2: int,
    connection_segment_count: int,
    radio: float,
    radio2: float,
    element_distance: float,
    winding_casing_distance: float,
):
    path = spiral(outer_diam, inner_diam, wire_diam, segment_count)
    spiral_1 = (
        path + np.array((-element_distance / 2, 0, -winding_casing_distance))[:, None]
    )

    path = spiral2(outer_diam2, inner_diam, wire_diam, segment_count)
    spiral_2 = np.fliplr(
        path + np.array((-element_distance / 2, 0, -winding_casing_distance))[:, None]
    )

    return np.concatenate(
        (          
            spiral_2,
            spiral_1,
        ),
        axis=1,
    ).T


# Set up coil parameters
wire_diam = 0.75
wire_diam2 = 0.75
segment_count = 600
segment_count2 = 600
connection_segment_count = 20
radio = 7.5 
radio2 = 40
element_distance = 0
winding_casing_distance = 0.5


wire_path = figure_of_wire_path(
    wire_diam,
    wire_diam2,
    segment_count,
    segment_count2,
    connection_segment_count,
    radio,   
    rado2,
    element_distance,
    winding_casing_distance,
)

# The limits of the a field of the coil, used for the transformation into nifti format
limits = [[-300.0, 300.0], [-200.0, 200.0], [-100.0, 300.0]]
# The resolution used when sampling to transform into nifti format
resolution = [2, 2, 2]

# Creating a example stimulator with a name, a brand and a maximum dI/dt
stimulator = TmsStimulator("Example Stimulator", "Example Stimulator Brand", 122.22e6)

# Creating the line segments from a list of wire path points
line_element = LineSegmentElements(stimulator, wire_path, name="Figure_of_8")
# Creating the TMS coil with its element, a name, a brand, a version, the limits and the resolution
tms_coil = TmsCoil(
    [line_element], "Example Coil", "Example Coil Brand", "V1.0", limits, resolution
)

# Generating a coil casing that has a specified distance from the coil windings
tms_coil.generate_element_casings(
    winding_casing_distance, winding_casing_distance / 2, False
)

# Write the coil to a tcd file
tms_coil.write("ModeladoBobina.tcd")