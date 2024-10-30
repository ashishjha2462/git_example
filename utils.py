# utils.py

import random

def assign_special_islands(islands, num_islands):
    """Assign special island types (trap, buff, etc.)."""
    num_traps = num_islands // 10
    num_buffs = num_islands // 10

    trap_ids = random.sample(range(num_islands - 1), num_traps)
    buff_ids = random.sample(range(num_islands - 1), num_buffs)

    for trap_id in trap_ids:
        islands[trap_id].type = "trap"

    for buff_id in buff_ids:
        islands[buff_id].type = "buff"
