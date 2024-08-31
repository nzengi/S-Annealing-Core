import random

class SimulatedAnnealing:
    def __init__(self, initial_key, energy_function, move_function, temp_schedule):
        self.key = initial_key
        self.energy_function = energy_function
        self.move_function = move_function
        self.temp_schedule = temp_schedule
        self.current_energy = self.energy_function(self.key)
    
    def run(self, max_iterations):
        temp = self.temp_schedule.initial_temperature()
        stagnation_counter = 0

        for iteration in range(max_iterations):
            new_key = self.move_function(self.key)
            new_energy = self.energy_function(new_key)
            energy_diff = new_energy - self.current_energy

            if energy_diff < 0 or random.random() < self.acceptance_probability(energy_diff, temp):
                self.key = new_key
                self.current_energy = new_energy
                stagnation_counter = 0
            else:
                stagnation_counter += 1

            temp = self.temp_schedule.update_temperature(temp, energy_diff, stagnation_counter)
            
            # Optionally, checkpointing or logging can be done here
            
            if stagnation_counter > self.temp_schedule.stagnation_threshold():
                break

    def acceptance_probability(self, energy_diff, temperature):
        return random.expovariate(energy_diff / temperature)
