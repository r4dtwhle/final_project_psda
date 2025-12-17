"""
Hash Table Implementation
"""


class HashTable:
    """Simple Hash Table implementation"""

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        """Hash function: string length % table size"""
        return len(key) % self.size

    def insert(self, key, value):
        """Insert key-value pair"""
        index = self.hash_function(key)
        self.table[index].append({"key": key, "value": value})

    def get_table(self):
        """Return the hash table"""
        return self.table


def create_driver_hash_table(drivers):
    """
    Create hash table from drivers list
    Hash function: name length % 10
    """
    hash_table = HashTable(10)

    for driver in drivers:
        hash_table.insert(driver["name"], driver)

    return hash_table