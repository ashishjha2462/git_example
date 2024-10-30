# island.py

class Island:
    """Class representing each island in the game."""
    def __init__(self, island_id, island_type="normal"):
        self.id = island_id
        self.type = island_type
        self.neighbors = []

    def add_neighbor(self, neighbor):
        """Add a neighboring island."""
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __repr__(self):
        """Represent the island with its id and type."""
        return f"Island(id={self.id}, type={self.type})"
