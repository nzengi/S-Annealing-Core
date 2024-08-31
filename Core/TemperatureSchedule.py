class TemperatureSchedule:
    def __init__(self, initial_temp):
        self.initial_temp = initial_temp

    def initial_temperature(self):
        return self.initial_temp

    def update_temperature(self, temp, energy_diff, stagnation_counter):
        if stagnation_counter > self.stagnation_threshold():
            temp = temp * 0.9
        elif energy_diff > self.significant_energy_drop():
            temp = temp * 0.99
        else:
            temp = temp * 0.95

        # Sıcaklık belirli bir alt sınırın altına düşmesin
        return max(temp, 1e-10)

    def stagnation_threshold(self):
        return 100  # Example value

    def significant_energy_drop(self):
        return 50  # Example value
