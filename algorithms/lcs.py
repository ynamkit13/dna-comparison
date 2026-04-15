# Longest Common Subsequence (LCS) algorithm for DNA comparison
# Uses dynamic programming to find the longest subsequence common to two sequences
# The LCS length relative to sequence length gives a similarity score


class Matrix:
    """
    Custom 2D Matrix data structure for the LCS dynamic programming table.
    Wraps a list of lists with convenient get/set/dimensions methods.
    This is one of the 5 required data structures.
    """

    def __init__(self, rows, cols, default_value=0):
        """Create a rows x cols matrix filled with the default value."""
        self.rows = rows
        self.cols = cols
        # Build the 2D array row by row
        self.data = []
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(default_value)
            self.data.append(row)

    def get(self, row, col):
        """Get the value at position (row, col)."""
        return self.data[row][col]

    def set(self, row, col, value):
        """Set the value at position (row, col)."""
        self.data[row][col] = value

    def dimensions(self):
        """Return (rows, cols) tuple."""
        return (self.rows, self.cols)


def lcs_length(seq1, seq2):
    """
    Compute the length of the Longest Common Subsequence between two DNA strings.

    Uses a 2D dynamic programming table (custom Matrix).

    Args:
        seq1: first DNA sequence string
        seq2: second DNA sequence string

    Returns:
        Integer length of the LCS

    Time complexity: O(m * n) where m = len(seq1), n = len(seq2)
    Space complexity: O(m * n) for the DP table
    """
    m = len(seq1)
    n = len(seq2)

    # Create the DP table with (m+1) rows and (n+1) columns
    # dp[i][j] = LCS length of seq1[:i] and seq2[:j]
    dp = Matrix(m + 1, n + 1, default_value=0)

    # Fill the table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                # Characters match — extend the LCS by 1
                dp.set(i, j, dp.get(i - 1, j - 1) + 1)
            else:
                # Characters don't match — take the best from excluding one character
                dp.set(i, j, max(dp.get(i - 1, j), dp.get(i, j - 1)))

    # The answer is in the bottom-right cell
    return dp.get(m, n)


def lcs_similarity(seq1, seq2):
    """
    Compute a similarity score between two DNA sequences using LCS.

    Similarity = LCS length / max(len(seq1), len(seq2))
    Returns a float between 0.0 (completely different) and 1.0 (identical).

    Args:
        seq1: first DNA sequence string
        seq2: second DNA sequence string

    Returns:
        Float similarity score between 0 and 1
    """
    if len(seq1) == 0 or len(seq2) == 0:
        return 0.0

    # Make both uppercase for consistent comparison
    seq1 = seq1.upper()
    seq2 = seq2.upper()

    # Compute the LCS length
    length = lcs_length(seq1, seq2)

    # Normalize by the longer sequence
    max_len = max(len(seq1), len(seq2))

    return length / max_len


def compare_against_candidates(input_sequence, candidates):
    """
    Compare an input DNA sequence against a list of candidate entries using LCS.

    Args:
        input_sequence: the user's input DNA string
        candidates: list of database entries (each has 'sequence' and 'species')

    Returns:
        List of candidates with 'lcs_score' added, sorted by score (highest first)
    """
    results = []

    for entry in candidates:
        # Compute LCS similarity between input and this candidate
        score = lcs_similarity(input_sequence, entry['sequence'])

        # Copy the entry and add the score
        result = {}
        for key in entry:
            result[key] = entry[key]
        result['lcs_score'] = score
        results.append(result)

    # Sort results by LCS score in descending order (highest similarity first)
    # Using merge sort to stay consistent with our sorting approach
    from algorithms.sorting import merge_sort
    sorted_results = merge_sort(results, lambda e: -e['lcs_score'])

    return sorted_results
