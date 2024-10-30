# game.py
import random
from galaxy import generate_galaxy
from player import Player

def main():
    # Define game settings (e.g., galaxy size)
    num_islands = 100
    num_hubs = 5
    num_spokes = 10

    # Step 1: Generate galaxy
    galaxy = generate_galaxy(num_islands=num_islands, num_hubs=num_hubs, num_spokes=num_spokes)
    
    # Step 2: Initialize players
    player1 = Player(player_id=1, starting_island=galaxy[0])
    player2 = Player(player_id=2, starting_island=galaxy[1])
    
    # Step 3: Example game loop
    turn = 0
    while True:
        current_player = player1 if turn % 2 == 0 else player2
        print(f"Turn {turn}: Player {current_player.id}'s move.")
        
        neighbors = current_player.current_island.neighbors
        
        # Filter neighbors to avoid going back to the last island if possible
        if len(neighbors) > 1 and current_player.move_history:
            last_island = current_player.move_history[-1]
            neighbors = [n for n in neighbors if n != last_island]

        # Move to a random neighbor
        next_island = random.choice(neighbors)
        current_player.move_to_island(next_island)
        
        # Update player's current island and move history
        current_player.move_history.append(current_player.current_island)
        if len(current_player.move_history) > 3:  # Keep only the last 3 moves in history
            current_player.move_history.pop(0)
        
        current_player.current_island = next_island
        print(f"Player {current_player.id} moved to Island {current_player.current_island.id} ({current_player.current_island.type})")
        
        # End condition (reaching the final island)
        if next_island.type == "final":
            print(f"Player {current_player.id} wins!")
            break
        
        turn += 1

if __name__ == "__main__":
    main()
