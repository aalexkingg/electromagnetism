from vpython import *
import numpy as np
from dataclasses import dataclass, replace

epsilon_0 = 8.854187817e-12
epsilon = epsilon_0
k = 1 / (4 * np.pi * epsilon)


@dataclass()
class Charge:
    q: float
    pos: vector
    mass: float

    def __add__(self, other): pass
    def __sub__(self, other): pass
    def __mul__(self, other): pass
    def __truediv__(self, other): pass


# Cartesian, polar or spherical vector basis?

def force(charge1: Charge, charge2: Charge) -> vector:
    """
    Finds the force a charge experiences due to another charge being present
    :param charge1:
    :param charge2:
    :return:
    """
    # Calculates and returns value of the force
    return k * charge1.q * charge2.q * (charge1.pos - charge2.pos) / ((mag(charge1.pos - charge2.pos)) ** 3)


def net_force(charges: list) -> vector:
    """

    :param charges:
    :return:
    """
    f = vector(0, 0, 0)
    for i in range(len(charges)-1):
        f += force(charges[0], charges[i+1])

    return f


def e_field(charge: Charge, pos: vector) -> vector:
    """
    Finds the electric force a charge at that point would feel, per coulomb
    :param charge:
    :param pos:
    :return:
    """
    # Calculates and returns value of the e-field
    return k * charge.q * (charge.pos - pos) / ((mag(charge.pos - pos)) ** 3)


def e_pot_energy(charge1: Charge, charge2: Charge) -> vector:
    """
    Finds the energy a charge has due to another charge being present
    :param charge1:
    :param charge2:
    :return:
    """
    # Calculates and returns value of the potential energy
    return k * charge1.q * charge2.q / mag(charge1.pos - charge2.pos)


def e_pot(charge: Charge, pos: vector) -> vector:
    """
    Finds the potential energy a charge at that point would have, per coulomb
    :param charge:
    :param pos:
    :return:
    """
    # Calculates amd returns the value of the electric potential
    return k * charge.q / mag(charge.pos - pos)


PROTON = Charge(1.602176634e-19, vector(0, 0, 0), 1.672621777e-27)
NEUTRON = Charge(0, vector(0, 0, 0), 1.674927351e-27)
ELECTRON = Charge(-1.602176634e-19, vector(0, 0, 0), 9.10938291e-31)


def main():
    p1 = replace(PROTON)
    p1.pos = vector(0, 0, 0)
    p1.q = 1

    p2 = replace(PROTON)
    p2.pos = vector(1, 0, 0)
    p2.q = 2

    p4 = replace(PROTON)
    p4.pos = vector(0.375, 0.65, 0)
    p4.q = -4

    temp = net_force([p1, p2, p4])
    print(temp)
    print(mag(temp))

    # Continuous charge distribution



if __name__ == "__main__":
    main()
