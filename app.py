# Flask web application for DNA Sequence Comparison
# Ties together all algorithms and data structures

import os
from flask import Flask, render_template, request, session, redirect, url_for

from dna_database import get_all_sequences
from algorithms.sorting import calculate_gc_content, sort_by_gc_content, filter_by_gc_threshold
from algorithms.lcs import compare_against_candidates
from algorithms.mst import build_similarity_graph, prims_mst, visualize_graphs

app = Flask(__name__)
app.secret_key = "dna-comparison-key"


def validate_dna(sequence):
    """
    Validate that the input only contains valid DNA bases (A, T, G, C).
    Returns (cleaned_sequence, error_message).
    """
    # Remove whitespace and newlines
    cleaned = sequence.strip().upper().replace(" ", "").replace("\n", "").replace("\r", "")

    if len(cleaned) == 0:
        return None, "Please enter a DNA sequence."

    if len(cleaned) < 10:
        return None, "Sequence is too short. Please enter at least 10 bases."

    # Check for invalid characters
    for i, char in enumerate(cleaned):
        if char not in "ATGC":
            return None, f"Invalid character '{char}' at position {i+1}. Only A, T, G, C are allowed."

    return cleaned, None


@app.route("/", methods=["GET"])
def index():
    """Main page — shows clean input form on GET."""
    return render_template("index.html", results=None, error=None, input_sequence="")


@app.route("/analyze", methods=["POST"])
def analyze():
    """Handle form submission — analyze the DNA and show results."""
    input_sequence = request.form.get("dna_sequence", "")

    # Validate the input
    cleaned, error = validate_dna(input_sequence)

    if error is not None:
        return render_template("index.html", results=None, error=error, input_sequence=input_sequence)

    # Run the analysis pipeline
    results = analyze_dna(cleaned)

    return render_template("index.html", results=results, error=None, input_sequence=cleaned)


def analyze_dna(input_sequence):
    """
    Run the full analysis pipeline on the input DNA sequence.

    Steps:
        1. Calculate GC content of the input
        2. Sort all database sequences by GC content (merge sort)
        3. Filter candidates within ±10pp of input GC content
        4. Compare filtered candidates using LCS
        5. Build similarity graph and MST from top matches
        6. Generate MST visualization

    Returns a dict with all results for the template.
    """
    # Clean up old graph images before generating a new one
    graph_dir = os.path.join(app.static_folder, "graphs")
    if os.path.exists(graph_dir):
        for old_file in os.listdir(graph_dir):
            if old_file.endswith(".png"):
                os.remove(os.path.join(graph_dir, old_file))

    # Step 1: Calculate GC content of the input sequence
    input_gc = calculate_gc_content(input_sequence)

    # Step 2: Load database and sort by GC content using merge sort
    all_sequences = get_all_sequences()
    sorted_sequences = sort_by_gc_content(all_sequences)

    # Step 3: Filter to candidates within ±10 percentage points of input GC
    gc_threshold = 0.10
    filtered_candidates = filter_by_gc_threshold(sorted_sequences, input_gc, gc_threshold)

    # Mark which sequences in the sorted list passed the filter
    # (for display purposes — show all sorted, highlight filtered)
    for entry in sorted_sequences:
        difference = abs(entry['gc_content'] - input_gc)
        entry['gc_filtered'] = difference <= gc_threshold
        entry['gc_difference'] = round(difference * 100, 2)  # as percentage points

    # Step 4: Compare filtered candidates against input using LCS
    if len(filtered_candidates) > 0:
        # Compare all filtered candidates using LCS
        lcs_results = compare_against_candidates(input_sequence, filtered_candidates)
    else:
        lcs_results = []

    # Step 5: Build similarity graph and MST from top 8 matches
    complete_image = None
    mst_image = None
    mst_edges = []
    top_for_mst = lcs_results[:10]

    if len(top_for_mst) >= 2:
        # Build the complete similarity graph
        similarity_graph = build_similarity_graph(
            input_sequence, "Your Input", top_for_mst
        )

        # Run Prim's MST algorithm
        mst = prims_mst(similarity_graph)
        mst_edges = mst.get_edges()

        # Generate both graph visualizations as separate images
        graph_dir = os.path.join(app.static_folder, "graphs")
        complete_image, mst_image = visualize_graphs(
            similarity_graph, mst, "Your Input", top_for_mst, graph_dir
        )

    # Find the best match
    best_match = lcs_results[0] if len(lcs_results) > 0 else None

    # Generate biological insight summary
    insight = generate_insight(best_match, lcs_results, top_for_mst, mst_edges, input_gc, filtered_candidates, all_sequences)

    return {
        "input_gc": round(input_gc * 100, 2),  # as percentage
        "input_length": len(input_sequence),
        "gc_threshold": gc_threshold * 100,  # as percentage points
        "total_sequences": len(all_sequences),
        "sorted_sequences": sorted_sequences,
        "filtered_count": len(filtered_candidates),
        "lcs_results": lcs_results,
        "best_match": best_match,
        "complete_image": complete_image,
        "mst_image": mst_image,
        "mst_edges": mst_edges,
        "insight": insight,
    }


def generate_insight(best_match, lcs_results, top_for_mst, mst_edges, input_gc, filtered, all_sequences):
    """
    Generate a plain-English biological insight based on the analysis results.
    """
    if best_match is None or len(lcs_results) == 0:
        return {
            "headline": "No Match Found",
            "strength": "none",
            "details": [
                "No candidates passed the GC content filter.",
                "This sequence does not appear to be closely related to any species in the database.",
                "The GC content of your input is outside the typical range for COI barcode sequences."
            ]
        }

    score = best_match['lcs_score']
    species = best_match['common_name']
    group = best_match.get('group', 'Unknown')

    # Determine match strength
    if score >= 0.95:
        strength = "exact"
        headline = f"Exact Match: {species}"
    elif score >= 0.80:
        strength = "strong"
        headline = f"Strong Match: {species}"
    elif score >= 0.65:
        strength = "moderate"
        headline = f"Moderate Match: {species}"
    else:
        strength = "weak"
        headline = f"Weak Match: {species}"

    details = []

    # Match description
    if strength == "exact":
        details.append(
            f"Your sequence is a {score*100:.1f}% match to {species}, "
            f"indicating it is very likely from this species or a very close relative."
        )
    elif strength == "strong":
        details.append(
            f"Your sequence shows {score*100:.1f}% similarity to {species}. "
            f"This suggests your sequence is from the same species or a closely related one, "
            f"with some mutations or sequencing differences."
        )
    elif strength == "moderate":
        details.append(
            f"Your sequence shows {score*100:.1f}% similarity to {species}. "
            f"This suggests a possible relationship, but the sequence may be from a related species "
            f"not in the database."
        )
    else:
        details.append(
            f"Your sequence shows only {score*100:.1f}% similarity to {species}. "
            f"This is a weak match — your sequence likely comes from a species not in the database."
        )

    # Dominant group analysis from top 10
    top10 = lcs_results[:10]
    group_counts = {}
    for r in top10:
        g = r.get('group', 'Unknown')
        group_counts[g] = group_counts.get(g, 0) + 1

    # Sort groups by count
    sorted_groups = sorted(group_counts.items(), key=lambda x: -x[1])
    dominant_group = sorted_groups[0][0]
    dominant_count = sorted_groups[0][1]

    # If the best match is strong/exact, trust its group over raw counts
    # (e.g., Human is 100% match but birds outnumber mammals in top 10)
    if strength in ("exact", "strong"):
        dominant_group = group

    if strength in ("exact", "strong"):
        # High confidence — trust the best match's group
        other_groups = [f"{g} ({c})" for g, c in sorted_groups if g != group]
        other_str = ", ".join(other_groups) if other_groups else "no other groups"
        details.append(
            f"Based on the {score*100:.1f}% match to {species}, your sequence belongs to the "
            f"{group} group. Other groups in the top 10: {other_str}."
        )
    elif strength == "moderate":
        # Moderate confidence — mention best match but note uncertainty
        details.append(
            f"The closest match is {species} ({group}) at {score*100:.1f}%, but the similarity "
            f"is not high enough for a definitive classification. "
            f"Top 10 breakdown: {', '.join(f'{g}: {c}' for g, c in sorted_groups)}."
        )
    else:
        # Weak match — don't claim any group
        details.append(
            f"With only {score*100:.1f}% similarity to the closest match, taxonomic classification "
            f"is unreliable. The low similarity suggests your sequence may come from a species "
            f"not represented in the database."
        )

    # GC content insight
    gc_pct = input_gc * 100
    if gc_pct < 35:
        details.append(
            f"Your sequence has a low GC content ({gc_pct:.1f}%), "
            f"which is characteristic of insect COI sequences (typically 25-35%)."
        )
    elif gc_pct < 42:
        details.append(
            f"Your sequence has a moderate GC content ({gc_pct:.1f}%), "
            f"falling in the range shared by reptiles, amphibians, and some fish (37-42%)."
        )
    elif gc_pct < 48:
        details.append(
            f"Your sequence has a GC content of {gc_pct:.1f}%, "
            f"typical of vertebrate COI sequences — mammals, birds, and fish commonly fall in this range."
        )
    else:
        details.append(
            f"Your sequence has a high GC content ({gc_pct:.1f}%), "
            f"which is characteristic of birds and some mammals in the COI gene."
        )

    # MST cluster insight
    if len(mst_edges) > 0 and strength != "weak":
        # Find what the input directly connects to in the MST
        direct_connections = []
        for v1, v2, w in mst_edges:
            if v1 == "Your Input":
                direct_connections.append((v2, w))
            elif v2 == "Your Input":
                direct_connections.append((v1, w))

        if len(direct_connections) > 0:
            conn_names = [name for name, w in direct_connections]
            # Check if direct connections are same group
            conn_groups = []
            for name in conn_names:
                for r in top_for_mst:
                    if r['common_name'] == name:
                        conn_groups.append(r.get('group', 'Unknown'))
                        break

            if len(set(conn_groups)) == 1 and conn_groups[0] == group:
                details.append(
                    f"In the relationship tree, your input connects directly to other {group.lower()} "
                    f"({', '.join(conn_names)}), confirming it belongs to this cluster."
                )
            elif len(conn_names) > 0:
                # Describe the actual connections honestly
                conn_desc = []
                for name, grp in zip(conn_names, conn_groups):
                    conn_desc.append(f"{name} ({grp})")
                unique_groups = list(set(conn_groups))

                if len(unique_groups) == 1:
                    details.append(
                        f"In the relationship tree, your input connects to {', '.join(conn_desc)}, "
                        f"placing it near the {unique_groups[0].lower()} cluster."
                    )
                elif strength in ("exact", "strong"):
                    # High confidence match — MST multi-group connections are just tree structure
                    details.append(
                        f"In the relationship tree, your input connects to {', '.join(conn_desc)}. "
                        f"The connection to other groups is due to how the tree links all species — "
                        f"the {score*100:.1f}% match to {species} confirms your sequence is {group.lower()}."
                    )
                else:
                    details.append(
                        f"In the relationship tree, your input connects to {', '.join(conn_desc)} — "
                        f"spanning multiple groups, which reflects the ambiguity of this match."
                    )

    # Filtering insight
    excluded = len(all_sequences) - len(filtered)
    if excluded > 5:
        details.append(
            f"The GC content filter excluded {excluded} of {len(all_sequences)} database sequences, "
            f"narrowing the search to {len(filtered)} biologically plausible candidates."
        )

    return {
        "headline": headline,
        "strength": strength,
        "details": details,
    }


if __name__ == "__main__":
    # Create the graphs directory if it doesn't exist
    os.makedirs(os.path.join("static", "graphs"), exist_ok=True)
    app.run(debug=True, host="0.0.0.0", port=5001)
