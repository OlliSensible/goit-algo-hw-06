import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

people = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
relationships = [("Alice", "Bob"), ("Bob", "Charlie"), ("Charlie", "Diana"), ("Diana", "Eve"), ("Eve", "Alice")]

G.add_nodes_from(people)
G.add_edges_from(relationships)

nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=15)
plt.show()

print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
degrees = dict(G.degree())
print(f"Ступені вершин: {degrees}")