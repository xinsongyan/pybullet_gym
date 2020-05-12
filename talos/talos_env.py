import os
import numpy as np
from sim_env import SimEnv
from sim_robot import SimRobot


if __name__ == '__main__':

    sim_rate = 1000
    g = 9.81
    urdfPath = os.getcwd() + '/urdf/talos_lower_body_mesh_updated.urdf'

    homing_config = np.zeros(12)

    sim_env = SimEnv(sim_rate=sim_rate)

    robot = SimRobot(urdfFileName=urdfPath,
                     basePosition=[-0.0, 0, 1.5],
                     baseRPY=[0, 0, 0],
                     useFixedBase=False,
                     jointPositions=homing_config)

    sim_env.reset()
    while True:


        sim_env.step()
        sim_env.debug()