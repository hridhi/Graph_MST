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
import kruskal as k;

def kruskal1():
    g4 = k.Kruskal(4)   
    g4.addEdge(0, 1, 10)
    g4.addEdge(0, 2, 6)
    g4.addEdge(0, 3, 5)
    g4.addEdge(1, 3, 15)
    g4.addEdge(2, 3, 4)
    g4.visualize1({1:(1,0),2:(-1,2),3:(1,-3),0:(-1,-3)})
    result=g4.KruskalMST()
    G4=nx.Graph()
    G4.add_edges_from([(2,3),(0,3),(0,1)]) 
    p4=nx.Graph()
    p4.add_edges_from([(0,1),(0,2),(0,3),(1,3),(2,3)])
    fixed_positions = {1:(1,0),2:(-1,2),3:(1,-3),0:(-1,-3)}
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G4,pos=fixed_positions, fixed = fixed_nodes)
    images4=[]
    labels =nx.get_edge_attributes(G4,'weight')
    for i in range(len(result)):
        nx.draw_networkx_edge_labels(g4,pos,edge_labels=labels)
        nx.draw_networkx_nodes(G4, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
        nx.draw_networkx_edges(G4,pos,edgelist=[(result[i][0],result[i][1])], alpha=0.5,width=3.5,edge_color="r")
        nx.draw(p4,pos,with_labels=True)
        plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi7.png")
        images4.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi7.png"))
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi7gif.gif",images4)
    gif4=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi7gif.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowjalebi7gif.gif",gif4,fps=1)
    plt.clf()
    return 
