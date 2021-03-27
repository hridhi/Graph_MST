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
        self.V = vertices  #num of vertices 
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)] #adjacency matrix 
        self.res=[] #resultant 
        self.visual = []

    #printing the MST
    def printMST(self, parent): 
        print( "Edge \tWeight")
        for i in range(1, self.V): 
            print( parent[i], "-", i, "\t", self.graph[i][ parent[i] ])
            self.res.append([parent[i],i,self.graph[i][ parent[i]] ])
        
    #Adding edges in the graph 
    def addEdge(self, a, b,c): 
        temp = [a, b,c] 
        self.visual.append(temp) 

    #to get the minimum distance edge node
    def minKey(self, key, mstSet): 
        min = 99999 
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
        return min_index 

    def visualize1(self): # for the initial graph 
        g= nx.Graph() 
        fixed_positions = {1:(-2,-1),2:(-1,2),3:(1,-3),4:(2,2),0:(-1,-3),5:(1,3),6:(-2,3)} 
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

    def visualize2(self,res): # for the result 
        n=len(res)
        g=nx.Graph()
        temp=[]
        for i in range(n):
            g.add_edge(res[i][0],res[i][1],weight=res[i][2])
            if(res[i][0] not in temp and res[i][1] not in temp):
                temp.append(res[i][0])
                temp.append(res[i][1])
            elif(res[i][0] not in temp and res[i][1] in temp):
                temp.append(res[i][0])
            if(res[i][0] in temp and res[i][1] not in temp):
                temp.append(res[i][1])
        m=len(temp)
        fixed_positions = {1:(-2,-1),2:(-1,2),3:(1,-3),4:(2,2),0:(-1,-3),5:(1,3),6:(-2,3)}
        for i in range(m):
            g.add_node(temp[i],pos=fixed_positions[i]) 

        pos =nx.get_node_attributes(g,'pos')
        labels =nx.get_edge_attributes(g,'weight')

        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
        nx.draw(g,pos,with_labels=True)
        plt.show()

    def primMST(self): 
        key = [99999] * self.V #instead of infinity
        parent = [None] * self.V # to check from where did we come to the current node 
        key[0] = 0 #for picking 0 in first hand 
        mstSet = [False] * self.V  # to check if node visited or not
        parent[0] = -1 # First node is always the root
        for cout in range(self.V):  
            u = self.minKey(key, mstSet) #pick the minimum distance 
            mstSet[u] = True #putting the node as visited 
            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: #checking 3 condition => if has edge , if visited node , if distance is mimimun 
                    key[v] = self.graph[u][v] 
                    parent[v] = u 
        #finally returning the result 
        self.printMST(parent)
        return(self.res)
        #return rest


def prims2():
    g = Prims(7) 
    g.graph =[ [0,28,0,0,0,10,0], 
			[28,0,16,0,0,0,14], 
			[0,16,0,12,0,0,0], 
			[0,0,12,22,0,0,18],

			[0,0,0,22,0,25,24],
            [10,0,0,0,25,0,0],
            [0,14,0,18,24,0,0]]
    g.addEdge(0,1,28)
    g.addEdge(0,5,10)
    g.addEdge(1,0,28)
    g.addEdge(1,2,16)
    g.addEdge(1,6,14)
    g.addEdge(2,1,16)
    g.addEdge(2,3,12)
    g.addEdge(3,2,12)
    g.addEdge(3,3,22)
    g.addEdge(3,6,18)
    g.addEdge(4,3,22)
    g.addEdge(4,5,25)
    g.addEdge(4,6,24)
    g.addEdge(5,0,10)
    g.addEdge(5,4,25)
    g.addEdge(6,1,14)
    g.addEdge(6,3,18)
    g.addEdge(6,4,24)
    print(g)
    g.visualize1()
    result=[[0, 5, 10],[5, 4, 25],[4, 3, 0],[3, 2, 12],[2, 1, 16], [1, 6, 14]];
    print(len(result))
    G=nx.Graph()
    #[[2, 1, 16], [3, 2, 12], [4, 3, 0], [5, 4, 25], [0, 5, 10], [1, 6, 14]]
    G.add_edges_from([(0,5),(5,4),(4,3),(3,2),(2,1),(1,6)]) 
    p=nx.Graph()
    p.add_edges_from([(0,1),(0,5),(1,0),(1,2),(1,6),(2,1),(2,3),(3,2),(3,3),(3,6),(4,3),(4,5),(4,6),(5,0),(5,4),(6,1),(6,3),(6,4)])
    fixed_positions = {1:(-2,-1),2:(-1,2),3:(1,-3),4:(2,2),0:(-1,-3),5:(1,3),6:(-2,3)}
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G,pos=fixed_positions,fixed = fixed_nodes)
    images=[]
    labels =nx.get_edge_attributes(G,'weight')
    for i in range(len(result)):
       nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
       nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
       nx.draw_networkx_edges(G,pos,edgelist=[(result[i][0],result[i][1])], alpha=0.5,width=3.5,edge_color="r")
       nx.draw(p,pos,with_labels=True)
       plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\orig.png")
       images.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\orig.png"))
    
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\originalgif.gif",images)
    gif=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\originalgif.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowgif11.gif",gif,fps=1)
    return 