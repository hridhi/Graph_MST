from collections import defaultdict
import networkx as nx 
from networkx.drawing.nx_agraph import graphviz_layout
import sys
import random
import imageio
import matplotlib
import os
matplotlib.use('Agg')
import matplotlib.pyplot as plt
class Graph:
    def __init__(self,vertices):
        self.visual=[]
        self.result=[]
        self.V=vertices
        self.graph=[None]
    def minDistance(self,dist,queue):
        minimum = float("Inf")
        min_index = -1
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index
    def printPath(self, parent, j):
        if parent[j] == -1 :
            self.result.append(j)
            return
        self.printPath(parent , parent[j])
        self.result.append(j)
    def printSolution(self, dist, parent,dest):
        src = 0
        x=[]
        for i in range(1, len(dist)):
            if(i==dest):
                x.append(self.printPath(parent,i))
        return x 
    def dijkstra(self, graph, src,dest):
        src=int(src)
        dest=int(dest)
        row = len(graph)
        col = len(graph[0])
        dist = [float("Inf")] * row
        parent = [-1] * row
        dist[src] = 0
        queue = []
        for i in range(row):
            queue.append(i)
        while queue:
            u = self.minDistance(dist,queue)
            queue.remove(u)
            for i in range(col):
                if graph[u][i] and i in queue:
                    if dist[u] + graph[u][i] < dist[i]:
                        dist[i] = dist[u] + graph[u][i]
                        parent[i] = u
        self.printSolution(dist,parent,dest)
        x=[]
        for i in range(len(self.result)-1):
            x.append((self.result[i],self.result[i+1]))
        return x
    def addEdge(self, a, b,c): 
        temp = [a, b,c] 
        self.visual.append(temp) 
    def visualize1(self,fixed_pos):  
        g= nx.Graph() 
        fixed_positions = fixed_pos 
        for i in range(self.V):
            g.add_node(i,pos=fixed_positions[i])
        n=len(self.visual)
        for i in range(n):
            g.add_edge(self.visual[i][0],self.visual[i][1],weight=self.visual[i][2])
        pos =nx.get_node_attributes(g,'pos')
        labels =nx.get_edge_attributes(g,'weight')
        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
        nx.draw(g,pos,with_labels=True)
        plt.show()