import numpy as np
from matrix_generator import MatrixGenerator
from particle import Particle
#from nashpy import Game
from quantecon.game_theory import lemke_howson, NormalFormGame, Player

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

    def update_error_estimates(self, believeOpponent, attitudeOpponent, normalFormGame):

        attitudeAgent = believeOpponent

        modifiedGame = self.modify_game(normalFormGame, attitudeAgent, attitudeOpponent)
 
        starting_label = self.estimate_opponents_method()
        _, nash_opponent = lemke_howson(modifiedGame, starting_label)


#        ne_agent, ne_opp = nash_opponent(moddified_game)
#        j = ne_opp[opp_move]
#        k = coop(att_opp, bel_opp)
#        for l, lvl in enumerate(err_lvls):
#            err_distr[str(lvl)] = err_distr[str(lvl)] # * t(j, k, l)
#        normalize_dictionary(err_distr)
#        err = est_error(err_lvls, err_distr)


    def update_resample_particles():
        return

    def update_perturb_particles():
        return


    def estimate_opponents_method(self):
        numbers = [p[2] for p in self.particles]
        counts = dict()
        for n in numbers:
            if str(n) in counts:
                counts[str(n)] += 1
            else:
                counts[str(n)] = 1
        keys = list(counts.keys())
        values = np.array(list(counts.values()))
        max_id = np.argmax(values)
        return keys[max_id]


    def modify_game(self, attitudeAgent, attitudeOpponent, game: NormalFormGame):
        agentPayoffMatrix, opponentPayoffMatrix = game.players[0].payoff_array, game.players[1].payoff_array

        agentModifiedPayOffMatrix = agentPayoffMatrix + attitudeAgent * opponentPayoffMatrix.T
        opponentModifiedPayOffMatrix = opponentPayoffMatrix + attitudeOpponent * agentPayoffMatrix.T

        return NormalFormGame(agentModifiedPayOffMatrix, opponentModifiedPayOffMatrix)

