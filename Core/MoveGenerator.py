import random

def make_large_move(key):
    # Modify multiple bits in the key
    return key ^ (1 << random.randint(0, 255))  # Example of flipping a bit

def make_small_move(key):
    # Modify a single bit or make a small change
    return key ^ (1 << random.randint(0, 255))  # Example of flipping a bit

def adaptive_move(key, energy):
    if energy > high_energy_threshold():
        return make_large_move(key)
    else:
        return make_small_move(key)
