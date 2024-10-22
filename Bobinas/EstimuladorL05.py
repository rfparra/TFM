"""
Script to create a parametric figure of TMS coil and save it in the tcd format.
The coil is constructed using line segments which reconstruct the windings of the coil.
This is a 4 coil stimulator compound by coils L1
"""

import numpy as np
from simnibs.simulation.tms_coil.tms_coil import TmsCoil

from simnibs.simulation.tms_coil.tms_coil_element import LineSegmentElements
from simnibs.simulation.tms_coil.tms_stimulator import TmsStimulator

# Each function spiral is to create a coil, odds are for core and even for coils
def spiral(outer_diam: float, inner_diam: float, wire_diam: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)
    # Turns of the coil
    N=3.5
    # Height of the coil (mm)
    h=2.625 

    #Evenly spaced angles
    phi = np.linspace(0, 2*np.pi*N, segment_count)
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    # Coil pitch
    pitch=-h/(2*np.pi*N) 
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam * np.cos(phi), outer_diam * np.sin(phi), pitch*phi]
    )

    return path

def spiral2(outer_diam2: float, inner_diam: float, wire_diam: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)
    # Turns of the coil
    N2=68.5 
    # Height of the coil (mm)
    h2=15 

    # Evenly spaced angles 
    phi = np.linspace(2*np.pi*N2, 0, segment_count)
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    # Coil pitch
    altura2=-h2/(2*np.pi*N2)
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam2 * np.cos(phi), outer_diam2 * np.sin(phi), altura2*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral3(outer_diam: float, inner_diam: float, wire_diam: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)
    # Turns of the coil
    N=3.5
    # Height of the coil (mm)
    h=2.625 

    #Evenly spaced angles
    phi = np.linspace(0, 2*np.pi*N, segment_count)
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    # Coil pitch
    pitch=-h/(2*np.pi*N) 
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam * np.cos(phi), outer_diam * np.sin(phi), pitch*phi]
    )

    return path

def spiral4(outer_diam2: float, inner_diam: float, wire_diam: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)
    # Turns of the coil
    N2=68.5 
    # Height of the coil (mm)
    h2=15 

    # Evenly spaced angles 
    phi = np.linspace(2*np.pi*N2, 0, segment_count)
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    # Coil pitch
    altura2=-h2/(2*np.pi*N2)
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam2 * np.cos(phi), outer_diam2 * np.sin(phi), altura2*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral5(outer_diam: float, inner_diam: float, wire_diam: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)
    # Turns of the coil
    N=3.5
    # Height of the coil (mm)
    h=2.625 

    #Evenly spaced angles
    phi = np.linspace(0, 2*np.pi*N, segment_count)
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    # Coil pitch
    pitch=-h/(2*np.pi*N) 
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam * np.cos(phi), outer_diam * np.sin(phi), pitch*phi]
    )

    return path

def spiral6(outer_diam2: float, inner_diam: float, wire_diam: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)
    # Turns of the coil
    N2=68.5 
    # Height of the coil (mm)
    h2=15 

    # Evenly spaced angles 
    phi = np.linspace(2*np.pi*N2, 0, segment_count)
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    # Coil pitch
    altura2=-h2/(2*np.pi*N2)
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam2 * np.cos(phi), outer_diam2 * np.sin(phi), altura2*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral7(outer_diam: float, inner_diam: float, wire_diam: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)
    # Turns of the coil
    N=3.5
    # Height of the coil (mm)
    h=2.625 

    #Evenly spaced angles
    phi = np.linspace(0, 2*np.pi*N, segment_count)
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    # Coil pitch
    pitch=-h/(2*np.pi*N) 
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam * np.cos(phi), outer_diam * np.sin(phi), pitch*phi]
    )

    return path

def spiral8(outer_diam2: float, inner_diam: float, wire_diam: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)
    # Turns of the coil
    N2=68.5 
    # Height of the coil (mm)
    h2=15 

    # Evenly spaced angles 
    phi = np.linspace(2*np.pi*N2, 0, segment_count)
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    # Coil pitch
    altura2=-h2/(2*np.pi*N2)
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam2 * np.cos(phi), outer_diam2 * np.sin(phi), altura2*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral9(outer_diam3: float, inner_diam: float, wire_diam2: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)

    N=6.5 #Numero de vueltas
    h=1.17 #Altura de la bobina en mm

    # Evenly spaced angles between 30 degrees and phi_max
    phi = np.linspace(0, 2*np.pi*N, segment_count)#El numero que multiplica el 2*pi del segundo parametro equivale al numero de vueltas
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    #Array de altura
    #altura = np.linspace(0,-14/(2*np.pi*18),segment_count)
    altura=-h/(2*np.pi*N) #Este valor es la altura de la bobina (h) entre 2*pi por el numero de vueltas(N). -h/(2*pi*N) el menos es para que la espira "crezca" hacia afuera y no hacia el craneo
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam3 * np.cos(phi), outer_diam3 * np.sin(phi), altura*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral10(outer_diam4: float, inner_diam: float, wire_diam2: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam4 / 2 - inner_diam / 2) / (wire_diam2 / 2)

    N2=15.84 #Numero de vueltas
    h2=4 #Altura de la bobina en mm

    # Evenly spaced angles between 30 degrees and phi_max
    phi = np.linspace(2*np.pi*N2, 0, segment_count)#El numero que multiplica el 2*pi del segundo parametro equivale al numero de vueltas
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam4 / 2 - wire_diam2 / 2 * phi / (2 * np.pi)
    #Array de altura
    #altura = np.linspace(0,-14/(2*np.pi*18),segment_count)
    altura2=-h2/(2*np.pi*N2) #Este valor es la altura de la bobina (h) entre 2*pi por el numero de vueltas(N). -h/(2*pi*N) el menos es para que la espira "crezca" hacia afuera y no hacia el craneo
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam4 * np.cos(phi), outer_diam4 * np.sin(phi), altura2*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral11(outer_diam3: float, inner_diam: float, wire_diam2: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)

    N=6.5 #Numero de vueltas
    h=1.17 #Altura de la bobina en mm

    # Evenly spaced angles between 30 degrees and phi_max
    phi = np.linspace(0, 2*np.pi*N, segment_count)#El numero que multiplica el 2*pi del segundo parametro equivale al numero de vueltas
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    #Array de altura
    #altura = np.linspace(0,-14/(2*np.pi*18),segment_count)
    altura=-h/(2*np.pi*N) #Este valor es la altura de la bobina (h) entre 2*pi por el numero de vueltas(N). -h/(2*pi*N) el menos es para que la espira "crezca" hacia afuera y no hacia el craneo
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam3 * np.cos(phi), outer_diam3 * np.sin(phi), altura*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral12(outer_diam4: float, inner_diam: float, wire_diam2: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam4 / 2 - inner_diam / 2) / (wire_diam2 / 2)

    N2=15.84 #Numero de vueltas
    h2=4 #Altura de la bobina en mm

    # Evenly spaced angles between 30 degrees and phi_max
    phi = np.linspace(2*np.pi*N2, 0, segment_count)#El numero que multiplica el 2*pi del segundo parametro equivale al numero de vueltas
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam4 / 2 - wire_diam2 / 2 * phi / (2 * np.pi)
    #Array de altura
    #altura = np.linspace(0,-14/(2*np.pi*18),segment_count)
    altura2=-h2/(2*np.pi*N2) #Este valor es la altura de la bobina (h) entre 2*pi por el numero de vueltas(N). -h/(2*pi*N) el menos es para que la espira "crezca" hacia afuera y no hacia el craneo
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam4 * np.cos(phi), outer_diam4 * np.sin(phi), altura2*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral13(outer_diam3: float, inner_diam: float, wire_diam2: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)

    N=6.5 #Numero de vueltas
    h=1.17 #Altura de la bobina en mm

    # Evenly spaced angles between 30 degrees and phi_max
    phi = np.linspace(0, 2*np.pi*N, segment_count)#El numero que multiplica el 2*pi del segundo parametro equivale al numero de vueltas
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    #Array de altura
    #altura = np.linspace(0,-14/(2*np.pi*18),segment_count)
    altura=-h/(2*np.pi*N) #Este valor es la altura de la bobina (h) entre 2*pi por el numero de vueltas(N). -h/(2*pi*N) el menos es para que la espira "crezca" hacia afuera y no hacia el craneo
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam3 * np.cos(phi), outer_diam3 * np.sin(phi), altura*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral14(outer_diam4: float, inner_diam: float, wire_diam2: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam4 / 2 - inner_diam / 2) / (wire_diam2 / 2)

    N2=15.84 #Numero de vueltas
    h2=4 #Altura de la bobina en mm

    # Evenly spaced angles between 30 degrees and phi_max
    phi = np.linspace(2*np.pi*N2, 0, segment_count)#El numero que multiplica el 2*pi del segundo parametro equivale al numero de vueltas
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam4 / 2 - wire_diam2 / 2 * phi / (2 * np.pi)
    #Array de altura
    #altura = np.linspace(0,-14/(2*np.pi*18),segment_count)
    altura2=-h2/(2*np.pi*N2) #Este valor es la altura de la bobina (h) entre 2*pi por el numero de vueltas(N). -h/(2*pi*N) el menos es para que la espira "crezca" hacia afuera y no hacia el craneo
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam4 * np.cos(phi), outer_diam4 * np.sin(phi), altura2*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral15(outer_diam3: float, inner_diam: float, wire_diam2: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam / 2 - inner_diam / 2) / (wire_diam / 2)

    N=6.5 #Numero de vueltas
    h=1.17 #Altura de la bobina en mm

    # Evenly spaced angles between 30 degrees and phi_max
    phi = np.linspace(0, 2*np.pi*N, segment_count)#El numero que multiplica el 2*pi del segundo parametro equivale al numero de vueltas
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam / 2 - wire_diam / 2 * phi / (2 * np.pi)
    #Array de altura
    #altura = np.linspace(0,-14/(2*np.pi*18),segment_count)
    altura=-h/(2*np.pi*N) #Este valor es la altura de la bobina (h) entre 2*pi por el numero de vueltas(N). -h/(2*pi*N) el menos es para que la espira "crezca" hacia afuera y no hacia el craneo
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam3 * np.cos(phi), outer_diam3 * np.sin(phi), altura*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def spiral16(outer_diam4: float, inner_diam: float, wire_diam2: float, segment_count: int):
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
    # Calculates the maximal spiral angle
    phi_max = 2 * np.pi * (outer_diam4 / 2 - inner_diam / 2) / (wire_diam2 / 2)

    N2=15.84 #Numero de vueltas
    h2=4 #Altura de la bobina en mm

    # Evenly spaced angles between 30 degrees and phi_max
    phi = np.linspace(2*np.pi*N2, 0, segment_count)#El numero que multiplica el 2*pi del segundo parametro equivale al numero de vueltas
    # Calculates the radius of every line segment in the spiral
    radius_loop = outer_diam4 / 2 - wire_diam2 / 2 * phi / (2 * np.pi)
    #Array de altura
    #altura = np.linspace(0,-14/(2*np.pi*18),segment_count)
    altura2=-h2/(2*np.pi*N2) #Este valor es la altura de la bobina (h) entre 2*pi por el numero de vueltas(N). -h/(2*pi*N) el menos es para que la espira "crezca" hacia afuera y no hacia el craneo
    # Calculates the cartesian coordinates of the spiral
    path = np.array(
        [outer_diam4 * np.cos(phi), outer_diam4 * np.sin(phi), altura2*phi]#donde pone outer_diam, habra que poner el radio de la bobina
    )#

    return path

def figure_of_8_wire_path(
    wire_diam: float,
    wire_diam2: float,
    segment_count: int,
    segment_count2: int,
    segment_count3: int,
    connection_segment_count: int,
    outer_diam: float,
    outer_diam2: float,
    outer_diam3: float,
    outer_diam4: float,
    inner_diam: float,
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
    # Generate left spiral of the coil
    path = spiral(outer_diam, inner_diam, wire_diam, segment_count)
    spiral_1 = (
        path + np.array((0, 11.497, -winding_casing_distance))[:, None]
    )

    path = spiral2(outer_diam2, inner_diam, wire_diam, segment_count)
    spiral_2 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((0, 11.497, -winding_casing_distance))[:, None]
    )

    path = spiral3(outer_diam, inner_diam, wire_diam, segment_count)
    spiral_3 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((12.386, 0, -winding_casing_distance))[:, None]
    )

    path = spiral4(outer_diam2, inner_diam, wire_diam, segment_count)
    spiral_4 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((12.386, 0, -winding_casing_distance))[:, None]
    )

    path = spiral5(outer_diam, inner_diam, wire_diam, segment_count)
    spiral_5 = (
        path + np.array((0, -11.497, -winding_casing_distance))[:, None]
    )

    path = spiral6(outer_diam2, inner_diam, wire_diam, segment_count)
    spiral_6 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((0, -11.497, -winding_casing_distance))[:, None]
    )

    path = spiral7(outer_diam, inner_diam, wire_diam, segment_count)
    spiral_7 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((-12.386, 0, -winding_casing_distance))[:, None]
    )

    path = spiral8(outer_diam2, inner_diam, wire_diam, segment_count)
    spiral_8 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((-12.386, 0, -winding_casing_distance))[:, None]
    )

    path = spiral9(outer_diam3, inner_diam, wire_diam2, segment_count)
    spiral_9 = (
        path + np.array((-3.5335, -2.7185, -winding_casing_distance))[:, None]
    )

    path = spiral10(outer_diam4, inner_diam, wire_diam2, segment_count)
    spiral_10 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((-3.5335, -2.7185, -winding_casing_distance))[:, None]
    )

    path = spiral11(outer_diam3, inner_diam, wire_diam2, segment_count2)
    spiral_11 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((3.5335, -2.7185, -winding_casing_distance))[:, None]
    )

    path = spiral12(outer_diam4, inner_diam, wire_diam2, segment_count)
    spiral_12 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((3.5335, -2.7185, -winding_casing_distance))[:, None]
    )
    path = spiral13(outer_diam3, inner_diam, wire_diam2, segment_count)
    spiral_13 = (
        path + np.array((3.5335, 2.7185, -winding_casing_distance))[:, None]
    )

    path = spiral14(outer_diam4, inner_diam, wire_diam2, segment_count)
    spiral_14 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((3.5335, 2.7185, -winding_casing_distance))[:, None]
    )

    path = spiral15(outer_diam3, inner_diam, wire_diam2, segment_count)
    spiral_15 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((-3.5335, 2.7185, -winding_casing_distance))[:, None]
    )

    path = spiral16(outer_diam4, inner_diam, wire_diam2, segment_count)
    spiral_16 = np.fliplr(
         #* np.array((-1, 1, 1))[:, None]
        path + np.array((-3.5335, 2.7185, -winding_casing_distance))[:, None]
    )
    # Generate incoming wire to the coil inside handle
    """initial_wire_path = np.linspace(
        (outer_diam, -outer_diam, -2),
        (outer_diam, 0, -2),
        connection_segment_count,
    ).T
    # Generate outgoing wire from the coil inside handle
    ending_wire_path = np.linspace(
        (-outer_diam, 0, -2),
        (-outer_diam, -outer_diam , -2),
        connection_segment_count,
    ).T"""

    # Generate the connection from the incoming wire to the right spiral center
    """wire_coil_2_connection = np.linspace(
        initial_wire_path[:, -1], spiral_2[:, 0], connection_segment_count
    ).T"""
    # Generate the connection from end of the right spiral to the outside start of the left spiral
    """coil_coil_connection = np.linspace(
        spiral_2[:, -2], spiral_1[:, 0], connection_segment_count
    ).T"""
    # Generate the connection from the inside of the left spiral to the outgoing wire
    """coil_1_wire_connection = np.linspace(
        spiral_1[:, -1], ending_wire_path[:, 0], connection_segment_count
    ).T"""

    return np.concatenate(
        (
            #initial_wire_path,
            #coil_coil_connection,
            spiral_16,
            spiral_15,
            spiral_14,
            spiral_13,
            spiral_12,
            spiral_11,
            spiral_10,
            spiral_9,
            spiral_8,
            spiral_7,
            spiral_6,
            spiral_5,
            spiral_4,
            spiral_3,
            spiral_2,
            spiral_1,
            #coil_1_wire_connection,
            #ending_wire_path,
        ),
        axis=1,
    ).T


# Set up coil parameters
wire_diam = 0.75
wire_diam2 = 0.18
segment_count = 600
segment_count2 = 600
segment_count3 = 1000
connection_segment_count = 20
outer_diam = 7.5 #Esto ya nos da igual, solo se va a tener un diametro
inner_diam = 0.02
outer_diam2 = 40
outer_diam3= 1.25
outer_diam4= 7
element_distance = 0
winding_casing_distance = 0.5


wire_path = figure_of_8_wire_path(
    wire_diam,
    wire_diam2,
    segment_count,
    segment_count2,
    segment_count3,
    connection_segment_count,
    outer_diam,   
    outer_diam2,
    outer_diam3,
    outer_diam4,
    inner_diam,
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
tms_coil.write("EstimuladorL05.tcd")
