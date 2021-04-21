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
import kruskal as k;
import matplotlib.pyplot as plt
def prims1(vertices,edges,edgelist):
    g91 = k.Kruskal(int(vertices))
    g8 = Prims.Prims(int(vertices))
    temp=edgelist.split(",")
    addedgesfromlist=[]
    addedgeslist=[]
    for i in range(int(edges)):
        x=temp[i].split(" ")
        addedgesfromtuple=[int(x[0]),int(x[1]),int(x[2])]
        addedges=[int(x[0]),int(x[1])]
        addedgesfromlist.append(addedgesfromtuple)
        addedgeslist.append(addedges)
        g8.addEdge(int(x[0]),int(x[1]),int(x[2]))
        
       
      
    adjacency = [[0]*int(vertices) for _ in range(int(vertices))]
    for sink, source,weight in addedgesfromlist:
        adjacency[sink][source] =weight 
        adjacency[source][sink] =weight 
        
    
    g8.graph=adjacency

    
    
    g8.visualize1(g91.fixx(vertices))
    result=g8.primMST()

    n=len(result)
    finlist=[]
    for i in range(n):
        Tup = (result[i][0],result[i][1])
        finlist.append(Tup)
    G8=nx.Graph()
    G8.add_edges_from(finlist) 
    p8=nx.Graph()
    p8.add_edges_from(addedgeslist)
    fixed_positions = g91.fixx(int(vertices))
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