from vpython import *
import numpy as np

e_0 = 8.854187817e-12

mass_proton = 1.672621777e-27
mass_neutron = 1.674927351e-27
mass_electron = 9.10938291e-31

charge_proton = 1.602176634e-19
charge_neutron = 0
charge_electron = -charge_proton

k = 1 / (4 * np.pi * e_0)


class Charge:
    def __init__(self, q, pos, mass=0.):
        self._q = q
        self._pos = pos
        self._mass = mass

    @property
    def pos(self): return self._pos
    @pos.setter
    def pos(self, pos): self._pos = pos

    @property
    def q(self): return self._q
    @q.setter
    def q(self, q): self._q = q

    @property
    def mass(self): return self._mass
    @mass.setter
    def mass(self, mass): self._mass = mass

    def __add__(self, other): pass
    def __sub__(self, other): pass
    def __mul__(self, other): pass
    def __truediv__(self, other): pass


def force(q1, q2, pos1, pos2):
    """

    :param q1:
    :param q2:
    :param pos1:
    :param pos2:
    :return:
    """
    # Calculates and returns value of the force
    return k * q1 * q2 * (pos1 - pos2) / ((mag(pos1 - pos2)) ** 3)


def e_field(q1, pos1, pos2):
    """

    :param q1:
    :param pos1:
    :param pos2:
    :return:
    """
    # Calculates and returns value of the e-field
    return k * q1 * (pos1 - pos2) / ((mag(pos1 - pos2)) ** 3)


def e_pot_energy(q1, q2, pos1, pos2):
    """

    :param q1:
    :param q2:
    :param pos1:
    :param pos2:
    :return:
    """
    # Calculates and returns value of the potential energy
    return k * q1 * q2 / mag(pos1 - pos2)


def e_pot(q1, pos1, pos2):
    """

    :param q1:
    :param pos1:
    :param pos2:
    :return:
    """
    # Calculates amd returns the value of the electric potential
    return k * q1 / mag(pos1 - pos2)


PROTON = Charge(1.602176634e-19, 0, 1.672621777e-27)
NEUTRON = Charge(0, 0, 1.674927351e-27)
ELECTRON = Charge(-1.602176634e-19, 0, 9.10938291e-31)


def main():
    f = force(charge_proton, charge_proton, vector(0,0,0), vector(-4e-15,0,0))
    print(mag(f))


if __name__ == "__main__":
    main()
