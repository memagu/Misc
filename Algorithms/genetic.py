# https://youtu.be/uQj5UNhCPuo
# https://www.youtube.com/watch?v=nhT56blfRpE

from collections import namedtuple
from functools import partial
import random
from typing import Callable, List, Tuple

Genome = List[bool]
Population = List[Genome]
FitnessFunc = Callable[[Genome], float]
PopulateFunc = Callable[[], Population]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
Item = namedtuple("Item", ("label", "value", "mass"))


def generate_genome(length: int) -> Genome:
    return random.choices(population=(True, False), k=length)


def generate_population(size: int, genome_lenght: int) -> Population:
    return [generate_genome(genome_lenght) for _ in range(size)]


def fitness(genome: Genome, items: [Item], mass_limit: float) -> float:
    if len(genome) != len(items):
        raise ValueError("len(genome) must equal len(items)")

    value_sum = 0
    mass_sum = 0
    for gene, item in zip(genome, items):
        if gene:
            value_sum += item.value
            mass_sum += item.mass
            if mass_sum > mass_limit:
                return 0

    return value_sum


def selection_pair(population: Population, fitness_func: FitnessFunc) -> Population:
    population_fitness = [fitness_func(genome) for genome in population]
    return random.choices(population=population, weights=(population_fitness if any(population_fitness) else [1 for _ in range(len(population))]), k=2)


def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if length := len(a) != len(b):
        raise ValueError("len(a) must equal len(b)")

    if length < 2:
        return a, b

    crossover_index = random.randint(1, length - 1)

    return a[:crossover_index] + b[crossover_index:], b[:crossover_index] + a[crossover_index:]


def mutate(genome: Genome, max_mutations: int = 1, mutation_probability: float = 0.5) -> Genome:
    for _ in range(max_mutations):
        mutation_index = random.randrange(len(genome))
        genome[mutation_index] = not genome[mutation_index] if random.uniform(0, 1) < mutation_probability else genome[
            mutation_index]
    return genome


def run_evolution(populate_func: PopulateFunc,
                  fitness_func: FitnessFunc,
                  fitness_limit: float,
                  selection_func: SelectionFunc = selection_pair,
                  crossover_func: CrossoverFunc = single_point_crossover,
                  mutation_func: MutationFunc = mutate,
                  generation_limit: int = 100) -> Tuple[Population, int]:
    population = populate_func()

    for i in range(generation_limit):
        population = sorted(population, key=lambda genome: fitness_func(genome), reverse=True)

        if fitness_func(population[0]) >= fitness_limit:
            break

        next_generation = population[:2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_func(population, fitness_func)
            child_a, child_b = crossover_func(*parents[:2])
            next_generation.append(mutation_func(child_a))
            next_generation.append(mutation_func(child_b))

        population = next_generation
        print(genome_to_items(population[0], itemset))

    population.sort(key=lambda genome: fitness_func(genome), reverse=True)

    return population, i


if __name__ == "__main__":
    def genome_to_items(genome: Genome, items: [Item]) -> List[str]:
        return [item.label for i, item in enumerate(items) if genome[i]]


    items = (Item('Laptop', 500, 2200),
             Item('Headphones', 150, 160),
             Item('Coffee Mug', 60, 350),
             Item('Notepad', 40, 333),
             Item('Water Bottle', 30, 192),
             Item('Mints', 5, 25),
             Item('Socks', 10, 38),
             Item('Tissues', 15, 80),
             Item('Phone', 500, 200),
             Item('Baseball Cap', 100, 70))

    itemset = items[:5]

    population, generations = run_evolution(
        populate_func=partial(generate_population, size=100, genome_lenght=len(itemset)),
        fitness_func=partial(fitness, items=itemset, mass_limit=3000),
        fitness_limit=750,
        generation_limit=100)

    print(f"number of generations: {generations}")

    print(f"best solution: {genome_to_items(population[0], itemset)} | value: {fitness(population[0], itemset, 3000)}")
