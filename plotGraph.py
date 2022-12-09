import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(node_list):
    nodes = [a['name'] for a in node_list]
    edges = []
    for index, a in enumerate(node_list):
        next_index = index + 1
        if next_index < len(node_list):
            next_entry_name = node_list[next_index]['name']
            movie_starred = node_list[next_index]['movie']
            edges.append((a["name"], next_entry_name, {"movie": movie_starred}))
    G = nx.Graph()
    G.add_nodes_from(nodes)
    
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, with_labels=True,
            node_color="red", node_size=5000,
            font_color="white", font_size=7,
            font_family="Times New Roman",
            font_weight="bold",
            width=3
    )
    
    edge_labels = nx.get_edge_attributes(G,'movie')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.margins(0.2)
    plt.show()
    

