import math
import logging


logger = logging.getLogger(__name__)

keplers_constant = 3.986*10**5  # km**3/s**2
Re = 6378  # km
KJELLER_LAT = math.radians(59.9693)
KJELLER_LON = math.radians(11.0361)


def distance_between_earth_centre_and_satellite(a, e, theta):
    """
    r = a(1-e^2) / 1+ecos(theta)
    :param a: the semi-major axis
    :param e: the eccentricity
    :param theta: how for the satellite have traveled "from" the perigree in relation to earth center
    :return: the distance (r) of the satellite from earth center
    """
    return (a * (1 - e ** 2)) / (1 + e * np.cos(theta))


def distance_between_position_and_satellite(lat, lon, satellite_height, lat_satellite=0, lon_satellite=0):
    """
    d = sqrt( R_e^2 + r^2 - 2R_e r cos(W) )
    R_e:    Earth radius (in km)
    r:      Distance from Earth center to satellite (in km)
    cos(W): sin(L_e)sin(L_s) + cos(L_e)cos(L_s)cos(l_e-l_s)
    e:      user location
    s:      satellite location
    GSO:    L_s = 0 => cos(W) = cos(L_e)cos(l_e-l_s)
    L = latitude
    l = longitude
    """
    R_e = 6371  # km
    r   = R_e + satellite_height
    L_e = lat
    l_e = lon
    L_s = lat_satellite
    l_s = lon_satellite
    GSO = lat_satellite
    if GSO:
        cos_W = math.cos(L_e) * math.cos(l_e - l_s)
    else:
        cos_W = math.sin(L_e) * math.sin(L_s) + math.cos(L_e) * math.cos(L_s) * math.cos(l_e - l_s)
    d = math.sqrt( R_e**2 + r**2 - 2 * R_e * r * cos_W )
    return d
    

def dB(val):
    return 10**(val/10)


def todB(val):
    return 10 * math.log(val)


def get_semi_major_axis(T):
    s = T/2*math.pi
    print(s)
    s = s**2
    s *= keplers_constant
    print(s)
    s = math.pow(s, 1/3)
#    return math.pow((T/2*math.pi)**2*keplers_constant, 1/3)
    return s


def get_period(a):
    return 2*math.pi*math.sqrt(a**3/keplers_constant)


def get_eccentricity_from_perigee(a, hp):
    return 1 - (hp + Re)/a
