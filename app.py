from flask import Flask, render_template, request, jsonify, url_for, redirect
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
import dijsktras1 as d1;
import trial as t;
import trial2 as t2;
import trial3 as t3;
from flask import Markup
PEOPLE_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
vertices=0
edges=0
edgelist=[]
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
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowjalebi4gif.gif')
    return render_template("MST.html",text4=text4,text5=text5,img2=img2,img3=img3, text3=text3,title="Prims Algorithm",text=text,text1=text1,text2=text2,img=full_filename,req1='view_prims1',req2='view_prims2',req3='view_prims3',img1=img1) 
@app.route("/prims2")
def view_prims2():
    p2.prims2()
    text=Markup('There are totally 7 nodes and 9 edges. Considering  the Prims algorithm, the the minimum spanning tree is formed as follows:')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowjalebi5gif.gif')
    return render_template("MST.html",text=text, title="Prims Algorithm",img=full_filename,req1='view_prims1',req2='view_prims2',req3='view_prims3') 
@app.route("/prims3")
def view_prims3():
    p3.prims3()
    text=Markup('There are totally 5 nodes and 6 edges. Considering  the Prims algorithm, the the minimum spanning tree is formed as follows:')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowjalebi6gif.gif')
    return render_template("MST.html", text=text,title="Prims Algorithm",img=full_filename,req1='view_prims1',req2='view_prims2',req3='view_prims3') 
@app.route("/second")
def view_Kruskal():
    text=Markup('<h3>Minimum spanning tree:</h3>Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all the vertices together. A single graph can have many different spanning trees. A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected and undirected graph is a spanning tree with weight less than or equal to the weight of every other spanning tree. The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.A minimum spanning tree has (V – 1) edges where V is the number of vertices in the given graph.One of the minimum spanning tree algorithms is  Kruskal’s Minimum Spanning Tree Algorithm.<br><br><h3>KRUSKAL:</h3><br><h5>Algorithm:</h5><br>1.Sort all the edges in non-decreasing order of their weight. <br>2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it. <br>3. Repeat step 2 until there are (V-1) edges in the spanning tree.')
    return render_template("MST.html",title="Kruskals Algorithm",req1='view_kruskal1',req2='view_kruskal2',req3='view_kruskal3',text=text)
@app.route("/kruskal1")
def view_kruskal1():
    k1.kruskal1()
    text=Markup('<h3>Step1:</h3><br>Sort the edges in increasing order of their weights.<br>The order of edges after sorting according to their weights : 4,5,6,10,15<br>No of edges=0<br><h3>Iteration1:</h3>Pick edge with smallest edge weight which is 4. Since  this edge doesn’t form a cycle, add it to MST.<br>MST set now contains edges with weights {4}<br><h3>Iteration 2:</h3>Pick edge with next smallest edge weight which is 5 . Since  this edge doesn’t form a cycle, add it to MST.<br>MST set now contains edges with weights {4,5}<br><h3>Iteration 3:</h3>Pick edge with next smallest edge weight which is 6. Since  this edge forms a cycle, don’t add it to MST.<br>MST set now contains edges with weights {4,5}<br><h3>Iteration 4:</h3>Pick edge with next smallest edge weight which is 10.<br> Since  this edge doesn’t form a cycle, add it to MST.<br>MST set now contains edges with weights {4,5,10}.<br><b> Since we got no of edges(3) = no of nodes(4)-1, we can stop the iteration here and our final MST is ready.')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowjalebi7gif.gif')
    return render_template("MST.html", text=text,title="Kruskal Algorithm",img=full_filename,req1='view_kruskal1',req2='view_kruskal2',req3='view_kruskal3') 
@app.route("/kruskal2")
def view_kruskal2():
    k2.kruskal2()
    text=Markup('There are totally 5 nodes and 7 edges. Considering  the Kruskals algorithm, the the minimum spanning tree is formed as follows:')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowjalebi10gif.gif')
    return render_template("MST.html",text=text, title="Kruskal Algorithm",img=full_filename,req1='view_kruskal1',req2='view_kruskal2',req3='view_kruskal3') 
@app.route("/kruskal3")
def view_kruskal3():
    k3.kruskal3()
    text=Markup('There are totally 5 nodes and 6 edges. Considering  the Kruskals algorithm, the the minimum spanning tree is formed as follows:')
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowjalebi9gif.gif')
    return render_template("MST.html",text=text, title="Kruskal Algorithm",img=full_filename,req1='view_kruskal1',req2='view_kruskal2',req3='view_kruskal3') 
@app.route('/kruskal4', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        source=request.form.get("source")
        destination=request.form.get("destination")
        vertices = request.form.get('vertices')
        edges = request.form.get('edges')
        edgelist = request.form.get('edgelist')
        algo= request.form.get('algo')
        return redirect(url_for('booking',vertices=vertices,edges=edges,edgelist=edgelist,algo=algo,source=source,destination=destination))
    return render_template('index1.html')
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    vertices = request.args.get('vertices', None)
    source=request.args.get("source",None)
    destination=request.args.get("destination",None)
    edges = request.args.get('edges', None)
    edgelist = request.args.get('edgelist', None)
    algo=request.args.get('algo', None)
    if (algo=="Prims"):
        t3.prims1(vertices,edges,edgelist)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowjalebi4gif.gif')
    elif(algo=="Kruskal"):
        t.kruskal1(vertices,edges,edgelist)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowjalebi10gif.gif')
    elif(algo=="Dijkstras"):
        t2.main(vertices,edges,edgelist,source,destination)
        full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowdijgif4.gif')
    return render_template('booking.html',img=full_filename) 
@app.route("/dij1", methods=['GET', 'POST'])
def view_dij1():
    text=Markup('<h3>Algorithm</h3>1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty. <br>2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first. <br>3) While sptSet doesn’t include all vertices <br>&nbsp;&nbsp;a) Pick a vertex u which is not there in sptSet and has minimum distance value. <br>&nbsp;&nbsp;b) Include u to sptSet<br>&nbsp;&nbsp;c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex <br>&nbsp;&nbsp;v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.')
    text2=Markup('<table><tr><th>Vertex</th><th></th><th>Distance from Source</th></tr><tr><td>0</td><td></td><td>0</td></tr><tr><td>1</td><td></td><td>4</td></tr><tr><td>2</td><td></td><td>12</td></tr><tr><td>3</td><td></td><td>19</td></tr><tr><td>4</td><td></td><td>21</td></tr><tr><td>5</td><td></td><td>11</td></tr><tr><td>6</td><td></td><td>9</td></tr><tr><td>7</td><td></td><td>8</td></tr><tr><td>8</td><td></td><td>14</td></tr></table>')    
    if request.method == 'POST':
        source=request.form.get("source")
        destination=request.form.get("destination")
        return redirect(url_for('index3',source=source,destination=destination))
    return render_template("MST2.html", text=text,text1=text2,title="Dijkstras Algorithm")
@app.route("/index3", methods=['GET', 'POST'])
def index3():
    vertices=9
    edges=14
    source=request.args.get("source",None)
    destination=request.args.get("destination",None)
    text=Markup('<h3>Algorithm</h3>1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty. <br>2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first. <br>3) While sptSet doesn’t include all vertices <br>&nbsp;&nbsp;a) Pick a vertex u which is not there in sptSet and has minimum distance value. <br>&nbsp;&nbsp;b) Include u to sptSet<br>&nbsp;&nbsp;c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. For every adjacent vertex <br>&nbsp;&nbsp;v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, then update the distance value of v.')
    text2=Markup('<table><tr><th>Vertex</th><th></th><th>Distance from Source</th></tr><tr><td>0</td><td></td><td>0</td></tr><tr><td>1</td><td></td><td>4</td></tr><tr><td>2</td><td></td><td>12</td></tr><tr><td>3</td><td></td><td>19</td></tr><tr><td>4</td><td></td><td>21</td></tr><tr><td>5</td><td></td><td>11</td></tr><tr><td>6</td><td></td><td>9</td></tr><tr><td>7</td><td></td><td>8</td></tr><tr><td>8</td><td></td><td>14</td></tr></table>')
    d1.main(source,destination)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'slowdijgif4.gif')
    return render_template("MST2.html", text=text,text1=text2,title="Dijkstras Algorithm",img=full_filename)
if __name__ == "__main__":
    app.run(debug=True)
