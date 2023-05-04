import numpy as np
import matplotlib.pyplot as plt
from minigrid import *
import imageio
import gym
from minigrid.wrappers import *
from minigrid import*


# State space definition
class State:
    def __init__(self, x, y, has_key, door_status):
        self.x = x
        self.y = y
        self.has_key = has_key
        self.door_status = door_status

# Action Space Definition
ACTIONS = ["MF", "TL", "TR", "PK", "UD"]

#Cost Definition
def get_cost(a):
    if a == "MF" or a == "TL" or a == "TR":
        return 1
    else:
        return 10

# Transition Function Definition
def get_transition(s, a, env):
    x, y, has_key, door_status = s.x, s.y, s.has_key, s.door_status
    if a == "MF":
        if env.grid.get(x, y).can_move("forward"):
            if env.grid.get(x, y).type == "key":
                has_key = True
            elif env.grid.get(x, y).type == "door":
                if has_key:
                    door_status = False
                else:
                    return None
            if env.grid.get(x, y+1) is None:
                return None
            return State(x, y+1, has_key, door_status)
        else:
            return None
    elif a == "TL":
        return State(x, y, has_key, door_status)
    elif a == "TR":
        return State(x, y, has_key, door_status)
    elif a == "PK":
        if env.grid.get(x, y).type == "key":
            has_key = True
            return State(x, y, has_key, door_status)
        else:
            return None
    elif a == "UD":
        if env.grid.get(x, y).type == "door":
            if has_key:
                door_status = False
                return State(x, y, has_key, door_status)
            else:
                return None
        else:
            return None

# Defining the Bellman equation
def bellman(s, V, env):
    q = []
    for a in ACTIONS:
        s_next = get_transition(s, a, env)
        if s_next is not None:
            q.append(get_cost(a) + V[s_next.x, s_next.y, int(s_next.has_key), int(s_next.door_status)])
    if len(q) == 0:
        return None
    else:
        return np.min(q)

# Compute the optimal value function using Dynamic Programming
def value_iteration(env):
    # Initialize the value function
    V = np.zeros((env.width, env.height, 20, 20))

    # Set the goal state
    goal_x, goal_y = env.goal_pos
    V[goal_x, goal_y, :, :] = 0

    # Initialize the plot
    fig, ax = plt.subplots(figsize=(env.width, env.height))

    # Iterate until convergence
    delta = 1
    while delta > 1e-6:
        delta = 0
        for x in range(env.width):
            for y in range(env.height):
                for has_key in [0, 1]:
                    for door_status in [0, 1]:
                        s = State(x, y, bool(has_key), bool(door_status))
                        v = V[x, y, has_key, door_status]
                        q = bellman(s, V, env)
                        if q is not None:
                            if abs(q - v) > delta:
                                delta = abs(q - v)
                            V[x, y, has_key, door_status] = q

        # Render the environment
        env.render(ax=ax)

        # Update the plot
        fig.canvas.draw()

    return V
