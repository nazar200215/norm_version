import pygame
from simulation import Simulation


if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((1300, 700))
    simulation = Simulation(win)
    simulation.run()
