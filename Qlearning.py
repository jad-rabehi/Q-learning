import gym
import numpy as np

env = gym.make("MountainCar-v0")

# hyperparameters for the Q-learning
LEARNING_RATE = 0.2
DISCOUNT = 0.85
EPISODES = 2000
SHOW_EVERY = 300

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high -env.observation_space.low)/ DISCRETE_OS_SIZE

Q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE+[env.action_space.n]))

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low)/discrete_os_win_size
    return tuple(discrete_state.astype(np.int))

for episode in range(EPISODES):

    # show simulation every SHOW_EVERY episodes
    if episode % SHOW_EVERY == 0:
        render = True
    else:
        render = False
        
    discrete_state = get_discrete_state(env.reset())
    done = False
    while not done:
        # Argmax action policy
        action = np.argmax(Q_table[discrete_state])
        new_state, reward, done, _ = env.step(action)
        new_discrete_state = get_discrete_state(new_state)

        if render:
            env.render()

        if not done:
            max_future_q = np.max(Q_table[new_discrete_state])
            current_q = Q_table[discrete_state + (action,)]
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            Q_table[discrete_state+(action, )] = new_q

        elif new_state[0] >= env.goal_position:
            print("Goal reached on episode: ", episode)
            Q_table[discrete_state + (action,)] = 0
        discrete_state = new_discrete_state

env.close()
