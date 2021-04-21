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
def prims1():
    g8 = Prims.Prims(5) 
    g8.graph =[ [0, 2, 0, 6, 0], 
			[2, 0, 3, 8, 5], 
			[0, 3, 0, 0, 7], 
			[6, 8, 0, 0, 9], 
			[0, 5, 7, 9, 0]] 
    g8.addEdge(0,1,2)
    g8.addEdge(0,3,6)
    g8.addEdge(1,0,2)
    g8.addEdge(1,2,3)
    g8.addEdge(1,3,8)
    g8.addEdge(1,4,5)
    g8.addEdge(2,1,3)
    g8.addEdge(2,4,7)
    g8.addEdge(3,0,6)
    g8.addEdge(3,1,8)
    g8.addEdge(3,4,9)
    g8.addEdge(4,1,5)
    g8.addEdge(4,2,7)

    g8.visualize1({1:(1,0),2:(-1,2),3:(1,-3),4:(2,2),0:(-1,-3)})
    result=[(0,1),(1,2),(1,4),(0,3)]
   
    G8=nx.Graph()
    G8.add_edges_from([(0,1),(1,2),(1,4),(0,3)]) 
    p8=nx.Graph()
    p8.add_edges_from([(0,1),(0,3),(1,0),(1,2),(1,3),(1,4),(2,1),(2,4),(3,0),(3,1),(3,4),(4,1),(4,2)])
    fixed_positions = {1:(1,0),2:(-1,2),3:(1,-3),4:(2,2),0:(-1,-3)}
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G8,pos=fixed_positions,fixed = fixed_nodes)
    images13=[]
    labels =nx.get_edge_attributes(G8,'weight')
    for i in range(len(result)):
       nx.draw_networkx_edge_labels(g8,pos,edge_labels=labels)
       nx.draw_networkx_nodes(G8, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
       nx.draw_networkx_edges(G8,pos,edgelist=[(result[i][0],result[i][1])], alpha=0.5,width=3.5,edge_color="r")
       nx.draw(p8,pos,with_labels=True)
       plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi4.png")
       images13.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi4.png"))
    
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi4gif.gif",images13)
    gif8=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi4gif.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowjalebi4gif.gif",gif8,fps=1)
    plt.clf()

    return
