# galaxy.py
import random
from island import Island
from utils import assign_special_islands

# galaxy.py
def generate_galaxy(num_islands, num_hubs, num_spokes):
    """Generate a galaxy as a graph of islands."""
    islands = {}
    
    # Step 1: Create islands
    for i in range(num_islands):
        islands[i] = Island(island_id=i)
    
    # Step 2: Assign final island (central node)
    final_island_id = num_islands - 1
    islands[final_island_id].type = "final"
    
    # Assign hub islands
    hub_ids = random.sample(range(num_islands), num_hubs)
    for hub_id in hub_ids:
        islands[hub_id].type = "hub"

    # Assign spoke islands (connected to hubs)
    spoke_ids = random.sample(range(num_islands), num_spokes)
    for spoke_id in spoke_ids:
        islands[spoke_id].type = "spoke"
    
    # Step 3: Connect islands (ensuring all are reachable)
    for hub_id in hub_ids:
        # Each hub connects to several random islands
        neighbors = random.sample(range(num_islands), random.randint(2, 5))
        for neighbor in neighbors:
            if neighbor != hub_id:
                islands[hub_id].add_neighbor(islands[neighbor])
                islands[neighbor].add_neighbor(islands[hub_id])

    # Step 4: Ensure all islands have at least one neighbor
    for island_id, island in islands.items():
        if not island.neighbors and island.type != "final":
            # If an island has no neighbors, connect it to a random hub or spoke
            random_island_id = random.choice(hub_ids + spoke_ids)
            island.add_neighbor(islands[random_island_id])
            islands[random_island_id].add_neighbor(island)

    # Step 5: Assign special island types (trap, buff, etc.)
    assign_special_islands(islands, num_islands)

    return islands
