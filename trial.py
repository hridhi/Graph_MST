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
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField  
from wtforms import validators, ValidationError  

def kruskal1(vertices,edges,edgelist):
    g4 = k.Kruskal(int(vertices))
    temp=edgelist.split(",")
    addedgesfromlist=[]
    for i in range(int(edges)):
        x=temp[i].split(" ")
        addedgesfromtuple=(int(x[0]),int(x[1]))
        addedgesfromlist.append(addedgesfromtuple)
        g4.addEdge(int(x[0]),int(x[1]),int(x[2]))
    g4.visualize1(g4.fixx(vertices))
    result=g4.KruskalMST()
    G4=nx.Graph()
    n=len(result)
    finlist=[]
    for i in range(n):
        Tup = (result[i][0],result[i][1])
        finlist.append(Tup)

    G4.add_edges_from(finlist) 
    p4=nx.Graph()
    p4.add_edges_from(addedgesfromlist)
    fixed_positions = g4.fixx(vertices)
    fixed_nodes = fixed_positions.keys()
    pos = nx.spring_layout(G4,pos=fixed_positions, fixed = fixed_nodes)
    images4=[]
    labels =nx.get_edge_attributes(G4,'weight')
    for i in range(len(result)):
        nx.draw_networkx_edge_labels(g4,pos,edge_labels=labels)
        nx.draw_networkx_nodes(G4, pos, cmap=plt.get_cmap('jet'), node_size=150, alpha=0.5)
        nx.draw_networkx_edges(G4,pos,edgelist=[(result[i][0],result[i][1])], alpha=0.5,width=3.5,edge_color="r")
        nx.draw(p4,pos,with_labels=True)
        plt.savefig("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi10.png")
        images4.append(imageio.imread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi10.png"))
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi10gif.gif",images4)
    gif4=imageio.mimread("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\jalebi10gif.gif")
    imageio.mimsave("C:\\Users\\HRIDHI SETHI\\Documents\\openlab\\static\\images\\slowjalebi10gif.gif",gif4,fps=1)
    plt.clf()
    return 