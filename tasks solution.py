import sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.Cgraph(nodes, init_graph)
        
    def Cgraph(self, nodes, init_graph):

        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        return self.nodes
    
    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}  
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes: 
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
 
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    path.append(start_node)
    
    print("The shortest route is {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))


nodes = ["Rabat", "Sueca", "Rudow", "Mosu", "Le Plessis Trevise", "Kang Dong",
		 "Nezahualcóyotl", "Lindenwold", "Queanbeyan", "Saint Chamond",
		  "Cheektowaga", "Tirupati", "Snezhinsk", "Glazov", "Gaoyou",
		   "Nola", "Rutigliano", "Colombo", "Meckenheim", "Hamburg"]
 
init_graph = {}
for node in nodes:
    init_graph[node] = {}
    
init_graph["Rabat"]["Sueca"] = 1063
init_graph["Sueca"]["Rudow"] = 2656
init_graph["Rudow"]["Mosu"] = 1352
init_graph["Mosu"]["Le Plessis Trevise"] = 1841
init_graph["Le Plessis Trevise"]["Kang Dong"] = 61
init_graph["Kang Dong"]["Nezahualcóyotl"] = 1634
init_graph["Nezahualcóyotl"]["Lindenwold"] = 151
init_graph["Lindenwold"]["Queanbeyan"] = 285
init_graph["Queanbeyan"]["Saint Chamond"] = 146
init_graph["Saint Chamond"]["Cheektowaga"] = 11
init_graph["Cheektowaga"]["Tirupati"] = 380
init_graph["Tirupati"]["Snezhinsk"] = 2547
init_graph["Snezhinsk"]["Glazov"] = 2524
init_graph["Glazov"]["Gaoyou"] = 97
init_graph["Gaoyou"]["Nola"] = 6999
init_graph["Nola"]["Rutigliano"] = 63
init_graph["Rutigliano"]["Colombo"] = 105
init_graph["Colombo"]["Meckenheim"] = 244
init_graph["Meckenheim"]["Hamburg"] = 502
init_graph["Hamburg"]["Rabat"] = 30

graph = Graph(nodes, init_graph)
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="Rabat")
print_result(previous_nodes, shortest_path, start_node="Rabat", target_node="Hamburg")
