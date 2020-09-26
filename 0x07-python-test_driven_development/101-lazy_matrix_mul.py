#!/usr/bin/python3
"""Module that multiplies matrices using Numpy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies using Numpy"""
    return numpy.dot(m_a, m_b)
