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
import dijsktras as d;
import kruskal as k;
def main(vertices,edges,edgelist,source,destination):
    g90 = k.Kruskal(int(vertices))
    g7 = d.Graph(int(vertices))
    temp=edgelist.split(",")
    addedgesfromlist=[]
    addedgeslist=[]
    for i in range(int(edges)):
        x=temp[i].split(" ")
        addedgesfromtuple=[int(x[0]),int(x[1]),int(x[2])]
        addedges=[int(x[0]),int(x[1])]
        addedgesfromlist.append(addedgesfromtuple)
        addedgeslist.append(addedges)
        g7.addEdge(int(x[0]),int(x[1]),int(x[2]))
        
       
      
    adjacency = [[0]*int(vertices) for _ in range(int(vertices))]
    for sink, source1,weight in addedgesfromlist:
        adjacency[sink][source1] =weight 
        adjacency[source1][sink] =weight 
        
    
    g7.graph=adjacency


    x=g7.dijkstra(adjacency,source,destination)
    g7.visualize1(g90.fixx(vertices))
    G7=nx.Graph()
    finlist=x
    result=x
    finlist=[(0, 5), (2, 3), (1, 6), (1, 2), (3, 4), (4, 5)]
    result=x
    G7.add_edges_from(finlist) 
    p7=nx.Graph()
    p7.add_edges_from(addedgeslist)
    fixed_positions = g90.fixx(int(vertices))
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G7,pos=fixed_positions,fixed = fixed_nodes)
    images11=[]
    labels =nx.get_edge_attributes(G7,'weight')
    for i in range(len(result)):
        nx.draw_networkx_edge_labels(g7,pos,edge_labels=labels)
        nx.draw_networkx_nodes(G7, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
        nx.draw_networkx_edges(G7,pos,edgelist=[(result[i][0],result[i][1])], alpha=0.5,width=3.5,edge_color="r")
        nx.draw(p7,pos,with_labels=True)
        plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\dij4.png")
        images11.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\dij4.png"))
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\dijgif4.gif",images11)
    gif8=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\dijgif4.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowdijgif4.gif",gif8,fps=1)
    plt.clf()
    return 
