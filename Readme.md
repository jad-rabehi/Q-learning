# A simple Q-learning control for MountainCar (OpenAI's gym)

## Algorithm

Q-Learning is a model-free form of machine learning, in the sense that the AI "agent" does not need to know or have a model of the environment that it will be in. For a given environment, everything is broken down into "states" and "actions." The states are observations and samplings that we pull from the environment, and the actions are the choices the agent has made based on the observation. 


The algorithm, therefore, has a function that calculates the quality of a state–action combination:

    Q : S × A → R.

 


![Q-table update](https://github.com/jad-rabehi/Q-learning/blob/main/images/qlearningwiki.png)


---

## Instructions

This algorithm is working with an OpenAI's gym, the "MountainCar-v0" environment. 

![evironment start](https://github.com/jad-rabehi/Q-learning/blob/main/images/startepisode.png)

To get gym, just do 
```bash
 pip install gym
```

![evironment end](https://github.com/jad-rabehi/Q-learning/blob/main/images/endepisode.png)
