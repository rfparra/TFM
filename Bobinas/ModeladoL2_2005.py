"""
Script to create a parametric figure of TMS coil and save it in the tcd format.
The coil is constructed using line segments which reconstruct the windings of the coil.
"""

import numpy as np
from simnibs.simulation.tms_coil.tms_coil import TmsCoil

from simnibs.simulation.tms_coil.tms_coil_element import LineSegmentElements
from simnibs.simulation.tms_coil.tms_stimulator import TmsStimulator

# Each function spiral is to create a coil, odds are for core and even for coils
def spiral(radio: float, wire_diam: float, segment_count: int):
    """Creates a spiral path based on the inner and outer diameter of the coil as well as
    the diameter of the wire and the segment count.

    Parameters
    ----------
    outer_diam : float
        The outer diameter of the spiral
    inner_diam : float
        The inner diameter of the spiral
    wire_diam : float
        The diameter of the wire
    segment_count : int
        The amount of segments used to represent the spiral

    Returns
    -------
        The wire path of the spiral
    """
    # Turns of the coil
    N=5.5
    # Height of the coil (mm)
    h=2.2

    #Evencly spaced angles
    phi = np.linspace(0, 2*np.pi*N, segment_count)
    # Coil pitch
    pitch=-h/(2*np.pi*N) 
    path = np.array(
        [radio * np.cos(phi), radio * np.sin(phi), pitch*phi]
    )

    return path

def spiral2(radio2: float, wire_diam2: float, segment_count2: int):
    """Creates a spiral path based on the inner and outer diameter of the coil as well as
    the diameter of the wire and the segment count.

    Parameters
    ----------
    outer_diam : float
        The outer diameter of the spiral
    inner_diam : float
        The inner diameter of the spiral
    wire_diam : float
        The diameter of the wire
    segment_count : int
        The amount of segments used to represent the spiral

    Returns
    -------
        The wire path of the spiral
    """
    # Turns of the coil
    N2=39.56
    # Height of the coil (mm)
    h2=15 
    
    phi = np.linspace(2*np.pi*N2, 0, segment_count)
    pitch2=-h2/(2*np.pi*N2) 
    path = np.array(
        [outer_diam2 * np.cos(phi), outer_diam2 * np.sin(phi), pitch2*phi]
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
     """Generates the windings of a figure of 8 coil

    Parameters
    ----------
    wire_diam : float
        The diameter of the wire
    segment_count : int
       The amount of segments used to represent each of the two spirals
    connection_segment_count : int
        The amount of segments used to connect the different parts of the coil
    outer_diam : float
        The outer diameter of the spiral
    inner_diam : float
        The inner diameter of the spiral
    element_distance : float
        The center to center distance of the two spirals
    winding_casing_distance : float
        The distance of the casing to the windings of the coil

    Returns
    -------
        The windings of a figure of 8 coil
    """
    # Generate the spirals of the coils
    path = spiral(outer_diam, inner_diam, wire_diam, segment_count)
    spiral_1 = (
        path + np.array((-element_distance / 2, 0, -winding_casing_distance))[:, None] # Global position of the  coil
    )

    path = spiral2(outer_diam2, inner_diam, wire_diam, segment_count)
    spiral_2 = np.fliplr(
        path + np.array((-element_distance / 2, 0, -winding_casing_distance))[:, None] # Global position of the core
    )

    return np.concatenate(
        (          
            spiral_2,
            spiral_1,
        ),
        axis=1,
    ).T


# Set up coil parameters
wire_diam = 0.4
wire_diam2 = 0.4
segment_count = 600
segment_count2 = 600
connection_segment_count = 20
radio = 4
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
tms_coil.write("ModeladoL22005.tcd")
