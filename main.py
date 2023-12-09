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


def force(charge1: Charge, charge2: Charge) -> vector:
    """

    :param charge1:
    :param charge2:
    :return:
    """
    # Calculates and returns value of the force
    return k * charge1.q * charge2.q * (charge1.pos - charge2.pos) / ((mag(charge1.pos - charge2.pos)) ** 3)


def e_field(charge: Charge, pos: vector) -> vector:
    """

    :param charge:
    :param pos:
    :return:
    """
    # Calculates and returns value of the e-field
    return k * charge.q * (charge.pos - pos) / ((mag(charge.pos - pos)) ** 3)


def e_pot_energy(charge1: Charge, charge2: Charge) -> vector:
    """

    :param charge1:
    :param charge2:
    :return:
    """
    # Calculates and returns value of the potential energy
    return k * charge1.q * charge2.q / mag(charge1.pos - charge2.pos)


def e_pot(charge: Charge, pos: vector) -> vector:
    """

    :param charge:
    :param pos:
    :return:
    """
    # Calculates amd returns the value of the electric potential
    return k * charge.q / mag(charge.pos - pos)


PROTON = Charge(1.602176634e-19, 0, 1.672621777e-27)
NEUTRON = Charge(0, 0, 1.674927351e-27)
ELECTRON = Charge(-1.602176634e-19, 0, 9.10938291e-31)


def main():
    f = force(, charge_proton, vector(0,0,0), vector(-4e-15,0,0))
    print(mag(f))


if __name__ == "__main__":
    main()
