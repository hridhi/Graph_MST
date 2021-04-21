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
def main(source,destination):
    g7 = d.Graph(9)
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		  [4, 0, 8, 0, 0, 0, 0, 11, 0],
		  [0, 8, 0, 7, 0, 4, 0, 0, 2],
		  [0, 0, 7, 0, 9, 14, 0, 0, 0],
		  [0, 0, 0, 9, 0, 10, 0, 0, 0],
		  [0, 0, 4, 14, 10, 0, 2, 0, 0],
		  [0, 0, 0, 0, 0, 2, 0, 1, 6],
		  [8, 11, 0, 0, 0, 0, 1, 0, 7],
		  [0, 0, 2, 0, 0, 0, 6, 7, 0]
		  ];
    g7.addEdge(0,1,4)
    g7.addEdge(0,7,8)
    g7.addEdge(1,0,4)
    g7.addEdge(1,2,8)
    g7.addEdge(1,7,11)
    g7.addEdge(2,1,8)
    g7.addEdge(2,3,7)
    g7.addEdge(2,5,4)
    g7.addEdge(2,8,2)
    g7.addEdge(3,2,7)
    g7.addEdge(3,4,9)
    g7.addEdge(3,5,14)
    g7.addEdge(4,3,9)
    g7.addEdge(4,5,10)
    g7.addEdge(5,2,4)
    g7.addEdge(5,3,14)
    g7.addEdge(5,4,10)
    g7.addEdge(5,6,2)
    g7.addEdge(6,5,2)
    g7.addEdge(6,7,1)
    g7.addEdge(6,8,6)
    g7.addEdge(7,0,8)
    g7.addEdge(7,1,11)
    g7.addEdge(7,6,1)
    g7.addEdge(7,8,7)
    g7.addEdge(8,2,2)
    g7.addEdge(8,6,6)
    g7.addEdge(8,7,7)
    g7.visualize1({0:(0,0),1:(2,2),2:(4,2),3:(6,2),4:(8,0),5:(6,-2),6:(4,-2),7:(2,-2),8:(4,0)})
    result=[(0,1),(0,7),(1,2),(7,6),(2,8),(6,5),(2,3),(5,4)]
    x=g7.dijkstra(graph, int(source), int(destination))
    images11=[]
    G7=nx.Graph()
    G7.add_edges_from(result) 
    p7=nx.Graph()
    p7.add_edges_from([(0,1),(0,7),(1,0),(1,2),(1,7),(2,1),(2,3),(2,5),(2,8),(3,2),(3,4),(3,5),(4,3),(4,5),(5,2),(5,3),(5,4),(5,6),(6,5),(6,7),(6,8),(7,0),(7,1),(7,6),(7,8),(8,2),(8,6),(8,7)])
    fixed_positions = {0:(0,0),1:(2,2),2:(4,2),3:(6,2),4:(8,0),5:(6,-2),6:(4,-2),7:(2,-2),8:(4,0)}
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G7,pos=fixed_positions,fixed = fixed_nodes)
    labels =nx.get_edge_attributes(G7,'weight')
    for i in range(len(x)):
        nx.draw_networkx_edge_labels(g7,pos,edge_labels=labels)
        nx.draw_networkx_nodes(G7, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
        nx.draw_networkx_edges(G7,pos,edgelist=[(x[i][0],x[i][1])], alpha=0.5,width=3.5,edge_color="r")
        nx.draw(p7,pos,with_labels=True)
        plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\dij4.png")
        images11.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\dij4.png"))
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\dijgif4.gif",images11)
    gif8=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\dijgif4.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowdijgif4.gif",gif8,fps=1)
    plt.clf()
    return 


