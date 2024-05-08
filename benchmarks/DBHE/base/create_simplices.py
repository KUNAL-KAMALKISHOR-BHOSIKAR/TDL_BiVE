from collections import defaultdict
import numpy as np

def read_data(file_path):
    data = []
    weights = defaultdict(int)
    with open(file_path, 'r') as file:
        for line in file:
            node1, node2, weight = line.strip().split()
            data.append((int(node1), int(node2), int(weight)))
            weights[int(node1)] += int(weight)
            weights[int(node2)] += int(weight)
    return data, weights

def create_simplex_dicts(data):
    # Create dictionary for 0-simplices
    all_nodes = set()
    for node1, node2, _ in data:
        all_nodes.add(node1)
        all_nodes.add(node2)

    node_simplex_dict = {frozenset({node}): idx for idx, node in enumerate(all_nodes)}

    # Create dictionary for 1-simplices
    edge_simplex_dict = defaultdict(lambda: len(edge_simplex_dict))
    for node1, node2, _ in data:
        edge = frozenset({node1, node2})
        edge_simplex_dict[edge]

    edge_simplex_dict = {edge: idx for edge, idx in edge_simplex_dict.items()}

    simplex_dicts = [node_simplex_dict, edge_simplex_dict]
    # print(simplex_dicts)
    return simplex_dicts

def build_cochains(simplex_dicts, data, function=sum):
    node_simplex_dict, edge_simplex_dict = simplex_dicts
    cochains = [{}, {}]

    for node1, node2, weight in data:
        edge = frozenset({node1, node2})
        edge_idx = edge_simplex_dict[edge]
        node1_idx = node_simplex_dict[frozenset({node1})]
        node2_idx = node_simplex_dict[frozenset({node2})]

        # Compute cochain for the edge
        cochains[1][edge] = weight

        # Compute cochains for the nodes
        cochains[0][frozenset({node1})] = cochains[0].get(frozenset({node1}), 0) + weight
        cochains[0][frozenset({node2})] = cochains[0].get(frozenset({node2}), 0) + weight

        cochains = [cochains[0], cochains[1]]

    return cochains

def main():
    # Replace 'dataset.txt' with the actual file name and path
    file_path = 'dataset_with_1.txt'
    data, weights = read_data(file_path)

    simplex_dicts = create_simplex_dicts(data)
    cochains_dicts = build_cochains(simplex_dicts, data)

    np.save("simplices.npy", simplex_dicts)
    np.save("cochains.npy", cochains_dicts)
    np.save("node_weights.npy", weights)

    # simplices=np.load(f'simplices.npy', allow_pickle = True)
    # cochains=np.load(f'cochains.npy', allow_pickle = True)

    # print(simplices)
    # print(cochains)

if __name__ == "__main__":
    main()