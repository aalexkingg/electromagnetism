import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
from vpython import canvas, vector, sphere, mag
from dataclasses import dataclass, field
import pandas as pd

e_0 = 8.8541878128e-12  # (F m-1) permittivity of free space
e_charge = 1.602e-19   # (C) elementary charge
G = 6.67408e-11     # (m3 kg-1 s-2) Gravitational constant

_element_lookup = pd.read_csv("../base/Periodic Table of Elements.csv")


class _Base:
    @staticmethod
    def e_force(particle1, particle2) -> vector:
        """
        Returns the electric force exerted by object 2 on object 1.
        Input:
            :param particle1: Particle1 object
            :param particle2: Particle2 object
        Depends on:
            - e_0    = permittivity of a vacuum (global variable)
        :return: vector force
        """
        # Calculates and returns value of the force
        return -(1 / (4 * np.pi * e_0)) * particle1.charge * particle2.charge * (
                particle1.position - particle2.position) / ((mag(particle1.position - particle2.position)) ** 3)

    @staticmethod
    def net_e_force(particles) -> vector:
        """

        :param particles:
        :return:
        """
        return np.sum(_Base.e_force(particles[0], particles[i]) for i in range(1, len(particles)))

    @staticmethod
    def e_field(particle, distance: vector) -> vector:
        """

        :param particle:
        :param distance:
        :return:
        """
        return -(1 / (4 * np.pi * e_0)) * particle.charge * (particle.position - distance) / (
                (mag(particle.position - distance)) ** 3)

    @staticmethod
    def e_potential(particle, distance: vector) -> float:
        """

        :param particle:
        :param distance:
        :return:
        """
        return (1 / (4 * np.pi * e_0)) * particle.charge / (mag(particle.position - distance))

    @staticmethod
    def e_pot_energy(particle1, particle2) -> float:
        """

        :param particle1:
        :param particle2:
        :return:
        """
        return (1 / (4 * np.pi * e_0)) * particle1.charge * particle2.charge / (
            mag(particle1.position - particle2.position))

    @staticmethod
    def g_force(particle1, particle2) -> vector:
        """
        Returns the gravitational force exerted by object 2 on object 1.
        Input:
            - particle1 = Particle object
            - particle2 = Particle object
        Depends on:
            - G    = gravitational constant (global variable)
        """
        # Calculates and returns value of the force
        return -G * particle1.mass * particle2.mass * (particle1.position - particle2.position) / (
                (mag(particle1.position - particle2.position)) ** 3)

    @staticmethod
    def net_g_force(particles) -> vector:
        """

        :param particles:
        :return:
        """
        return np.sum(_Base.g_force(particles[0], particles[i]) for i in range(1, len(particles)))

    @staticmethod
    def g_field(particle, distance) -> vector:
        """

        :param particle:
        :param distance:
        :return:
        """
        return -G * particle.mass / (mag(particle.position - distance))

    @staticmethod
    def kinetic_energy() -> float: ...

    @staticmethod
    def total_energy() -> float:
        """

        :return:
        """
        #return _Base.kinetic_energy() + _Base.e_pot_energy()


@dataclass
class System(_Base):
    _permittivity: float = e_0

    @property
    def permittivity(self):
        return self._permittivity

    @permittivity.setter
    def permittivity(self, new):
        self._permittivity = new


class Wave(_Base):
    def __init__(self):
        velocity: float = 0
        wavelength: float = 0


class Particle:
    def __init__(self, symbol):
        (
            self.AtomicNumber,
            self.Element,
            self.Symbol,
            self.AtomicMass,
            self.NumberofNeutrons,
            self.NumberofProtons,
            self.NumberofElectrons,
            self.Period,
            self.Group,
            self.Phase,
            self.Radioactive,
            self.Natural,
            self.Metal,
            self.Nonmetal,
            self.Metalloid,
            self.Type,
            self.AtomicRadius,
            self.Electronegativity,
            self.FirstIonization,
            self.Density,
            self.MeltingPoint,
            self.BoilingPoint,
            self.NumberOfIsotopes,
            self.Discoverer,
            self.Year,
            self.SpecificHeat,
            self.NumberofShells,
            self.NumberofValence
        ) = list(*_element_lookup.loc[_element_lookup['Symbol'] == symbol].itertuples(index=False, name=None))

        self.position: vector = vector(0, 0, 0)
        self.velocity: vector = vector(0, 0, 0)
        self.Z: int = 1
        self._energy: float = 0
        self.composition = []

    def __str__(self):
        return f'{self.Element} particle with {self.NumberofNeutrons} neutrons, {self.NumberofProtons} protons and {self.NumberofElectrons} electrons.'

    def __add__(self, other): ...

    def __sub__(self, other): ...

    def reduced_mass(self, particle):
        """
        For one-electron systems
        :param particle:
        :return:
        """
        if len(self.composition) == 2:
            return (self.composition[0].mass * self.composition[1].mass) / (self.composition[0].mass + self.composition[1].mass)


class Atom(Particle):
    def __init__(self):
        ...

    def energy_n(self, n):
        """

        :param n:
        :return:
        """
        ...


class Ion(Particle):
    def __init__(self, electrons):
        ...


@dataclass
class Charge(_Base):
    charge: float
    mass: float
    position: vector = vector(0, 0, 0)
    velocity: vector = vector(0, 0, 0)


PROTON = Charge(1.602176634e-19, 1.672621777e-27)
NEUTRON = Charge(0, 1.674927351e-27)
ELECTRON = Charge(-1.602176634e-19, 9.10938291e-31)

def main():

    p = Particle("Li")
    print(p)

    #p1 = Particle(0, e)
    #p2 = Particle(0, e)
    #p4 = Particle(0, -4*e)

    #p2.position = vector(4e-10, 0, 0)
    #p4.position = vector(0, 0, 0)


    #print(f"The force between the particle is {mag(p1.force(p2)):.2f} N")


if __name__ == "__main__":
    main()
