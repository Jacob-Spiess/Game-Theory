from random import random
import numpy as np

class MatrixGenerator:

    def __init__(self, nb_moves):
        self.nb_players = 2
        self.nb_moves = nb_moves

    def random_matrix(self):
        matrix_1 = np.array([[random() for _ in range(self.nb_moves)] for _ in range(self.nb_moves)])
        matrix_2 = np.array([[random() for _ in range(self.nb_moves)] for _ in range(self.nb_moves)])
        
        np.random.rand(size,size), np.random.rand(size, size)

        matrix = [[(1, 4), (2, 5)], [(3, 6), (4, 7)]]

        return matrix




    def nb_lemke_howson_labels(self):
        ex, _ = self.random_matrix()
        return sum(ex.shape)