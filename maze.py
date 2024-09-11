"""
   Vinni Panagiota
   A.M. : 1873
   Semester : 5th
   Email: penyvinni@gmail.com 
"""

from disjoint_set import DisjointSet
import random
import time
import matplotlib.pyplot as plt
from collections import deque


class Maze:
    """The maze class.

    Generates a perfect maze of given length and height

    Attributes:
        entrance: An integer indicating the entrance of the maze.
        exit: An integer indicating the exit of the maze.
        length: The length of the maze
        height: The height of the maze
        size: length * height
        adjacency_list: Set of edges representing paths in maze
        adjacency_map: A dictionary representation of the edges (key: vertex, value: vertex neighbours) for bfs

    Methods:
        visualize_maze(): Visualize maze with matplotlibs cmap
        evaluate_solution(solution): Evaluates to true or false a given sequence
    """

    def __init__(
        self,
        length,
        height,
        entrance=None,
        entrance_direction=None,
        exit=None,
        exit_direction=None,
        seed=None,
    ):
        """Definision of parametrs, creation and design of maze"""

        # If no seed is provided use current time
        if seed == None:
            random.seed(time.time())

        # Set length and height
        self._length = length
        self._height = height

        # If no entrance is provided default to node 1 and direction 'UP'
        if entrance == None or entrance_direction == None:
            self._entrance = 1
            self._entrance_direction = "UP"
        else:
            self._entrance = entrance
            self._entrance_direction = entrance_direction

        # If no exit is provided default to last node and direction 'RIGHT'
        if exit == None or exit_direction == None:
            self._exit = length * height
            self._exit_direction = "RIGHT"
        else:
            self._exit = exit
            self._exit_direction = exit_direction

        # Create all possible walls  ftiaxnv tis edges
        edges = list()
        for i in range(1, self.size + 1):  # we use +1 because it's open space
            if i % length > 0:
                edges.append((i, i + 1))  # tuple
            if 1 + i // self.length < self.height:
                edges.append((i, i + self.length))

        # Do some suffling  anakateuw tis edges
        random.shuffle(edges)

        # Remove some walls  afairv tis edges gia na ginei monopati
        removed = set()
        ds = DisjointSet()  # creating an empty structure union - find
        for i in range(1, self.size + 1):
            ds.find(i)  #for each node
        for e1, e2 in edges:  # e1 e2 <- (1,2) (1,4) (2,3) (2,5) (3,6) ....
            if ds.find(e1) != ds.find(e2):
                removed.add((e1, e2))  # node added to the remmoved nodes
                ds.union(ds.find(e1), ds.find(e2))  # join the edges
                #because there has been a change in the maze I check if 
                #entranceand exit are in the same set
                if ds.find(self._entrance) == ds.find(self._exit):
                    break
        self._adjacency_list = set(removed)


    # We use properties to take entrance, exit etc. as attributes and not as functions
    @property
    def entrance(self):
        return self._entrance

    @property
    def exit(self):
        return self._exit

    @property
    def length(self):
        return self._length

    @property
    def height(self):
        return self._height

    @property
    def size(self):
        return self.height * self.length

    @property
    def adjacency_list(self):
        """ Fuction that shows the neighbours nodes"""
        return self._adjacency_list

    @property
    def adjacency_map(self):
        """ Function that convert adjacency_list to a dictionary to make the bfs function below work"""
        adj_map = dict()
        for v1, v2 in self.adjacency_list:
            if v1 not in adj_map.keys():
                adj_map[v1] = set()
            adj_map[v1].add(v2)

            if v2 not in adj_map.keys():
                adj_map[v2] = set()
            adj_map[v2].add(v1)

        return adj_map

    def visualize_maze(self):
        """Visualize maze with matplotlibs cmap"""
        grid = [[1 for _ in range(3 * self._length)] for _ in range(3 * self._height)]

        for point, direction in [
            (self._entrance, self._entrance_direction),
            (self._exit, self._exit_direction),
        ]:
            point_x = ((point - 1) % self._length) * 3 + 1
            point_y = ((point - 1) // self._length) * 3 + 1

            grid[point_y][point_x] = 0
            if direction == "UP":
                grid[point_y - 1][point_x] = 0
            elif direction == "RIGHT":
                grid[point_y][point_x + 1] = 0
            elif direction == "DOWN":
                grid[point_y + 1][point_x] = 0
            elif direction == "LEFT":
                grid[point_y][point_x - 1] = 0

        for e1, e2 in self._adjacency_list:
            if e1 > e2:
                e1, e2 = e2, e1

            point_x = ((e2 - 1) % self._length) * 3 + 1
            point_y = ((e2 - 1) // self._length) * 3 + 1
            grid[point_y][point_x] = 0

            point_x = ((e1 - 1) % self._length) * 3 + 1
            point_y = ((e1 - 1) // self._length) * 3 + 1
            grid[point_y][point_x] = 0

            if (e1 - 1) // self._length == (e2 - 1) // self._length:
                grid[point_y][point_x + 1] = 0
                grid[point_y][point_x + 2] = 0
            else:
                grid[point_y + 1][point_x] = 0
                grid[point_y + 2][point_x] = 0

        plt.figure(figsize=(10, 10))
        plt.imshow(grid, cmap=plt.cm.binary, interpolation="nearest")
        plt.xticks([]), plt.yticks([])
        plt.show()

    def evaluate_solution(self, solution):
        """Evaluates to true or false a given sequence"""
        if solution[0] != self.entrance or solution[-1] != self.exit:
            return False
        if len(solution) != len(set(solution)):
            return False
        for i in range(1, len(solution)):
            if (solution[i], solution[i - 1]) not in self.adjacency_list and (
                solution[i - 1],
                solution[i],
            ) not in self.adjacency_list:
                return False
        return True

    def bfs(self,graph, s, e):
        """Breadth-first search from s to e in a graph which is the adjacency_map"""
        frontier = deque()  # search front 
        frontier.append(s)
        visited = set()    # visited vertex
        visited.add(s)
        prev = {s: None}    #for each vertex, the previous vertex
        while frontier:
            current_node = frontier.popleft()    # front becomes the current node
            for next_node in graph[current_node]:
                if not next_node in visited:
                    frontier.append(next_node)  # next_node is added to front and then to visited nodes
                    visited.add(next_node)
                    prev[next_node] = current_node
    
        # construction of the path from e to s
        path = []
        at = e
        while at != None:
            path.append(at)
            at = prev[at]

        # reverse of the path to emerge the path from s to e
        path = path[::-1]

        # if s and e are connected then return the path
        if path[0] == s:
            return path
        
        return []  # return path as a list


if __name__ == "__main__":
    m1 = Maze(length=10, height=10)  # create an object m1 of class Maze
    print("Maze's information:\n")
    print(f"Maze's length is: {m1.length}")
    print(f"Maze's heigth is: {m1.height}")
    print(f"Maze's entrance is in: {m1._entrance_direction}, {m1.entrance}")
    print(f"Maze's exit is in: {m1._exit_direction}, {m1.exit}\n")
    print(f"Adjacency list for maze is: \n{m1.adjacency_list}\n")  # shows graph as adjacency list
    print(f"Adjacency map for maze is: \n{m1.adjacency_map}\n")  # shows graph as adjacency map
    print("Maze's sortest path with BFS is:")
    print(m1.bfs(graph = m1.adjacency_map, s = m1.entrance, e = m1.exit))  # shows the fastest path with bfs 
    m1.visualize_maze()  # shows maze with matplotlib
    m1.evaluate_solution([])   # shows if the given sequence is true or false