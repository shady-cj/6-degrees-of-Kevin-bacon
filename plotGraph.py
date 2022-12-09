"""
This module provides a function plot_graph that uses networkx
and matplotlib to plot the edges from the Bacon's number relationship
result and displays the visualization
"""

import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(rel_table):
    nodes = rel_table["nodes"]
    edges = []
    for entry in rel_table["edges"]:
        if all([entry[0], entry[1]]):
            firstPerson = entry[0].getName()
            secondPerson = entry[1].getName()
            movie_starred = entry[2]
            edges.append((firstPerson, secondPerson, {"movie": movie_starred}))
    G = nx.Graph()
    G.add_nodes_from(nodes)
    
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, with_labels=True,
            node_color="red", node_size=5000,
            font_color="black", font_size=9,
            font_family="Times New Roman",
            font_weight="bold",
            width=3
    )
    
    edge_labels = nx.get_edge_attributes(G,'movie')
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=5)
    plt.margins(0.2)
    plt.show()
    

