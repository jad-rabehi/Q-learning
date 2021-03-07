# A simple Q-learning control for MountainCar (OpenAI's gym)

## Algorithm

Q-Learning is a model-free form of machine learning, in the sense that the AI "agent" does not need to know or have a model of the environment that it will be in. For a given environment, everything is broken down into "states" and "actions." The states are observations and samplings that we pull from the environment, and the actions are the choices the agent has made based on the observation. 


The algorithm has a function that calculates the quality of a state–action combination called Q-table:

   {\displaystyle Q:S\times A\to \mathbb {R} } Q:S\times A\to {\mathbb {R}}.

Before learning begins, $Q$ is initialized randomly. Then, at each time $t$ the agent selects an action $a_t$, observes a reward $r_t$, enters a new state  $s_{t+1}$ (that may depend on both the previous state $s_{t}$ and the selected action), and $Q$ is updated. The core of the algorithm is a *Bellman equation* as a simple *value iteration* update, using the weighted average of the old value and the new information: 

![Q-table update](https://github.com/jad-rabehi/Q-learning/blob/main/images/qlearningwiki.png)




## Instructions

This algorithm is working with an OpenAI's gym, the "MountainCar-v0" environment. 

![evironment start](https://github.com/jad-rabehi/Q-learning/blob/main/images/startepisode.png)

To get gym, just do 
```bash
 pip install gym
```

![evironment end](https://github.com/jad-rabehi/Q-learning/blob/main/images/endepisode.png)
