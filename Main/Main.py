from Core.SimulatedAnnealing import SimulatedAnnealing
from Utils.FileIO import checkpoint_save, load_checkpoint
from Utils.Logger import log_iteration
from Configuration.Config import Config

def main():
    config = Config()

    starting_key = config.get('starting_key', 0x2000000000000000)
    max_iterations = config.get('max_iterations', 10000)

    checkpoint = load_checkpoint()
    if checkpoint:
        starting_key, energy, iteration = checkpoint
    else:
        iteration = 0

    sa = SimulatedAnnealing(
        initial_key=starting_key,
        energy_function=energy_function,
        move_function=adaptive_move,
        temp_schedule=TemperatureSchedule(INITIAL_TEMPERATURE)
    )

    while iteration < max_iterations:
        sa.run(max_iterations)
        iteration += 1
        log_iteration(iteration, sa.key, sa.current_energy)
        checkpoint_save(sa.key, sa.current_energy, iteration)

if __name__ == '__main__':
    main()
