# Custom MinHeap (Priority Queue) implementation
# Used in Prim's MST algorithm to extract the minimum weight edge


class MinHeap:
    """
    A binary min-heap where each element is a (priority, item) tuple.
    The element with the smallest priority is always at the top.
    """

    def __init__(self):
        # The heap is stored as a flat list (array-based binary tree)
        self.heap = []
        # Maps item -> index in heap, for decrease_key support
        self.position = {}

    def _parent(self, index):
        """Get the parent index of a node."""
        return (index - 1) // 2

    def _left_child(self, index):
        """Get the left child index of a node."""
        return 2 * index + 1

    def _right_child(self, index):
        """Get the right child index of a node."""
        return 2 * index + 2

    def _swap(self, i, j):
        """Swap two elements in the heap and update their positions."""
        # Update position map
        self.position[self.heap[i][1]] = j
        self.position[self.heap[j][1]] = i
        # Swap elements
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, index):
        """Move an element up the heap until the heap property is restored."""
        while index > 0:
            parent = self._parent(index)
            # If current element has smaller priority than parent, swap them
            if self.heap[index][0] < self.heap[parent][0]:
                self._swap(index, parent)
                index = parent
            else:
                break

    def _sift_down(self, index):
        """Move an element down the heap until the heap property is restored."""
        size = len(self.heap)
        while True:
            smallest = index
            left = self._left_child(index)
            right = self._right_child(index)

            # Check if left child is smaller
            if left < size and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            # Check if right child is smaller
            if right < size and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            # If the smallest is not the current node, swap and continue
            if smallest != index:
                self._swap(index, smallest)
                index = smallest
            else:
                break

    def insert(self, priority, item):
        """Insert a new element with the given priority."""
        self.heap.append((priority, item))
        self.position[item] = len(self.heap) - 1
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        """Remove and return the element with the smallest priority."""
        if len(self.heap) == 0:
            return None

        # The minimum is at the root (index 0)
        min_element = self.heap[0]
        last_element = self.heap[-1]

        # Move the last element to the root
        self.heap[0] = last_element
        self.position[last_element[1]] = 0

        # Remove the last position
        del self.position[min_element[1]]
        self.heap.pop()

        # Restore heap property by sifting down
        if len(self.heap) > 0:
            self._sift_down(0)

        return min_element  # Returns (priority, item)

    def decrease_key(self, item, new_priority):
        """Decrease the priority of an existing item in the heap."""
        if item not in self.position:
            return

        index = self.position[item]
        old_priority = self.heap[index][0]

        # Only decrease, never increase
        if new_priority < old_priority:
            self.heap[index] = (new_priority, item)
            self._sift_up(index)

    def is_empty(self):
        """Check if the heap is empty."""
        return len(self.heap) == 0

    def contains(self, item):
        """Check if an item is in the heap."""
        return item in self.position

    def __len__(self):
        return len(self.heap)
