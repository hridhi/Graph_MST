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
def kruskal3():
    g6= k.Kruskal(5)  
    g6.addEdge(0,1,5)
    g6.addEdge(0,2,5)
    g6.addEdge(0,4,5)
    g6.addEdge(1,0,5)
    g6.addEdge(1,3,3)
    g6.addEdge(2,0,5)
    g6.addEdge(2,3,4)
    g6.addEdge(2,4,6)
    g6.addEdge(3,1,3)
    g6.addEdge(3,2,4)
    g6.addEdge(4,0,5)
    g6.addEdge(4,2,6)
    g6.visualize1({1:(2,-2),2:(-1,2),3:(1,-3),0:(-1,-3),4:(3,4)})
    result=g6.KruskalMST()
    G6=nx.Graph()
    G6.add_edges_from([(1,3),(2,3),(0,1),(0,4)]) 
    p6=nx.Graph()
    p6.add_edges_from([(0,1),(0,2),(0,4),(1,0),(1,3),(2,0),(2,3),(2,4),(3,1),(3,2),(4,0),(4,2)])
    fixed_positions = {1:(2,-2),2:(-1,2),3:(1,-3),0:(-1,-3),4:(3,4)}
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G6,pos=fixed_positions, fixed = fixed_nodes)
    images6=[]
    labels =nx.get_edge_attributes(G6,'weight')
    for i in range(len(result)):
        nx.draw_networkx_edge_labels(g6,pos,edge_labels=labels)
        nx.draw_networkx_nodes(G6, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
        nx.draw_networkx_edges(G6,pos,edgelist=[(result[i][0],result[i][1])], alpha=0.5,width=3.5,edge_color="r")
        nx.draw(p6,pos,with_labels=True)
        plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi9.png")
        images6.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi9.png"))
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi9gif.gif",images6)
    gif6=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi9gif.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowjalebi9gif.gif",gif6,fps=1)
    plt.clf()
    return 
