#!/usr/bin/env python3

import rospy
import random
import math
from algorithms.neighbors import find_neighbors

def rrt_algorithm(start_index, goal_index, width, height, costmap, resolution, origin, viz, iterations=5000):
    rrt_tree = {start_index: None}  # Node to parent mapping
    rgba_colors = {'green': 4278255360, 'red': 4294901760, 'blue': 4278190335, 'lime_green': 4284802916}
    
    def random_node():
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        return int(x), int(y)

    def nearest_node(random_node):
        min_dist = float('inf')
        nearest = None
        for node in rrt_tree.keys():
            # Check if the node is not an integer (this can happen if the node is the root of the tree)
            if isinstance(node, int):
                continue

            dist = math.sqrt((node[0] - random_node[0]) ** 2 + (node[1] - random_node[1]) ** 2)
            if dist < min_dist:
                min_dist = dist
                nearest = node
        return nearest


    def steer(from_node, to_node, max_distance=3.0):
        angle = math.atan2(to_node[1] - from_node[1], to_node[0] - from_node[0])
        new_x = from_node[0] + max_distance * math.cos(angle)
        new_y = from_node[1] + max_distance * math.sin(angle)
        return int(new_x), int(new_y)

    def is_valid_node(node):
        return 0 <= node[0] < width and 0 <= node[1] < height and costmap[node[1] * width + node[0]] < 150

    def is_goal_reached(current_node):
        return math.sqrt((current_node[0] - goal_index[0]) ** 2 + (current_node[1] - goal_index[1]) ** 2) < resolution

    def generate_path_from_goal(goal_node):
        path = [goal_node]
        current_node = goal_node
        while current_node != start_index:
            current_node = rrt_tree[current_node]
            path.append(current_node)
        path.reverse()
        return path

    iterations = iterations or 5000  # Set a default value if iterations is None
    for _ in range(iterations):
        random_node_val = random_node()
        nearest_node_val = nearest_node(random_node_val)
        new_node_val = steer(nearest_node_val, random_node_val)
        
        if is_valid_node(new_node_val) and new_node_val not in rrt_tree:
            rrt_tree[new_node_val] = nearest_node_val
            viz.set_color(new_node_val, 'lime_green')  # Visualize the new node
            if is_goal_reached(new_node_val):
                path = generate_path_from_goal(new_node_val)
                return path

    return []

# Other imports and functions remain unchanged

# if __name__ == "__main__":
#     rospy.init_node('rrt_planner_node', log_level=rospy.INFO, anonymous=False)

#     # Replace the following values with your specific values
#     start_index = (10, 10)
#     goal_index = (90, 90)
#     width = 100
#     height = 100
#     resolution = 1.0
#     origin = (0.0, 0.0)
#     costmap = [...]  # Your costmap data as a 1D array

#     # Create a dummy visualization class to satisfy the function signature
#     class DummyViz:
#         def set_color(self, idx, color):
#             pass
    
#     rrt_path = rrt_algorithm(start_index, goal_index, width, height, costmap, resolution, origin, DummyViz(), iterations=5000)
#     print("RRT Path:", rrt_path)
