from utils import *
import sys
sys.path.append("./starter_code")
from example import example_use_of_gym_env
#from starter_code.utils import draw_gif_from_seq, load_env, load_random_env
from starter_code.utils import draw_gif_from_seq, load_env, load_random_env
MF = 0  # Move Forward
TL = 1  # Turn Left
TR = 2  # Turn Right
PK = 3  # Pickup Key
UD = 4  # Unlock Door


def doorkey_problem(env):
    """
    Implementation of the Door&Key algorithm to find the optimal path
    in various doorkey environments.

    Parameters:
    env (gym.Env): The gym environment to solve.

    Returns:
    optim_act_seq (list): The optimal action sequence to solve the environment.
    """
    # Initialize variables
    key_pos = None
    door_pos = None
    current_pos = env.start_pos
    visited = set()
    q = [(current_pos, [], set())] # Position, action sequence, visited positions
    
    while q:
        current_pos, actions, visited = q.pop(0)
        
        # Check if we have reached the goal
        if current_pos == env.goal_pos and env.has_key and env.has_door:
            return actions
        
        # Check if we have picked up the key
        if current_pos == key_pos and not env.has_key:
            env.pickup_key()
        
        # Check if we have unlocked the door
        if current_pos == door_pos and env.has_key and not env.has_door:
            env.unlock_door()
        
        # Check if we have already visited the current position
        if current_pos in visited:
            continue
        
        # Mark the current position as visited
        visited.add(current_pos)
        
        # Get the available actions in the current position
        available_actions = env.get_avail_actions(current_pos)
        
        # Add the next positions to the queue
        for action in available_actions:
            if action == PK:
                key_pos = env.get_key_pos(current_pos)
            elif action == UD:
                door_pos = env.get_door_pos(current_pos)
            
            next_pos = env.get_next_pos(current_pos, action)
            next_actions = actions + [action]
            next_visited = set(visited)
            q.append((next_pos, next_actions, next_visited))
    
    # If we reach here, we couldn't find a solution
    return []


def partA():
    env_path = "./envs/example-8x8.env"
    env, info = load_env(env_path)  # load an environment
    seq = doorkey_problem(env)  # find the optimal action sequence
    draw_gif_from_seq(seq, load_env(env_path)[0])  # draw a GIF & save


def partB():
    env_folder = "./envs/random_envs"
    env, info, env_path = load_random_env(env_folder)
    seq = doorkey_problem(env)  # find the optimal action sequence
    draw_gif_from_seq(seq, env)  # draw a GIF & save


if __name__ == "__main__":
    partA()
    partB()
