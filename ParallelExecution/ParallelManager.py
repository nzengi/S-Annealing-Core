from multiprocessing import Pool

def simulated_annealing_parallel(starting_points, sa_class, max_iterations):
    with Pool(processes=len(starting_points)) as pool:
        results = pool.map(lambda point: run_sa_instance(point, sa_class, max_iterations), starting_points)
    return results

def run_sa_instance(starting_point, sa_class, max_iterations):
    sa_instance = sa_class(starting_point)
    sa_instance.run(max_iterations)
    return sa_instance.key, sa_instance.current_energy
