import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Simulated Annealing Bitcoin Puzzle Solver')
    parser.add_argument('--config', type=str, help='Path to configuration file', default='config.json')
    return parser.parse_args()
