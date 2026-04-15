# Prim's Minimum Spanning Tree algorithm
# Builds a relationship graph from DNA similarity scores
# Uses custom MinHeap and Graph data structures

import os
import uuid
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for server
import matplotlib.pyplot as plt
import networkx as nx

from data_structures.heap import MinHeap
from data_structures.graph import Graph
from algorithms.lcs import lcs_similarity


def build_similarity_graph(input_sequence, input_label, top_matches):
    """
    Build a complete weighted graph from the input sequence and top LCS matches.

    Nodes = input sequence + each top match
    Edge weights = 1 - LCS similarity (lower weight = more similar)

    Args:
        input_sequence: the user's DNA string
        input_label: label for the input node (e.g. "Your Input")
        top_matches: list of top candidate entries (each has 'species', 'sequence', 'lcs_score')

    Returns:
        A Graph object with all vertices and weighted edges
    """
    graph = Graph()

    # Collect all nodes: input + top matches
    nodes = []
    sequences = {}

    # Add the input sequence as the first node
    graph.add_vertex(input_label)
    nodes.append(input_label)
    sequences[input_label] = input_sequence

    # Add each top match as a node
    for match in top_matches:
        label = match['common_name']
        graph.add_vertex(label)
        nodes.append(label)
        sequences[label] = match['sequence']

    # Add edges between every pair of nodes (complete graph)
    # Edge weight = 1 - similarity (so more similar = lower weight = closer in MST)
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            node_a = nodes[i]
            node_b = nodes[j]

            # If one of them is the input, we may already have the LCS score
            similarity = lcs_similarity(sequences[node_a], sequences[node_b])
            weight = round(1.0 - similarity, 4)  # Lower weight = more similar

            graph.add_edge(node_a, node_b, weight)

    return graph


def prims_mst(graph):
    """
    Find the Minimum Spanning Tree using Prim's algorithm with a custom MinHeap.

    Args:
        graph: a Graph object with vertices and weighted edges

    Returns:
        A new Graph object containing only the MST edges

    Time complexity: O(E log V) with min-heap
    """
    vertices = graph.get_vertices()
    if len(vertices) == 0:
        return Graph()

    # Track which vertices are in the MST
    in_mst = []

    # Track the minimum weight edge to reach each vertex
    # and which vertex connects to it
    min_weight = {}   # vertex -> minimum weight to connect to MST
    parent = {}       # vertex -> parent vertex in MST

    # Initialize: all vertices have infinite weight except the start
    heap = MinHeap()
    start = vertices[0]

    for v in vertices:
        if v == start:
            min_weight[v] = 0.0
            heap.insert(0.0, v)
        else:
            min_weight[v] = float('inf')
            heap.insert(float('inf'), v)
        parent[v] = None

    # Build the MST
    mst = Graph()
    for v in vertices:
        mst.add_vertex(v)

    while not heap.is_empty():
        # Extract the vertex with the minimum connection weight
        weight, current = heap.extract_min()

        # Add this vertex to the MST
        in_mst.append(current)

        # If it has a parent, add the MST edge
        if parent[current] is not None:
            mst.add_edge(parent[current], current, min_weight[current])

        # Update neighbors
        for neighbor, edge_weight in graph.get_neighbors(current):
            # Only consider vertices not yet in the MST
            if neighbor not in in_mst and edge_weight < min_weight[neighbor]:
                min_weight[neighbor] = edge_weight
                parent[neighbor] = current
                # Decrease the key in the heap
                heap.decrease_key(neighbor, edge_weight)

    return mst


def _get_graph_style(input_label, top_matches):
    """
    Return shared styling info (colors, groups, etc.) used by both graph visualizations.
    """
    group_colors = {
        "Mammals": "#E74C3C",
        "Birds": "#1ABC9C",
        "Fish": "#3498DB",
        "Insects": "#27AE60",
        "Reptiles": "#F39C12",
        "Amphibians": "#9B59B6",
        "Input": "#00E5FF",
    }

    node_groups = {}
    node_groups[input_label] = "Input"
    for match in top_matches:
        node_groups[match['common_name']] = match.get('group', 'Unknown')

    return group_colors, node_groups


def _draw_graph(ax, nx_graph, pos, node_groups, group_colors, input_label, title, show_edge_labels=True):
    """
    Draw a graph on the given axes with consistent styling.
    Shared by both the complete graph and the MST visualization.
    """
    ax.set_facecolor('#1a1a2e')

    # Assign colors to each node
    node_colors = []
    for node in nx_graph.nodes():
        group = node_groups.get(node, "Unknown")
        color = group_colors.get(group, "#CCCCCC")
        node_colors.append(color)

    # Draw edges with varying thickness based on similarity
    edge_weights = nx.get_edge_attributes(nx_graph, 'weight')
    for (u, v), w in edge_weights.items():
        similarity = 1 - w
        line_width = 1 + similarity * 4
        alpha = 0.3 + similarity * 0.5
        nx.draw_networkx_edges(
            nx_graph, pos, ax=ax,
            edgelist=[(u, v)],
            width=line_width, alpha=alpha,
            edge_color='#88ccff',
            style='solid'
        )

    # Draw edge labels (similarity %)
    if show_edge_labels:
        edge_labels = {}
        for (u, v), w in edge_weights.items():
            similarity_pct = round((1 - w) * 100, 1)
            edge_labels[(u, v)] = f"{similarity_pct}%"
        nx.draw_networkx_edge_labels(
            nx_graph, pos, edge_labels=edge_labels, ax=ax,
            font_size=7, font_color='#aaccee',
            bbox=dict(boxstyle='round,pad=0.1', facecolor='#1a1a2e', edgecolor='none', alpha=0.8)
        )

    # Node sizes — input is larger but keep all nodes smaller to avoid overlap
    node_sizes = []
    for node in nx_graph.nodes():
        if node == input_label:
            node_sizes.append(1000)
        else:
            node_sizes.append(600)

    # Glow layer
    nx.draw_networkx_nodes(
        nx_graph, pos, ax=ax,
        node_color=node_colors, node_size=[s * 1.6 for s in node_sizes],
        alpha=0.15, linewidths=0
    )

    # Main nodes
    nx.draw_networkx_nodes(
        nx_graph, pos, ax=ax,
        node_color=node_colors, node_size=node_sizes,
        edgecolors='white', linewidths=2.5, alpha=0.95
    )

    # Labels
    for node, (x, y) in pos.items():
        ax.text(
            x, y - 0.12, node,
            fontsize=8, fontweight='bold',
            color='white',
            ha='center', va='top',
            bbox=dict(
                boxstyle='round,pad=0.3',
                facecolor='#2d2d44', edgecolor='#555577',
                alpha=0.85
            )
        )

    # Legend
    legend_handles = []
    for group, color in group_colors.items():
        if any(node_groups.get(n) == group for n in nx_graph.nodes()):
            handle = plt.Line2D(
                [0], [0], marker='o', color='w',
                markerfacecolor=color, markersize=10,
                markeredgecolor='white', markeredgewidth=1.5,
                label=group
            )
            legend_handles.append(handle)
    ax.legend(
        handles=legend_handles, loc='upper left', fontsize=8,
        facecolor='#2d2d44', edgecolor='#555577',
        labelcolor='white', framealpha=0.9
    )

    ax.set_title(title, fontsize=13, fontweight='bold', color='white', pad=15)
    ax.axis('off')


def _render_single_graph(nx_graph, pos, node_groups, group_colors, input_label,
                         title, subtitle, output_dir, prefix, show_edge_labels=True):
    """Render a single graph to its own PNG file."""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    fig.patch.set_facecolor('#1a1a2e')

    _draw_graph(ax, nx_graph, pos, node_groups, group_colors, input_label,
                title, show_edge_labels=show_edge_labels)

    # Edge count subtitle
    ax.text(0.5, -0.02, subtitle,
            transform=ax.transAxes, ha='center', fontsize=10, color='#aaaaaa')

    plt.tight_layout(pad=1.5)

    os.makedirs(output_dir, exist_ok=True)
    filename = f"{prefix}_{uuid.uuid4().hex[:8]}.png"
    filepath = os.path.join(output_dir, filename)
    plt.savefig(filepath, dpi=150, bbox_inches='tight')
    plt.close(fig)

    return filename


def visualize_graphs(complete_graph, mst, input_label, top_matches, output_dir="static/graphs"):
    """
    Generate two separate graph images:
      1. Complete graph (all edges)
      2. MST (only Prim's selected edges)

    Both use the same node positions so they can be visually compared.

    Returns:
        (complete_filename, mst_filename) tuple
    """
    group_colors, node_groups = _get_graph_style(input_label, top_matches)

    # Build networkx graphs for visualization only
    nx_complete = nx.Graph()
    for v1, v2, weight in complete_graph.get_edges():
        nx_complete.add_edge(v1, v2, weight=weight)
    for v in complete_graph.get_vertices():
        nx_complete.add_node(v)

    nx_mst = nx.Graph()
    for v1, v2, weight in mst.get_edges():
        nx_mst.add_edge(v1, v2, weight=weight)
    for v in mst.get_vertices():
        nx_mst.add_node(v)

    complete_edge_count = len(complete_graph.get_edges())
    mst_edge_count = len(mst.get_edges())

    # Layout for complete graph — spring layout on all edges
    pos_complete = nx.spring_layout(nx_complete, k=3.0, iterations=200, seed=42)
    for key in pos_complete:
        pos_complete[key] = pos_complete[key] * 2.0

    # Layout for MST — spring layout on MST edges only
    # This makes connected nodes cluster together visually
    # Use edge weight as distance (higher weight = more repulsion)
    pos_mst = nx.spring_layout(nx_mst, k=4.0, iterations=300, seed=42, weight='weight')
    for key in pos_mst:
        pos_mst[key] = pos_mst[key] * 2.5

    # Render complete graph
    complete_file = _render_single_graph(
        nx_complete, pos_complete, node_groups, group_colors, input_label,
        "Complete Graph (All Edges)", f"{complete_edge_count} edges",
        output_dir, "complete", show_edge_labels=False
    )

    # Render MST graph with its own layout
    mst_file = _render_single_graph(
        nx_mst, pos_mst, node_groups, group_colors, input_label,
        "After Prim's MST", f"{mst_edge_count} edges",
        output_dir, "mst", show_edge_labels=True
    )

    return complete_file, mst_file
