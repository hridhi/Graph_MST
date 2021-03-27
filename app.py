from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
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
import prims1 as p1;
import prims2 as p2;
import prims3 as p3;
import kruskal1 as k1;
import kruskal2 as k2;
import kruskal3 as k3;
from flask import Markup
PEOPLE_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
@app.route("/")
def view_home():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'add.gif')
    img1 = os.path.join(app.config['UPLOAD_FOLDER'], '1stgraph.png')
    img2 = os.path.join(app.config['UPLOAD_FOLDER'], '2ndgraph.png')
    img3 = os.path.join(app.config['UPLOAD_FOLDER'], 'directed.png')
    img4 = os.path.join(app.config['UPLOAD_FOLDER'], 'undirected.png')
    img5 = os.path.join(app.config['UPLOAD_FOLDER'], 'adjancencymatrix.png')
    img6 = os.path.join(app.config['UPLOAD_FOLDER'], 'adjlistgraph.png')
    img7 = os.path.join(app.config['UPLOAD_FOLDER'], 'adjlist.png')
    return render_template("index.html",title="Graph",img=full_filename,img1=img1,img2=img2,img3=img3,img4=img4,img5=img5,img6=img6,img7=img7)

@app.route("/first")
def view_prims():
    text= Markup("1) Create a set mstSet that keeps track of vertices already included in MST.<br> 2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE. Assign key value as 0 for the first vertex so that it is picked first.<br> 3) While mstSet doesn’t include all vertices <br>a) Pick a vertex u which is not there in mstSet and has minimum key value.<br> b) Include u to mstSet. <br>c) Update key value of all adjacent vertices of u. <br>To update the key values, iterate through all adjacent vertices. For every adjacent vertex v, if weight of edge u-v is less than the previous key value of v, update the key value as weight of u-v The idea of using key values is to pick the minimum weight edge from cut. The key values are used only for vertices which are not yet included in MST, the key value for these vertices indicate the minimum weight edges connecting them to the set of vertices included in MST. ")
    return render_template("MST.html",title="Prims Algorithm",req1='view_prims1',req2='view_prims2',req3='view_prims3',text=text)
@app.route("/prims1")
def view_prims1():
    p1.prims1()
    text= Markup('<h3>Step1:</h3> <br> Mstset = { } <br> ')
    img1=os.path.join(app.config['UPLOAD_FOLDER'], 'p11.PNG')
    img2=os.path.join(app.config['UPLOAD_FOLDER'], 'p12.PNG')
    text1=Markup('<h3>ITERATION – 1:</h3><br><h5>Step3:</h5><br>a) As min key vertex is vertex-0 and it is not included in Mstset hence add it to mstset <br> b)Adding vertex value to mstset<br>&nbsp;&nbsp;&nbsp;&nbsp;mstset = { 0 }<br>c) Updating the key values<br>&nbsp;&nbsp;&nbsp;&nbsp;if(weight(u,v) < v.key):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;v.key = weight(u,v)<br>For edge (0 – 1):<br>&nbsp;&nbsp;&nbsp;2 < ∞ <br>Hence update key of vertex 1 with 2 <br> And for edge (0 – 3): <br>&nbsp;&nbsp;&nbsp;6<∞<br>Hence update key of vertex2 with 6')
    text2=Markup('<h3>ITERATION – 2:<h3><br><h5>STEP – 3 :</h5><br>a) As min key is with vertex1 and not included in mstset hence add it to mstset<br>b) mstset = { 0 , 1 }<br>c) For edge (1 – 2)<br>&nbsp;&nbsp;&nbsp;3 < ∞<br>Hence update key of vertex 2 with 3 <br> For edge (1 – 3): <br>&nbsp;&nbsp;&nbsp;8 > 6<br>Hence no updation required <br> For edge (1 – 4) <br>&nbsp;&nbsp;&nbsp; 5 < ∞<br>Hence update the key of vertex 4 with 5')
    img3=os.path.join(app.config['UPLOAD_FOLDER'], 'p13.PNG')
    text3=Markup('<h3>ITERATION – 3:</h3><br><h5>Step-3:</h5><br>a) The vertex2 is the vertex with is with minimum key and not selected yet.so add it to mst set<br>b) mstset = {​​​​​ 0 , 1 , 2 }<br>​​​​c) For edge (2 – 4):<br>&nbsp;&nbsp;&nbsp;7 > 5<br>     Hence no updation required')
    text4=Markup('<h3> ITERATION – 4:</h3><br><h5>Step -3:</h5>a) The vertex4 is the vertex with minimum key value and not selected yet. So add it to mst set<br>b) mstset = {​​​​​ 0, 1, 2, 4}<br>c) For edge ( 4 – 3)<br>&nbsp;&nbsp;&nbsp;6 == 6<br>Hence no updation required')
    text5=Markup('Add vertex3 into mst set as it is the remaining vertex and our MST is ready')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowgif5.gif')
    return render_template("MST.html",text4=text4,text5=text5,img2=img2,img3=img3, text3=text3,title="Prims Algorithm",text=text,text1=text1,text2=text2,img=full_filename,req1='view_prims1',req2='view_prims2',req3='view_prims3',img1=img1) 
@app.route("/prims2")
def view_prims2():
    p2.prims2()
    text=Markup('There are totally 7 nodes and 9 edges. Considering  the Prims algorithm, the the minimum spanning tree is formed as follows:')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowgif11.gif')
    return render_template("MST.html",text=text, title="Prims Algorithm",img=full_filename,req1='view_prims1',req2='view_prims2',req3='view_prims3') 
@app.route("/prims3")
def view_prims3():
    p3.prims3()
    text=Markup('There are totally 5 nodes and 6 edges. Considering  the Prims algorithm, the the minimum spanning tree is formed as follows:')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowgif4.gif')
    return render_template("MST.html", text=text,title="Prims Algorithm",img=full_filename,req1='view_prims1',req2='view_prims2',req3='view_prims3') 

@app.route("/second")
def view_Kruskal():
    text=Markup('<h3>Minimum spanning tree:</h3>Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together. A single graph can have many different spanning trees. A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree with weight less than or equal to the weight of every other spanning tree. The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.A minimum spanning tree has (V – 1) edges where V is the number of vertices in the given graph.One of the minimum spanning tree algorithms is  Kruskal’s Minimum Spanning Tree Algorithm.<br><br><h3>KRUSKAL:</h3><br><h5>Algorithm:</h5><br>1.Sort all the edges in non-decreasing order of their weight. <br>2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. <br>3. Repeat step 2 until there are (V-1) edges in the spanning tree.')
    return render_template("MST.html",title="Kruskals Algorithm",req1='view_kruskal1',req2='view_kruskal2',req3='view_kruskal3',text=text)

@app.route("/kruskal1")
def view_kruskal1():
    k1.kruskal1()
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowgif1.gif')
    return render_template("MST.html", title="Kruskal Algorithm",img=full_filename,req1='view_kruskal1',req2='view_kruskal2',req3='view_kruskal3') 
@app.route("/kruskal2")
def view_kruskal2():
    k2.kruskal2()
    text=Markup('There are totally 5 nodes and 7 edges. Considering  the Kruskals algorithm, the the minimum spanning tree is formed as follows:')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowgif12.gif')
    return render_template("MST.html",text=text, title="Kruskal Algorithm",img=full_filename,req1='view_kruskal1',req2='view_kruskal2',req3='view_kruskal3') 
@app.route("/kruskal3")
def view_kruskal3():
    k3.kruskal3()
    text=Markup('There are totally 5 nodes and 6 edges. Considering  the Kruskals algorithm, the the minimum spanning tree is formed as follows:')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowgif14.gif')
    return render_template("MST.html",text=text, title="Kruskal Algorithm",img=full_filename,req1='view_kruskal1',req2='view_kruskal2',req3='view_kruskal3') 









if __name__ == "__main__":
    app.run(debug=True)


