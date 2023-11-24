import math
import time

import numpy as np
from numpy import random


def f(x_list, a_list, b_list):
    if correct_function(*x_list):
        # Check if the lengths of a_list and b_list match the length of x_list
        if len(a_list) == len(b_list) == len(x_list):

            np.seterr(all='raise')

            try:
                f_value = sum(a * (x ** b) for a, x, b in zip(a_list, x_list, b_list))
            except FloatingPointError:
                return False
            return f_value
        else:
            raise ValueError("Lengths of a_list, b_list, and x_list must be the same.")
    return False


def correct_function(x0, x1, x2, x3, x4, x5, x6, x7, x8, x9):
    if x0 * x2 * x7 > 10000 and x0 * x3 * x6 <= 1000 and x1 * x4 * x9 in range(-1000,
                                                                               1000) and x1 * x4 * x9 != 0 and x4 + x5 + x6 <= 10:  # ostatni warunek zamieniam na równoznaczny w celu przyspieszenia obliczeń (10! = 3,628,800)

        return True
    # print(f"x0 * x2 * x7 > 10000: {x0 * x2 * x7 > 10000}")
    # print(f"x0 * x3 * x6 <= 1000: {x0 * x3 * x6 <= 1000}")
    # print(f"x1 * x4 * x9 in range(-1000, 1000): {x1 * x4 * x9 in range(-1000, 1000)}")
    # print(f"x1 * x4 * x9 != 0: {x1 * x4 * x9 != 0}")
    # print(f"x4 + x5 + x6 <= 10: {x4 + x5 + x6 <= 10}")
    return False

def correct_function_ranged(x_values, ranges):
    for i in range(len(ranges)):
        if not(x_values[i] in ranges[i]):
            return False

    x0, x1, x2, x3, x4, x5, x6, x7, x8, x9 = x_values
    if x0 * x2 * x7 > 10000 and x0 * x3 * x6 <= 1000 and x1 * x4 * x9 in range(-1000,
                                                                               1000) and x1 * x4 * x9 != 0 and x4 + x5 + x6 <= 10:  # ostatni warunek zamieniam na równoznaczny w celu przyspieszenia obliczeń (10! = 3,628,800)

        return True
    # print(f"x0 * x2 * x7 > 10000: {x0 * x2 * x7 > 10000}")
    # print(f"x0 * x3 * x6 <= 1000: {x0 * x3 * x6 <= 1000}")
    # print(f"x1 * x4 * x9 in range(-1000, 1000): {x1 * x4 * x9 in range(-1000, 1000)}")
    # print(f"x1 * x4 * x9 != 0: {x1 * x4 * x9 != 0}")
    # print(f"x4 + x5 + x6 <= 10: {x4 + x5 + x6 <= 10}")
    return False

def generate_ranges():
    x0_r = list(range(0, 51))
    x1_r = []
    for i in range(40, 61):
        if (i - 1) % 10 in range(0, 7):
            x1_r.append(i)
    x2_r = list(range(1, 101))
    x3_r = list(range(0, 21))
    x4_r = list(range(2, 101))
    x5_r = list(range(0, 3))
    x6_r = [1]
    x7_r = [20]
    x8_r = list(range(0, 10))
    x9_r = list(range(5, 100, 2))
    return x0_r, x1_r, x2_r, x3_r, x4_r, x5_r, x6_r, x7_r, x8_r, x9_r


def indexes_to_values(indexes, ranges):
    n = min(len(indexes), len(ranges))
    values = []
    for i in range(n):
        values.append(ranges[i][indexes[i]])
    return values



def simulated_annealing(a_list, b_list, max_iterations=10000, initial_temperature=1.0, cooling_rate=0.95, step_size = 1):
    def generate_random_solution(ranges):
        while True:
            solution = [random.choice(r) for r in ranges]
            if correct_function_ranged(solution, ranges):
                if f(solution, a_list, b_list):
                    break
                else:
                    continue
        return solution

    def neighbor(solution, ranges, step_size=1):
        while True:
            neighbor_solution = list(solution)
            index_to_change = random.randint(0, len(solution))
            new_value = neighbor_solution[index_to_change] + random.randint(-step_size, step_size)
            neighbor_solution[index_to_change] = new_value
            if new_value in ranges[index_to_change] and correct_function_ranged(neighbor_solution, ranges):
                neighbor_solution[index_to_change] = new_value
                if f(neighbor_solution, a_list, b_list):
                    break
                else:
                    continue
        return neighbor_solution
        # print(f(neighbor_solution, a_list, b_list))



    def acceptance_probability(current_value, new_value, temperature):
        delta_e = new_value - current_value

        if delta_e <= 0:
            return 1.0  # Accept improvement

        probability = math.exp(-delta_e / temperature)
        return probability  # Accept worse solution with probability p

    start_time = time.time()
    x0_r, x1_r, x2_r, x3_r, x4_r, x5_r, x6_r, x7_r, x8_r, x9_r = generate_ranges()
    ranges = (x0_r, x1_r, x2_r, x3_r, x4_r, x5_r, x6_r, x7_r, x8_r, x9_r)

    current_solution = generate_random_solution(ranges)
    current_value = f(current_solution, a_list, b_list)
    best_solution = current_solution
    best_value = current_value

    for iteration in range(max_iterations):
        temperature = initial_temperature * (cooling_rate ** iteration)
        # print(f"temperature: {temperature}")
        new_solution = neighbor(current_solution, ranges, step_size)
        new_value = f(new_solution, a_list, b_list)
        # print(f"new_solution {new_solution}")
        # print(f"new_value {new_value}")
        if correct_function(*new_solution) and (new_value > current_value or random.uniform(0, 1) < acceptance_probability(current_value, new_value, temperature)):
            current_solution = new_solution
            current_value = new_value

        if current_value > best_value:
            best_solution = current_solution
            best_value = current_value

    end_time = time.time()
    exec_time = end_time - start_time

    return best_solution, best_value, exec_time, "O(n*m)" # m number of variables


def hill_climbing(a_values, b_values):
    start_time = time.time()
    x0_r, x1_r, x2_r, x3_r, x4_r, x5_r, x6_r, x7_r, x8_r, x9_r = generate_ranges()
    ranges = (x0_r, x1_r, x2_r, x3_r, x4_r, x5_r, x6_r, x7_r, x8_r, x9_r)
    # Initialize current solution and best solution
    current_indexes = [random.choice(len(x0_r)), random.choice(len(x1_r)), random.choice(len(x2_r)),
                       random.choice(len(x3_r)), random.choice(len(x4_r)), random.choice(len(x5_r)),
                       random.choice(len(x6_r)), random.choice(len(x7_r)), random.choice(len(x8_r)),
                       random.choice(len(x9_r))]
    current_variables = indexes_to_values(current_indexes, ranges)

    while not correct_function(*current_variables):
        current_indexes = [random.choice(len(x0_r)), random.choice(len(x1_r)), random.choice(len(x2_r)),
                           random.choice(len(x3_r)), random.choice(len(x4_r)), random.choice(len(x5_r)),
                           random.choice(len(x6_r)), random.choice(len(x7_r)), random.choice(len(x8_r)),
                           random.choice(len(x9_r))]
        current_variables = variables = indexes_to_values(current_indexes, ranges)

    best_solution = current_variables
    best_value = f(current_variables, a_values, b_values)

    while True:
        # Generate all possible neighboring solutions
        neighboring_solutions = []
        for i in range(len(ranges)):
            # print(f"i: {i}")
            # print(f"current_indexes: {current_indexes}")
            # print(f"best_value: {best_value}")

            if 0 < (current_indexes[i] - 1) < len(ranges[i]):
                neighbor_indexes = list(current_indexes)
                neighbor_indexes[i] = neighbor_indexes[i] - 1
                neighbor_variables = indexes_to_values(neighbor_indexes, ranges)
                if correct_function(*neighbor_variables):
                    f_value = f(neighbor_variables, a_values, b_values)
                    if f_value > best_value:
                        neighbouring_solution = (neighbor_indexes, f(neighbor_variables, a_values, b_values))
                        neighboring_solutions.append(neighbouring_solution)

            if 0 < (current_indexes[i] + 1) < len(ranges[i]):
                neighbor_indexes = list(current_indexes)
                neighbor_indexes[i] = neighbor_indexes[i] + 1
                neighbor_variables = indexes_to_values(neighbor_indexes, ranges)
                if correct_function(*neighbor_variables):
                    neighbor_indexes = list(current_indexes)
                    neighbor_indexes[i] = neighbor_indexes[i] + 1
                    neighbor_variables = indexes_to_values(neighbor_indexes, ranges)
                    if correct_function(*neighbor_variables):
                        f_value = f(neighbor_variables, a_values, b_values)
                        if f_value > best_value:
                            neighbouring_solution = (neighbor_indexes, f(neighbor_variables, a_values, b_values))
                            neighboring_solutions.append(neighbouring_solution)
        # Check if there are no valid neighboring solutions
        if not neighboring_solutions:
            break

        # Find the best neighboring solution
        best_neighbor = max(neighboring_solutions, key=lambda x: x[1])

        # Update the best solution if the neighboring solution is better
        if best_neighbor[1] > best_value:
            best_solution = indexes_to_values(best_neighbor[0], ranges)
            best_value = best_neighbor[1]

        # Check if the current solution is the best solution
        if current_indexes == best_neighbor[0]:
            break

        # Update the current solution
        current_indexes = best_neighbor[0]

    end_time = time.time()
    exec_time = end_time - start_time

    return best_solution, best_value, exec_time, "O(n^2)"


def select_parents(population, fitness_values):
    # Sort the population and fitness values together
    sorted_population = sorted(zip(population, fitness_values), key=lambda x: x[1], reverse=True)

    # Select the top two parents
    parent1 = sorted_population[0][0]
    parent2 = sorted_population[1][0]

    return parent1, parent2


def crossover(parent1, parent2):
    # Select a random crossover point
    crossover_point = random.choice(len(parent1))

    # Create two offspring
    child1 = list(parent1)
    child2 = list(parent2)

    for i in range(len(parent1)):
        if i < crossover_point:
            child1[i] = parent1[i]
            child2[i] = parent2[i]
        else:
            child1[i] = parent2[i]
            child2[i] = parent1[i]

    return child1, child2


def mutate(child, ranges):
    # Randomly mutate one of the genes
    while True:
        mutation_point = random.choice(len(child))

        # Mutate the gene by adding or subtracting a small random value
        mutated_gene = child[mutation_point] + random.choice(range(-1, 2))

        # Check if the mutated gene is within the valid range
        if mutated_gene in ranges[mutation_point]:
            child[mutation_point] = mutated_gene
            break

    return child


def genetic_algorithm(population_size, max_generations, a_values, b_values):
    start_time = time.time()
    # Initialize the population
    x0_r, x1_r, x2_r, x3_r, x4_r, x5_r, x6_r, x7_r, x8_r, x9_r = generate_ranges()
    ranges = (x0_r, x1_r, x2_r, x3_r, x4_r, x5_r, x6_r, x7_r, x8_r, x9_r)
    population = []
    for i in range(population_size):
        individual = []
        while True:
            for j in range(10):
                individual.append(random.choice(ranges[j]))
            if correct_function(*individual):
                break
            else: individual = []
        population.append(individual)
    # Evaluate the initial population
    fitness_values = [f(individual, a_values, b_values) if correct_function(*individual) else 0 for individual in population]

    # Iterate for the maximum number of generations
    for generation in range(max_generations):
        # Select the top two parents
        parent1, parent2 = select_parents(population, fitness_values)

        # Create offspring using crossover
        child1, child2 = crossover(parent1, parent2)

        # Mutate the offspring
        mutated_child1 = mutate(child1, ranges)
        mutated_child2 = mutate(child2, ranges)

        # Add the offspring to the population
        population.append(mutated_child1)
        population.append(mutated_child2)
        # Evaluate the new population
        fitness_values = [f(individual, a_values, b_values) if correct_function(*individual) else 0 for individual in population]

        # Remove the least fit individuals from the population
        if len(population) > population_size:
            new_population = sorted(zip(population, fitness_values), key=lambda x: x[1], reverse=True)[:population_size]
            population = []
            for individual, fitness in new_population:
                population.append(individual)

    # Find the best individual
    best_individual = sorted(zip(population, fitness_values), key=lambda x: x[1], reverse=True)[0][0]
    best_fitness = f(best_individual, a_values, b_values)
    end_time = time.time()
    exec_time = end_time - start_time
    return best_individual, best_fitness, exec_time, "O(kn^2)"
