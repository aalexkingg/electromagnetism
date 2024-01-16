from vpython import *
import numpy as np
from atomic import PROTON





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
