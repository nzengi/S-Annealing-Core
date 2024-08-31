def aggregate_results(results):
    best_key = None
    best_energy = float('inf')

    for key, energy in results:
        if energy < best_energy:
            best_key = key
            best_energy = energy

    return best_key, best_energy
