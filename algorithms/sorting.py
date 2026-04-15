# Merge Sort implementation for sorting DNA sequences by GC content
# GC content = ratio of G and C bases in a DNA sequence
# Similar GC content suggests higher chance of being the same species


def calculate_gc_content(sequence):
    """
    Calculate the GC content of a DNA sequence.
    GC content = (number of G + number of C) / total length
    Returns a float between 0 and 1.
    """
    if len(sequence) == 0:
        return 0.0

    # Count G and C bases (case-insensitive)
    sequence = sequence.upper()
    gc_count = 0
    for base in sequence:
        if base == 'G' or base == 'C':
            gc_count += 1

    return gc_count / len(sequence)


def merge_sort(entries, key_func):
    """
    Sort a list of entries using merge sort algorithm.

    Args:
        entries: list of items to sort
        key_func: function that extracts the sort key from each item

    Returns:
        A new sorted list (does not modify the original)

    Time complexity: O(n log n)
    """
    # Base case: a list of 0 or 1 elements is already sorted
    if len(entries) <= 1:
        return list(entries)

    # Split the list into two halves
    mid = len(entries) // 2
    left_half = entries[:mid]
    right_half = entries[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left_half, key_func)
    right_sorted = merge_sort(right_half, key_func)

    # Merge the two sorted halves together
    return _merge(left_sorted, right_sorted, key_func)


def _merge(left, right, key_func):
    """
    Merge two sorted lists into one sorted list.
    Uses the key_func to compare elements.
    """
    result = []
    i = 0  # pointer for left list
    j = 0  # pointer for right list

    # Compare elements from both lists and add the smaller one
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any remaining elements from the right list
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def sort_by_gc_content(entries):
    """
    Sort DNA database entries by their GC content using merge sort.
    Each entry must have a 'sequence' field.
    Adds a 'gc_content' field to each entry.

    Returns:
        A new sorted list of entries with gc_content added.
    """
    # Calculate GC content for each entry
    entries_with_gc = []
    for entry in entries:
        # Make a copy so we don't modify the original
        entry_copy = {}
        for key in entry:
            entry_copy[key] = entry[key]
        entry_copy['gc_content'] = calculate_gc_content(entry['sequence'])
        entries_with_gc.append(entry_copy)

    # Sort using merge sort with GC content as the key
    sorted_entries = merge_sort(entries_with_gc, lambda e: e['gc_content'])

    return sorted_entries


def filter_by_gc_threshold(sorted_entries, input_gc, threshold=0.10):
    """
    Filter entries to only include those within ±threshold of the input GC content.

    Args:
        sorted_entries: list of entries sorted by GC content (each has 'gc_content')
        input_gc: GC content of the input sequence (float 0-1)
        threshold: maximum allowed difference (default 0.10 = 10 percentage points)

    Returns:
        List of entries that pass the GC content filter.
    """
    filtered = []
    for entry in sorted_entries:
        # Check if this entry's GC content is within the threshold
        difference = abs(entry['gc_content'] - input_gc)
        if difference <= threshold:
            # Mark as included
            entry['gc_filtered'] = True
            filtered.append(entry)
        else:
            entry['gc_filtered'] = False

    return filtered
