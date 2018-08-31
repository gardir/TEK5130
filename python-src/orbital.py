import numpy as np


def distance_between_earth_centre_and_satellite(a, e, theta):
    """
    r = a(1-e^2) / 1+ecos(theta)
    :param a: the semi-major axis
    :param e: the eccentricity
    :param theta: how for the satellite have traveled "from" the perigree in relation to earth center
    :return: the distance (r) of the satellite from earth center
    """
    return (a * (1 - e ** 2)) / (1 + e * np.cos(theta))


