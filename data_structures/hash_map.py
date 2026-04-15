# Custom HashMap implementation using separate chaining
# Used to store the DNA database: maps species name -> sequence data


class HashMap:
    """
    A hash map (dictionary) that uses separate chaining for collision resolution.
    Each bucket is a list of (key, value) pairs.
    """

    def __init__(self, capacity=64):
        # Number of buckets in the hash table
        self.capacity = capacity
        # Each bucket is a list (chain) of (key, value) pairs
        self.buckets = [[] for _ in range(capacity)]
        # Track how many key-value pairs are stored
        self.size = 0

    def _hash(self, key):
        """
        Compute a hash index for the given key.
        Uses Python's built-in hash() then maps to a bucket index.
        """
        return abs(hash(key)) % self.capacity

    def put(self, key, value):
        """Insert or update a key-value pair in the hash map."""
        index = self._hash(key)
        bucket = self.buckets[index]

        # Check if the key already exists in this bucket
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Key exists — update the value
                bucket[i] = (key, value)
                return

        # Key doesn't exist — add a new pair to the chain
        bucket.append((key, value))
        self.size += 1

    def get(self, key):
        """Retrieve the value for a given key. Returns None if not found."""
        index = self._hash(key)
        bucket = self.buckets[index]

        # Search through the chain for the matching key
        for k, v in bucket:
            if k == key:
                return v

        return None

    def contains(self, key):
        """Check if a key exists in the hash map."""
        return self.get(key) is not None

    def keys(self):
        """Return a list of all keys in the hash map."""
        all_keys = []
        for bucket in self.buckets:
            for k, v in bucket:
                all_keys.append(k)
        return all_keys

    def values(self):
        """Return a list of all values in the hash map."""
        all_values = []
        for bucket in self.buckets:
            for k, v in bucket:
                all_values.append(v)
        return all_values

    def items(self):
        """Return a list of all (key, value) pairs in the hash map."""
        all_items = []
        for bucket in self.buckets:
            for k, v in bucket:
                all_items.append((k, v))
        return all_items

    def __len__(self):
        return self.size
