from model import Model

def main():
    n = 200
    r = 0.1
    f_ab = 0.2
    f_nash = 0.1
    err_lvls = [.0, .001, .002, .004, .008, .016, .032, .064, .128, .256, .512, 1.0]
    nb_moves = 16

    model = Model(n, r, err_lvls, nb_moves, f_ab, f_nash)
    print(model.particles)




if __name__ == "__main__":
    main()