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

class Prims(): 

    def __init__(self, vertices): 
        self.V = vertices  
        self.graph1 = [[0 for column in range(vertices)] for row in range(vertices)]
        self.res=[]  
        self.visual = []
    def printMST(self, parent): 
        for i in range(self.V-1): 
            self.res.append([parent[i],parent[i+1],self.graph1[parent[i]][parent[i+1]] ])
    def addEdge(self, a, b,c): 
        temp = [a,b,c] 
        self.graph1[a][b]=c
        self.graph1[b][a]=c
        self.visual.append(temp) 
    def minKey(self, key, mstSet): 
        min = 99999 
        min_index=0
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
        return min_index 
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
    def primMST(self): 
        key = [99999] * self.V 
        parent = [None] * self.V  
        key[0] = 0 
        mstSet = [False] * self.V  
        parent[0] = -1 
        cheating=[]
        
        for cout in range(self.V):  
            u = self.minKey(key, mstSet) 
            cheating.append(u)
            
            mstSet[u] = True 
            for v in range(self.V):
                
                if self.graph1[u][v] > 0 and mstSet[v] == False and key[v] > self.graph1[u][v]: #checking 3 condition => if has edge , if visited node , if distance is mimimun 
                    key[v] = self.graph1[u][v] 
                    parent[v] = u 
                    
        
        self.printMST(cheating)
        
        return(self.res)