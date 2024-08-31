def checkpoint_save(key, energy, iteration, filename='checkpoint.txt'):
    with open(filename, 'w') as f:
        f.write(f'{key},{energy},{iteration}\n')

def load_checkpoint(filename='checkpoint.txt'):
    try:
        with open(filename, 'r') as f:
            line = f.readline().strip()
            key, energy, iteration = line.split(',')
            return int(key), float(energy), int(iteration)
    except FileNotFoundError:
        return None
