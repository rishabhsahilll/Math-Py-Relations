import matplotlib.pyplot as plt
import networkx as nx
from itertools import product, combinations
from sklearn.cluster import KMeans
import numpy as np

# Introduction
intro = """
Name: Rishabh Sahil
Topic: Relation & Functions (Find all Possible Relations with Graph & ML)
Version: 1.2 (Fully Display)
"""
print(intro)

# Select Mode
mode = input("Choose mode - Simple (S) or Advanced (A): ").strip().upper()

# Get number of sets from user
while True:
    try:
        num_sets = int(input("Enter the number of sets (2 or 3): "))
        if num_sets in [2, 3]:
            break
        print("Please enter either 2 or 3")
    except ValueError:
        print("Please enter a valid number")

# Get elements for sets
sets = {}
sets['A'] = input("Enter elements for set A (comma-separated): ").split(',')
sets['B'] = input("Enter elements for set B (comma-separated): ").split(',')
if num_sets == 3:
    sets['C'] = input("Enter elements for set C (comma-separated): ").split(',')

# Print the sets
print("\nGiven Sets:")
for set_name, set_values in sets.items():
    print(f"{set_name} = {set(set_values)}")

# Calculate Cartesian Product
if num_sets == 2:
    cartesian_product = list(product(sets['A'], sets['B']))
    print(f"\nA × B = {set(cartesian_product)}")
else:
    cartesian_product = list(product(sets['A'], sets['B'], sets['C']))
    print(f"\nA × B × C = {set(cartesian_product)}")

# Calculate total number of possible relations
n_cartesian = len(cartesian_product)
n_relations = 2 ** n_cartesian
print(f"\nNumber of possible relations = 2^{n_cartesian} = {n_relations}")

# Generate all possible relations
all_relations = [set(comb) for i in range(len(cartesian_product) + 1) for comb in combinations(cartesian_product, i)]
print("\nAll possible relations:")
for i, relation in enumerate(all_relations, 1):
    print(f"R{i} = {relation}")

# Graph Visualization (Advanced Mode)
if mode == 'A':
    G = nx.DiGraph()
    
    # Add nodes for set A and set B
    for a in sets['A']:
        G.add_node(a, layer=0)
    for b in sets['B']:
        G.add_node(b, layer=1)

    # Add edges for Cartesian product relations
    G.add_edges_from(cartesian_product)

    # Positioning nodes for better visualization
    pos = {}
    for i, a in enumerate(sets['A']):
        pos[a] = (0, i)
    for i, b in enumerate(sets['B']):
        pos[b] = (1, i)

    # Draw the Graph
    plt.figure(figsize=(7, 5))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=12, arrows=True)
    plt.title("Mapping Diagram for Cartesian Product")
    plt.show()

    # Machine Learning - Clustering
    X = []
    for x in cartesian_product:
        try:
            X.append([int(x[0]), int(x[1])])
        except ValueError:
            continue  # Skip non-numeric pairs

    X = np.array(X)

    if len(X) > 1:
        kmeans = KMeans(n_clusters=min(2, len(X)), random_state=42, n_init=10)
        labels = kmeans.fit_predict(X)
        print("\nCluster Labels:", labels)
    else:
        print("\nNot enough numeric data for clustering.")
