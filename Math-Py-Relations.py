intro = """

Name: Rishabh Sahil
Topic: Relation & Functions (Find all Possible Relations)
Version = 0.6
"""
print("")
print(intro)
print("")
print("")
from itertools import product, chain, combinations

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
if num_sets >= 2:
    A_input = input("Enter elements for set A (comma-separated): ")
    sets['A'] = A_input.split(',')  # Using list to maintain order

    B_input = input("Enter elements for set B (comma-separated): ")
    sets['B'] = B_input.split(',')  # Using list to maintain order

if num_sets == 3:
    C_input = input("Enter elements for set C (comma-separated): ")
    sets['C'] = C_input.split(',')  # Using list to maintain order

# Print the sets
for set_name, set_values in sets.items():
    print(f"{set_name} = {set(set_values)}")  # Display as set, but keep order internally

# Calculate Cartesian product based on number of sets
if num_sets == 2:
    cartesian_product = list(product(sets['A'], sets['B']))  # Keeping order
    print(f"A × B = {set(cartesian_product)}")  # Display as set, but maintain list order
else:
    cartesian_product = list(product(sets['A'], sets['B'], sets['C']))
    print(f"A × B × C = {set(cartesian_product)}")  # Display as set

# Calculate and print size of Cartesian product
n_cartesian = len(cartesian_product)
print("")
print(f"n({' × '.join(sets.keys())}) = {n_cartesian}")
print("")

# Calculate total number of possible relations
n_relations = 2 ** n_cartesian
print(f"Number of possible relations = 2^{n_cartesian} = {n_relations}")

# Generate all possible relations
cartesian_list = list(cartesian_product)
all_relations = []
for i in range(len(cartesian_list) + 1):
    combos = combinations(cartesian_list, i)
    all_relations.extend(combos)

# Print all relations
print("\nAll possible relations:")
for i, relation in enumerate(all_relations, 1):
    relation_set = set(relation)
    if not relation_set:
        print(f"R{i} = {{}}")
    else:
        relation_str = ", ".join([str(tuple(x)) for x in relation_set])
        print(f"R{i} = {{{relation_str}}}")
