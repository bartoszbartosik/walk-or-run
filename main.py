import numpy as np
from matplotlib import pyplot as plt


def main():
    ########################
    # HUMAN BOX DIMENSIONS #
    ########################
    height = 1.81
    width = 0.5
    depth = 0.3

    a = width * height
    b = width * depth


    ########################
    # ENVIRONMENT SETTINGS #
    ########################
    G = -9.81
    phi = -20

    # Distance to travel
    d = 20

    #######################
    # SIMULATION SETTINGS #
    #######################
    dt = 0.1
    t = np.arange(0, 20, dt)
    dv = 0.1
    v = np.arange(0, 20, dv)

    V_t = []
    V_v = []

    for v_i in v:
        if v_i != 0:
            vol = abs(a*d - 1/2*a*G*(d/v_i)**2*np.tan(np.deg2rad(phi))) - 1/2*b*G*(d/v_i)**2
        else:
            vol = float('inf')
        V_v.append(vol)

    v_min = min(V_v)

    for t_i in t:
            vol = abs(a*v_min*t_i - 1/2*a*G*t_i**2*np.tan(np.deg2rad(phi))) - 1/2*b*G*t_i**2
            V_t.append(vol)

    plt.plot(v, V_v, c='0.3')
    plt.xlabel('velocity [m/s]')
    plt.ylabel('volume [m^3]')
    plt.grid()
    plt.ylim(0, 200)
    plt.show()

if __name__ == '__main__':
    main()