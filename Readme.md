# A simple Q-learning control for MountainCar 

---

## Instructions
To run the code you need only two librairies; [Numpy](https://numpy.org/install/) and [Gym](https://github.com/openai/gym).

If you use pip, you can install NumPy with:

```bash
 pip install numpy
```

and gym with: 
```bash
 pip install gym
```

---

## Algorithm

Q-Learning is a model-free form of machine learning, in the sense that the AI "agent" does not need to know or have a model of the environment that it will be in. For a given environment, everything is broken down into "states" and "actions." The states are observations and samplings that we pull from the environment, and the actions are the choices the agent has made based on the observation. 


The algorithm has a function that calculates the quality of a state–action combination known as Q-table: <img src="https://render.githubusercontent.com/render/math?math= Q : S \times A \rightarrow R.">



Before learning begins, <img src="https://render.githubusercontent.com/render/math?math=Q"> is initialized to a random value. Then, at each time <img src="https://render.githubusercontent.com/render/math?math=t"> the agent selects an action <img src="https://render.githubusercontent.com/render/math?math=a_{t}">, 
observes a reward <img src="https://render.githubusercontent.com/render/math?math=r_{t}">,
 enters a new state <img src="https://render.githubusercontent.com/render/math?math=s_{t%2B1}">
 (that may depend on both the previous state <img src="https://render.githubusercontent.com/render/math?math=s_{t}">
 and the selected action), and <img src="https://render.githubusercontent.com/render/math?math=Q"> is updated. The core of the algorithm is a _Bellman equation_ as a simple _value iteration_ update, using the weighted average of the old value and the new information: 

 


<img src:"images/qlearningwiki.png" width="600">
*figure credit: https://en.wikipedia.org/wiki/Q-learning*

where <img src="https://render.githubusercontent.com/render/math?math=r_{t}">
 is the reward received when moving from the state <img src="https://render.githubusercontent.com/render/math?math=s_{t}">
 to the state <img src="https://render.githubusercontent.com/render/math?math=s_{t%2B1}">.

For more details, the reader can see the reference
* Sutton, Richard S., and Andrew G. Barto. Reinforcement learning: An introduction. MIT press, 2018.
---

## Environment

This algorithm is working with an OpenAI's gym, the "MountainCar-v0" environment. The goal is to learn the car to move from the  down position to the and reach the up position (Pinned with flag) as it is show in figure below.

![evironment start](https://github.com/jad-rabehi/Q-learning/blob/main/images/startepisode.png)



![evironment end](https://github.com/jad-rabehi/Q-learning/blob/main/images/endepisode.png)

---
### Copyright
