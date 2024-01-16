# Path Planning Repository for custom robot

## Overview
This repository utilizes path planning algorithms for navigation. This README provides instructions on how to set up and run the simulation.

## Setup

### 1. Clone Repository
Clone the Navogenius and path planning repositories using the following commands:

```bash
git clone https://github.com/bitcurious/NavoGenius.git
```
```bash
git clone https://github.com/bitcurious/Path-Planning.git
```
after cloning do catkin_make

### 2. Launch Simulation
opem a terminal and run following command
```bash
roslaunch myrobot_description gazebo.launch
```
### 3. Launch Navigation with different Path Planning algorithms
To enable navigation with different path planning algorithms, run the following command:
```bash
roslaunch path_planning path_planning.launch
```
It will open a rviz window select 2D Nav Goal button and select the goal position on the map.

![Astar](https://github.com/bitcurious/Path-Planning/blob/master/videos/Screenshot%20from%202023-12-20%2016-31-19.png)

In the path_planning/scripts/path_planning_server.py file, locate line 42 and change the algorithm to your desired one (e.g., astar, dijkstra, rrt).

### 4. RRT

![RRT](https://github.com/bitcurious/Path-Planning/blob/master/videos/RRT.png)

### 5. Dijkstra

![Dijkstra](https://github.com/bitcurious/Path-Planning/blob/master/videos/Dijkstra.png)
