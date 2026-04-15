# DNA Sequence Comparison

A web application that compares user-input DNA sequences against a database of 34 real COI barcode sequences from NCBI GenBank. It identifies the closest species match using GC content filtering, sequence similarity analysis, and relationship graph visualization.

## How It Works

1. **GC Content Pre-filtering** - Calculates the GC content (ratio of G+C bases) of the input and sorts all database sequences by GC content using Merge Sort. Sequences outside a ±10 percentage point threshold are excluded, narrowing the search space.

2. **Sequence Similarity** - Compares the input against filtered candidates using the Longest Common Subsequence (LCS) algorithm. Produces a similarity score (0-100%) for each candidate.

3. **Relationship Graph** - Builds a complete similarity graph between the input and top matches, then extracts a Minimum Spanning Tree using Prim's algorithm. Visualizes how species cluster by evolutionary relatedness.

## Algorithms
- **Merge Sort** - O(n log n) sorting of sequences by GC content
- **Longest Common Subsequence** - O(m x n) dynamic programming for pairwise sequence comparison
- **Prim's MST** - O(E log V) minimum spanning tree extraction using a min-heap

## Data Structures (all custom implementations)
1. **Hash Map** - Separate chaining hash table for database storage
2. **Array/List** - Merge sort working arrays and candidate lists
3. **2D Matrix** - LCS dynamic programming table
4. **Min-Heap** - Priority queue with insert, extract_min, decrease_key for Prim's algorithm
5. **Adjacency List Graph** - Weighted undirected graph for similarity relationships and MST

## Database
34 real COI (Cytochrome c Oxidase Subunit I) barcode sequences sourced from NCBI GenBank, covering mammals, birds, fish, insects, reptiles, and amphibians. Each entry includes the NCBI accession number for verification.

## Setup

```bash
pip install flask matplotlib networkx
python app.py
```

Then open http://localhost:5001 in your browser.

## Project Structure
```
dna-comparison/
├── app.py                  # Flask web server and analysis pipeline
├── dna_database.py         # 34 real COI sequences from NCBI GenBank
├── algorithms/
│   ├── sorting.py          # Merge Sort + GC content calculation
│   ├── lcs.py              # LCS with custom 2D Matrix
│   └── mst.py              # Prim's MST with custom MinHeap + Graph
├── data_structures/
│   ├── hash_map.py         # Custom hash map (separate chaining)
│   ├── heap.py             # Custom min-heap (priority queue)
│   └── graph.py            # Custom adjacency list graph
├── templates/
│   └── index.html          # Web UI
├── static/
│   ├── style.css           # Dashboard styling
│   └── graphs/             # Generated graph images
└── requirements.txt
```

## References
- GC content as phylogenetic signal: Hildebrand et al. (2010) https://doi.org/10.1371/journal.pgen.1001107
- GC deviation thresholds: Mann & Chen (2010) https://doi.org/10.1016/j.ygeno.2009.09.002
- DNA barcode data: BOLD Systems https://www.boldsystems.org/
- Sequence data: NCBI GenBank https://www.ncbi.nlm.nih.gov/genbank/
