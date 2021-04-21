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

class Kruskal:
    
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = [] 
        self.visual=[] 
    def addEdge(self, u, v, w):
        temp = [u, v,w] 
        self.visual.append(temp)
        self.graph.append([u, v, w])
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
        return True
    
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

    def KruskalMST(self):
        result = [] 
        i = 0  
        e = 0 
        self.graph = sorted(self.graph,key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
			       
        minimumCost = 0
        res=[]
        for u, v, weight in result:
            res.append([u,v,weight])
            minimumCost += weight
        return res
    def fixx(self,vertices):
        if(int(vertices)==1):
            fixed_positions = {0:(-2,-3)}
        elif(int(vertices)==2):
            fixed_positions = {1:(5,-3),0:(-2,-3)}
        elif(int(vertices)==3):
            fixed_positions = {1:(5,-3),2:(6,2),0:(-2,-3)}
        elif(int(vertices)==4):
            fixed_positions = {1:(5,-3),2:(6,2),3:(1,-5),0:(-2,-3)}
        elif(int(vertices)==5):
            fixed_positions = {1:(5,-3),2:(6,2),3:(1,-5),0:(-2,-3),4:(0,2)}
        elif(int(vertices)==6):
            fixed_positions = {1:(5,-3),2:(6,2),3:(1,-5),0:(-2,-3),4:(0,2),5:(4,4)}
        elif(int(vertices)==7):
            fixed_positions = {1:(5,-3),2:(6,2),3:(1,-5),0:(-2,-3),4:(0,2),5:(4,4),6:(-5,2)}
        elif(int(vertices)==8):
            fixed_positions = {1:(5,-3),2:(6,2),3:(1,-5),0:(-2,-3),4:(0,2),5:(4,4),6:(-5,2),7:(0,2)}
        return fixed_positions

