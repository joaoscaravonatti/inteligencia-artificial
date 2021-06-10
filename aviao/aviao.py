from random import Random
from time import time
from inspyred import ec
from inspyred.ec import terminators
import numpy as np

def generate_(random, args):
    size = args.get('num_inputs', 12)
    return [random.randint(0, 16000) for i in range(size)] 

def evaluate_(candidates, args):
    fitness = []
    for cs in candidates:
        fit = perform_fitness(cs[0], cs[1], cs[2], cs[3], cs[4], cs[5], cs[6], cs[7], cs[8], cs[9], cs[10], cs[11])
        fitness.append(fit)
    return fitness

def perform_fitness(C1D, C2D, C3D, C4D, C1C, C2C, C3C, C4C, C1T, C2T, C3T, C4T):
    c1d = np.round(C1D)
    c2d = np.round(C2D)
    c3d = np.round(C3D)
    c4d = np.round(C4D)
    c1c = np.round(C1C)
    c2c = np.round(C2C)
    c3c = np.round(C3C)
    c4c = np.round(C4C)
    c1t = np.round(C1T)
    c2t = np.round(C2T)
    c3t = np.round(C3T)
    c4t = np.round(C4T)

    fit = float((((c1d + c1c + c1t) * 0.31) +
                ((c2d + c2c + c2t) * 0.38) +
                ((c3d + c3c + c3t) * 0.35) +
                ((c4d + c4c + c4t) * 0.285)) / 42565.92)

    d = c1d + c2d + c3d + c4d
    c = c1d + c2c + c3c + c4c
    t = c1t + c2t + c3t + c4t
    total_weight = d + c + t               

    nh = 13

    # peso máximo no compartimento dianteiro
    h1 = np.maximum(0, float(d - 10000)) / (10000 / nh)
    # peso máximo no compartimento central
    h2 = np.maximum(0, float(c - 16000)) / (16000 / nh)
    # peso máximo no compartimento traseira
    h3 = np.maximum(0, float(t - 8000)) / (8000 / nh)

    # volume máximo no compartimento dianteiro
    h4 = np.maximum(0, float(((((c1d * 0.480) + (c2d * 0.650) + (c3d * 0.580) + (c4d * 0.390)) - 6800)))) / (6800 / nh)
    # volume máximo no compartimento central
    h5 = np.maximum(0, float(((((c1c * 0.480) + (c2c * 0.650) + (c3c * 0.580) + (c4c * 0.390)) - 8700)))) / (6800 / nh)
    # volume máximo no compartimento traseiro
    h6 = np.maximum(0, float(((((c1t * 0.480) + (c2t * 0.650) + (c3t * 0.580) + (c4t * 0.390)) - 5300)))) / (6800 / nh)

    # peso máximo da carga 1
    h7 = np.maximum(0, float((c1d + c1c + c1t) - 18000)) / (18000 / nh)
    # peso máximo da carga 2
    h8 = np.maximum(0, float((c2d + c2c + c2t) - 15000)) / (15000 / nh)
    # peso máximo da carga 3
    h9 = np.maximum(0, float((c3d + c3c + c3t) - 23000)) / (23000 / nh)
    # peso máximo da carga 4
    h10 = np.maximum(0, float((c4d + c3c + c4t) - 12000)) / (12000 / nh)

    # proporção dianteira
    h11 = np.maximum(0, float(((d / total_weight) - 0.29411764706))) / (0.29411764706 / nh)
    # proporção central
    h12 = np.maximum(0, float(((c / total_weight) - 0.47058823529))) / (0.47058823529 / nh)
    # proporção traseira
    h13 = np.maximum(0, float(((t / total_weight) - 0.23529411765))) / (0.23529411765 / nh)

    h = h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + h10 + h11 + h12 + h13

    fit = fit - h

    return fit

def solution_evaluation(C1D, C2D, C3D, C4D, C1C, C2C, C3C, C4C, C1T, C2T, C3T, C4T):
    c1d = np.round(C1D)
    c2d = np.round(C2D)
    c3d = np.round(C3D)
    c4d = np.round(C4D)
    c1c = np.round(C1C)
    c2c = np.round(C2C)
    c3c = np.round(C3C)
    c4c = np.round(C4C)
    c1t = np.round(C1T)
    c2t = np.round(C2T)
    c3t = np.round(C3T)
    c4t = np.round(C4T)

    c1 = c1d + c1c + c1t
    c2 = c2d + c2c + c2t
    c3 = c3d + c3c + c3t
    c4 = c4d + c4c + c4t

    profit_c1 = float(c1 * 0.31)
    profit_c2 = float(c2 * 0.38)
    profit_c3 = float(c3 * 0.35)
    profit_c4 = float(c4 * 0.285)

    profit = float(profit_c1 + profit_c2 + profit_c3 + profit_c4)

    cd = c1d + c2d + c3d + c4d
    cc = c1c + c2c + c3c + c4c
    ct = c1t + c2t + c3t + c4t
    total_weight = cd + cc + ct

    print('\nRelatório')
    print(f'Lucro total: R$ %.2f - Peso total: {total_weight}' % profit)
    print(f'Carga 1: {c1}kg - {profit_c1}')
    print(f'Carga 2: {c2}kg - {profit_c2}')
    print(f'Carga 3: {c3}kg - {profit_c3}')
    print(f'Carga 4: {c4}kg - {profit_c4}')
    print(f'\nCompartimento dianteiro ({cd}kg - {cd / total_weight}):')
    print(f'Carga 1: {c1d}kg')
    print(f'Carga 2: {c2d}kg')
    print(f'Carga 3: {c3d}kg')
    print(f'Carga 4: {c4d}kg')
    print(f'\nCompartimento central ({cc}kg - {cc / total_weight}):')
    print(f'Carga 1: {c1c}kg')
    print(f'Carga 2: {c2c}kg')
    print(f'Carga 3: {c3c}kg')
    print(f'Carga 4: {c4c}kg')
    print(f'\nCompartimento traseiro ({ct}kg - {ct / total_weight}):')
    print(f'Carga 1: {c1t}kg')
    print(f'Carga 2: {c2t}kg')
    print(f'Carga 3: {c3t}kg')
    print(f'Carga 4: {c4t}kg')

def main():
  rand = Random()
  rand.seed(int(time()))

  ea = ec.GA(rand)
  ea.selector = ec.selectors.tournament_selection
  ea.variator = [ec.variators.uniform_crossover,
                  ec.variators.gaussian_mutation]

  ea.replacer = ec.replacers.steady_state_replacement

  ea.terminator = terminators.generation_termination

  ea.observer = [ec.observers.stats_observer, ec.observers.file_observer]

  final_pop = ea.evolve(generator=generate_,
                        evaluator=evaluate_,
                        pop_size=10000,
                        maximize=True,
                        bounder=ec.Bounder(0, 16000),
                        max_generations=1000,
                        num_inputs=12,
                        crossover_rae=1.0,
                        num_crossover_points=1,
                        mutation_rate=0.5,
                        num_elites=1,
                        num_selected=12,
                        tournament_size=12,
                        statistics_file=open('aviao_statistics.csv', 'w'),
                        individuals_file=open('aviao_individuals.csv', 'w'))

  final_pop.sort(reverse=True)
  print(final_pop[0])

  perform_fitness(final_pop[0].candidate[0], final_pop[0].candidate[1], final_pop[0].candidate[2], final_pop[0].candidate[3], final_pop[0].candidate[4], final_pop[0].candidate[5], final_pop[0].candidate[6], final_pop[0].candidate[7], final_pop[0].candidate[8], final_pop[0].candidate[9], final_pop[0].candidate[10], final_pop[0].candidate[11])
  solution_evaluation(final_pop[0].candidate[0], final_pop[0].candidate[1], final_pop[0].candidate[2], final_pop[0].candidate[3], final_pop[0].candidate[4], final_pop[0].candidate[5], final_pop[0].candidate[6], final_pop[0].candidate[7], final_pop[0].candidate[8], final_pop[0].candidate[9], final_pop[0].candidate[10], final_pop[0].candidate[11])

if __name__ == '__main__':
  main()
