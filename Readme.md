# A simple Q-learning control for MountainCar 

## Algorithm

Q-Learning is a model-free form of machine learning, in the sense that the AI "agent" does not need to know or have a model of the environment that it will be in. For a given environment, everything is broken down into "states" and "actions." The states are observations and samplings that we pull from the environment, and the actions are the choices the agent has made based on the observation. 


The algorithm has a function that calculates the quality of a state–action combination known as Q-table: <img src="https://render.githubusercontent.com/render/math?math=\Large Q : S \times A \rightarrow R.">



Before learning begins, <img src="https://render.githubusercontent.com/render/math?math=Q"> is initialized to a random value. Then, at each time <img src="https://render.githubusercontent.com/render/math?math=t"> the agent selects an action <img src="https://render.githubusercontent.com/render/math?math=a_{t}">, 
observes a reward <img src="https://render.githubusercontent.com/render/math?math=r_{t}">,
 enters a new state <img src="https://render.githubusercontent.com/render/math?math=s_{t%2B1}">
 (that may depend on both the previous state <img src="https://render.githubusercontent.com/render/math?math=s_{t}">
 and the selected action), and <img src="https://render.githubusercontent.com/render/math?math=Q"> is updated. The core of the algorithm is a _Bellman equation_ as a simple _value iteration_ update, using the weighted average of the old value and the new information: 

 


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

---
### Copyright
