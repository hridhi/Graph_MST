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
def kruskal2():
    g5 = k.Kruskal(5) 
    g5.addEdge(0,1,2)
    g5.addEdge(0,3,6)
    g5.addEdge(1,0,2)
    g5.addEdge(1,2,3)
    g5.addEdge(1,3,8)
    g5.addEdge(1,4,5)
    g5.addEdge(2,1,3)
    g5.addEdge(2,4,7)
    g5.addEdge(3,0,6)
    g5.addEdge(3,1,8)
    g5.addEdge(3,4,9)
    g5.addEdge(4,1,5)
    g5.addEdge(4,2,7)

    g5.visualize1({1:(1,0),2:(-1,2),3:(1,-3),0:(-1,-3),4:(3,4)})
    result=g5.KruskalMST()
    G5=nx.Graph()
    G5.add_edges_from([(0,1),(1,2),(1,4),(0,3)]) 
    p5=nx.Graph()
    p5.add_edges_from([(0,1),(1,0),(0,3),(1,2),(1,3),(1,4),(2,1),(2,4),(3,0),(3,1),(3,4),(4,1),(4,2)])
    fixed_positions = {1:(1,0),2:(-1,2),3:(1,-3),0:(-1,-3),4:(3,4)}
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G5,pos=fixed_positions, fixed = fixed_nodes)
    images5=[]
    labels =nx.get_edge_attributes(G5,'weight')
    for i in range(len(result)):
        nx.draw_networkx_edge_labels(g5,pos,edge_labels=labels)
        nx.draw_networkx_nodes(G5, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
        nx.draw_networkx_edges(G5,pos,edgelist=[(result[i][0],result[i][1])], alpha=0.5,width=3.5,edge_color="r")
        nx.draw(p5,pos,with_labels=True)
        plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi10.png")
        images5.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi10.png"))
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi10gif.gif",images5)
    gif5=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi10gif.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowjalebi10gif.gif",gif5,fps=1)
    plt.clf()
    return 
