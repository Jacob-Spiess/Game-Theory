import numpy as np
from matrix_generator import MatrixGenerator
from particle import Particle
from nashpy import Game

class Model:
    def __init__(self, numberOfParticles, reciprocationLevel, errorLevels, nb_moves, pertubationFactor=0.2,
                 pertubationFactorNash=0.1) -> None:

        self.numberOfParticles = numberOfParticles
        self.reciprocationLevel = reciprocationLevel
        self.pertubationFactor = pertubationFactor
        self.pertubationFactorNash = pertubationFactorNash
        self.errorLevels = errorLevels
        self.matrix = MatrixGenerator(nb_moves)

        self.errorDistribution = dict()
        for lvl in errorLevels:
            self.errorDistribution[str(lvl)] = 1/len(errorLevels)

        self.particles = [[np.random.normal(), np.random.normal(),
                           np.random.randint(low=0, high=self.matrix.nb_lemke_howson_labels())] for _ in range(0, numberOfParticles)]

    def update_error_estimates(believeOpponent, attitudeOpponent, agentPayoffMatrix, opponentPayoffMatrix):

        attitudeAgent = believeOpponent

        modded_game = modify_game(game, attitudeAgent, attitudeOpponent)
        ne_agent, ne_opp = nash_opp(modded_game)
        j = ne_opp[opp_move]
        k = coop(att_opp, bel_opp)
        for l, lvl in enumerate(err_lvls):
            err_distr[str(lvl)] = err_distr[str(lvl)] # * t(j, k, l)
        normalize_dictionary(err_distr)
        err = est_error(err_lvls, err_distr)

    def update_resample_particles():
        return

    def update_perturb_particles():
        return

    def modify_game(attitudeAgent, attitudeOpponent, game):
        agentPayoffMatrix, opponentPayoffMatrix = game.payoff_matrices

        agentModifiedPayOffMatrix = agentPayoffMatrix + attitudeAgent*opponentPayoffMatrix
        opponentModifiedPayOffMatrix = opponentPayoffMatrix + attitudeOpponent*agentPayoffMatrix

        return agentModifiedPayOffMatrix, opponentModifiedPayOffMatrix
         