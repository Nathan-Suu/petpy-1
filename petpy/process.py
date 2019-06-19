"""
Processing utilities
"""
import numpy as np


def smooth_curve(curve, length):
    """
    Smooth a curve with a boxcar of length 11 elements.
    """
    boxcar = np.ones(length)/length
    return np.convolve(boxcar, curve, mode='same')
