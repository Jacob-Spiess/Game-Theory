from model import Model
from quantecon.game_theory import NormalFormGame
import numpy as np

def main():
    n = 200
    r = 0.1
    f_ab = 0.2
    f_nash = 0.1
    err_lvls = [.0, .001, .002, .004, .008, .016, .032, .064, .128, .256, .512, 1.0]
    nb_moves = 2

    model = Model(n, r, err_lvls, nb_moves, f_ab, f_nash)
#    A, B = model.matrix.random_matrix()

    A = [[(1, 4), (2, 5)], [(3, 6), (4, 7)]]
    normalFormGame = NormalFormGame(A)
    print(normalFormGame)

    print(model.modify_game(-1,1,normalFormGame))




if __name__ == "__main__":
    main()