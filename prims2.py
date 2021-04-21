import prims as Prims;
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

def prims2():
    g9 = Prims.Prims(7) 
    g9.graph =[ [0,28,0,0,0,10,0], 
			[28,0,16,0,0,0,14], 
			[0,16,0,12,0,0,0], 
			[0,0,12,22,0,0,18],

			[0,0,0,22,0,25,24],
            [10,0,0,0,25,0,0],
            [0,14,0,18,24,0,0]]
    g9.addEdge(0,1,28)
    g9.addEdge(0,5,10)
    g9.addEdge(1,0,28)
    g9.addEdge(1,2,16)
    g9.addEdge(1,6,14)
    g9.addEdge(2,1,16)
    g9.addEdge(2,3,12)
    g9.addEdge(3,2,12)
    g9.addEdge(3,3,22)
    g9.addEdge(3,6,18)
    g9.addEdge(4,3,22)
    g9.addEdge(4,5,25)
    g9.addEdge(4,6,24)
    g9.addEdge(5,0,10)
    g9.addEdge(5,4,25)
    g9.addEdge(6,1,14)
    g9.addEdge(6,3,18)
    g9.addEdge(6,4,24)
    g9.visualize1({1:(-2,-1),2:(-1,2),3:(1,-3),4:(2,2),0:(-1,-3),5:(1,3),6:(-2,3)})
    result=[[0, 5, 10],[5, 4, 25],[4, 3, 0],[3, 2, 12],[2, 1, 16], [1, 6, 14]];
    G9=nx.Graph()
    G9.add_edges_from([(0,5),(5,4),(4,3),(3,2),(2,1),(1,6)]) 
    p9=nx.Graph()
    p9.add_edges_from([(0,1),(0,5),(1,0),(1,2),(1,6),(2,1),(2,3),(3,2),(3,3),(3,6),(4,3),(4,5),(4,6),(5,0),(5,4),(6,1),(6,3),(6,4)])
    fixed_positions = {1:(-2,-1),2:(-1,2),3:(1,-3),4:(2,2),0:(-1,-3),5:(1,3),6:(-2,3)}
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G9,pos=fixed_positions,fixed = fixed_nodes)
    images14=[]
    labels =nx.get_edge_attributes(G9,'weight')
    for i in range(len(result)):
       nx.draw_networkx_edge_labels(g9,pos,edge_labels=labels)
       nx.draw_networkx_nodes(G9, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
       nx.draw_networkx_edges(G9,pos,edgelist=[(result[i][0],result[i][1])], alpha=0.5,width=3.5,edge_color="r")
       nx.draw(p9,pos,with_labels=True)
       plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi5.png")
       images14.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi5.png"))
    
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi5gif.gif",images14)
    gif9=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi5gif.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowjalebi5gif.gif",gif9,fps=1)
    plt.clf()
    return 
