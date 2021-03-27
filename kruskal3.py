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
        self.V = vertices#num of vertices 
        self.graph = [] #edge list 
        self.visual=[] 

	# function to add an edge to graph
    def addEdge(self, u, v, w):
        temp = [u, v,w] 
        self.visual.append(temp)
        self.graph.append([u, v, w])

    #recursively finding the parent 
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    #union by rank 
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
		# Attach smaller rank tree under root of
		# high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
		# If ranks are same, then make one as root
		# and increment its rank by one
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
        return True
    
    def visualize1(self): #for the initial graph 
        g= nx.Graph() #initialzing 
        fixed_positions = {1:(2,-2),2:(-1,2),3:(1,-3),4:(2,2),0:(-1,-3),4:(3,4)} 
        for i in range(self.V):
            g.add_node(i,pos=fixed_positions[i])
        n=len(self.visual)
        for i in range(n):
            g.add_edge(self.visual[i][0],self.visual[i][1],weight=self.visual[i][2])#visual edge list 
        pos =nx.get_node_attributes(g,'pos')
        labels =nx.get_edge_attributes(g,'weight')

        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
        nx.draw(g,pos,with_labels=True)
        plt.show()

    def visualize2(self,res): #for the result 
        n=len(res)
        g=nx.Graph()
        temp=[] #picking all the unique nodes for defining 
        for i in range(n):
            g.add_edge(res[i][0],res[i][1],weight=res[i][2])
            if(res[i][0] not in temp and res[i][1] not in temp):
                temp.append(res[i][0])
                temp.append(res[i][1])
            elif(res[i][0] not in temp and res[i][1] in temp):
                temp.append(res[i][0])
            elif(res[i][0] in temp and res[i][1] not in temp):
                temp.append(res[i][1])
        m=len(temp)
        fixed_positions = {0:(-1,-3),1:(2,-2),2:(-1,2),3:(1,-3),4:(3,4)}
        for i in range(m):
            g.add_node(temp[i],pos=fixed_positions[i]) 

        pos =nx.get_node_attributes(g,'pos')
        labels =nx.get_edge_attributes(g,'weight')

        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
        nx.draw(g,pos,with_labels=True)
        plt.show()

    def KruskalMST(self):
        result = [] #resultant MST
        i = 0 #graph looping 
        e = 0 #resultant array looping
        #sorting array according to weight
        self.graph = sorted(self.graph,key=lambda item: item[2])
        parent = []
        rank = []
        #initialization , appending each node as its own parent and setting rank as 0 
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
		# Kruskals contains V-1 edges 
        while e < self.V - 1:
			# start,end,weight
            u, v, w = self.graph[i]
            i = i + 1
            #storing parent
            x = self.find(parent, u)
            y = self.find(parent, v)
			#cycle detecting
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
			      # Else discarding the edge

      #finally printing the result 
        minimumCost = 0
        print ("Edges in the constructed MST")
        res=[]
        for u, v, weight in result:
            res.append([u,v,weight])
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree" , minimumCost)
        return res


def kruskal3():
    g = Kruskal(5)  
    g.addEdge(0,1,5)
    g.addEdge(0,2,5)
    g.addEdge(0,4,5)
    g.addEdge(1,0,5)
    g.addEdge(1,3,3)
    g.addEdge(2,0,5)
    g.addEdge(2,3,4)
    g.addEdge(2,4,6)
    g.addEdge(3,1,3)
    g.addEdge(3,2,4)
    g.addEdge(4,0,5)
    g.addEdge(4,2,6)
    g.visualize1()
    result=g.KruskalMST()
    print(result)
    G=nx.Graph()
  #[[1, 3, 3], [2, 3, 4], [0, 1, 5], [0, 4, 5]]
    G.add_edges_from([(1,3),(2,3),(0,1),(0,4)]) 
    p=nx.Graph()
    p.add_edges_from([(0,1),(0,2),(0,4),(1,0),(1,3),(2,0),(2,3),(2,4),(3,1),(3,2),(4,0),(4,2)])
    fixed_positions = {1:(2,-2),2:(-1,2),3:(1,-3),0:(-1,-3),4:(3,4)}
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G,pos=fixed_positions, fixed = fixed_nodes)
    images=[]
    labels =nx.get_edge_attributes(G,'weight')
    for i in range(len(result)):
        nx.draw_networkx_edge_labels(g,pos,edge_labels=labels)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
        nx.draw_networkx_edges(G,pos,edgelist=[(result[i][0],result[i][1])], alpha=0.5,width=3.5,edge_color="r")
        nx.draw(p,pos,with_labels=True)
        plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\orig1.png")
        images.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\orig1.png"))
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\originalgif1.gif",images)
    gif=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\originalgif1.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowgif14.gif",gif,fps=1)
    return 