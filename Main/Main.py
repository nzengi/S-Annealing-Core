from Core.SimulatedAnnealing import SimulatedAnnealing
from Core.EnergyFunction import energy_function
from Core.MoveGenerator import adaptive_move
from Core.TemperatureSchedule import TemperatureSchedule
from Utils.FileIO import checkpoint_save, load_checkpoint
from Utils.Logger import log_iteration
from Configuration.Config import Config

def main():
    config = Config()

    starting_key = int(config.get('starting_key', 0x7ffffffffffffffff), 16)
    max_iterations = config.get('max_iterations', 10000)
    initial_temperature = config.get('initial_temperature', 1000)  # INITIAL_TEMPERATURE yerine config'den alınan değer

    checkpoint = load_checkpoint()
    if checkpoint:
        starting_key, energy, iteration = checkpoint
    else:
        iteration = 0

    sa = SimulatedAnnealing(
        initial_key=starting_key,
        energy_function=energy_function,
        move_function=adaptive_move,
        temp_schedule=TemperatureSchedule(initial_temperature)
    )

    while iteration < max_iterations:
        sa.run(max_iterations)
        iteration += 1
        log_iteration(iteration, sa.key, sa.current_energy)
        checkpoint_save(sa.key, sa.current_energy, iteration)
    
    print(f"Final Key: {sa.key}, Final Energy: {sa.current_energy}")

if __name__ == '__main__':
    main()
