#!/usr/bin/python3
"""Module that multiplies 2 matrices."""


def matrix_mul(m_a, m_b):
    """multiply two matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a must be a list of lists")
    for i in m_b:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b must be a list of lists")
    for i in m_a:
        if len(m_a[0]) != len(i):
            raise TypeError("each row of m_a must be of the same size")
    for i in m_b:
        if len(m_b[0]) != len(i):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    new_m = []
    for i in range(len(m_a)):
        new_m.append([])
        for j in range(len(m_b)):
            new_m[i].append(0)

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_a[0])):
                new_m[i][j] += m_a[i][k] * m_b[k][j]
    return new_m
