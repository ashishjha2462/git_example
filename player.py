# player.py

class Player:
    """Class representing a player in the game."""
    def __init__(self, player_id, starting_island):
        self.id = player_id
        self.current_island = starting_island
        self.resources = 100  # Initial resources for the player
        self.abilities = []
        self.move_history = []

    def move_to_island(self, new_island):
        """Move the player to a new island."""
        self.current_island = new_island

    def add_resource(self, amount):
        """Add resources to the player's pool."""
        self.resources += amount

    def use_ability(self, ability):
        """Use an ability (placeholder for now)."""
        if ability in self.abilities:
            print(f"Player {self.id} used {ability}!")
            self.abilities.remove(ability)

    def __repr__(self):
        """Represent the player with id and current island."""
        return f"Player(id={self.id}, island={self.current_island.id})"
