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

def prims3():
    g3 = Prims.Prims(5) 
    g3.graph =[ [0, 5, 5, 0, 5], 
			[5, 0, 0, 3, 0], 
			[5, 0, 0, 4, 6], 
			[0, 3, 4, 0, 0], 
			[5, 0, 6, 0, 0]] 
    g3.addEdge(0,1,5)
    g3.addEdge(0,2,5)
    g3.addEdge(0,4,5)
    g3.addEdge(1,0,5)
    g3.addEdge(1,3,3)
    g3.addEdge(2,0,5)
    g3.addEdge(2,3,4)
    g3.addEdge(2,4,6)
    g3.addEdge(3,1,3)
    g3.addEdge(3,2,4)
    g3.addEdge(4,0,5)
    g3.addEdge(4,2,6)


    g3.visualize1({1:(1,0),2:(-1,2),3:(1,-3),4:(2,2),0:(-1,-3)})
    result=[(0,1),(1,3),(3,2),(0,4)]
    G3=nx.Graph()
    G3.add_edges_from([(0,1),(1,3),(3,2),(0,4)]) 
    p3=nx.Graph()
    p3.add_edges_from([(0,1),(0,2),(0,4),(1,0),(1,3),(2,0),(2,3),(2,4),(3,1),(3,2),(4,0),(4,2)])
    fixed_positions = {1:(1,0),2:(-1,2),3:(1,-3),4:(2,2),0:(-1,-3)}
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G3,pos=fixed_positions,fixed = fixed_nodes)
    images3=[]
    labels =nx.get_edge_attributes(G3,'weight')
    for i in range(len(result)):
       nx.draw_networkx_edge_labels(g3,pos,edge_labels=labels)
       nx.draw_networkx_nodes(G3, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
       nx.draw_networkx_edges(G3,pos,edgelist=[(result[i][0],result[i][1])], alpha=0.5,width=3.5,edge_color="r")
       nx.draw(p3,pos,with_labels=True)
       plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi6.png")
       images3.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi6.png"))
    
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi6gif.gif",images3)
    gif3=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi6gif.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowjalebi6gif.gif",gif3,fps=1)
    plt.clf()
    return 
