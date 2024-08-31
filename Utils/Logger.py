import logging

def setup_logger():
    logger = logging.getLogger('SimulatedAnnealing')
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler('simulated_annealing.log')
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logger.addHandler(handler)
    return logger

logger = setup_logger()

def log_iteration(iteration, key, energy):
    logger.info(f'Iteration {iteration}: Key = {key}, Energy = {energy}')
