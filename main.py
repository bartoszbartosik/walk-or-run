import numpy as np
from matplotlib import pyplot as plt


def main():
    ########################
    # HUMAN BOX DIMENSIONS #
    ########################
    height = 1.81
    width = 0.5
    depth = 0.3

    # Constants
    a = width * height
    b = width * depth

    ########################
    # ENVIRONMENT SETTINGS #
    ########################
    # Gravitational acceleration
    G = -9.81

    # Rain angle
    phi = -20

    # Distance to travel
    d = 20

    # Velocity domain
    dv = 0.1
    v = np.arange(0, 20, dv)
    V_v = []

    ##################
    # RESULTS & PLOT #
    ##################
    # Volume function
    volume = lambda v: abs(a*d - 1/2*a*G*(d/v)**2*np.tan(np.deg2rad(phi))) - 1/2*b*G*(d/v)**2

    # Compute volume with respect to velocity
    for v_i in v:
        if v_i != 0:
            vol = volume(v_i)
        else:
            vol = float('inf')
        V_v.append(vol)

    # Visualize data
    plt.plot(v, V_v, c='0.3')
    plt.xlabel('velocity [m/s]')
    plt.ylabel('volume [m^3]')
    plt.grid()
    plt.ylim(0, 200)
    plt.show()

if __name__ == '__main__':
    main()