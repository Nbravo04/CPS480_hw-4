# Nicholas J Bravata and Thaddeus Warner
# CPS 480 Assignment 4 Genetic Algorithm
# Started: Oct 23, 2019

# Imports
import csv

# import numpy as np
import random
import operator

# import pandas as pd
# import matplotlib.pyplot as plt

# Seed for Random
import sys

seed = 0
maxgen = 0
popsize = 0
bestrate = 0
mutrate = 0


# Class
class Traveler:

    def __init__(self, start_city, total_dist, visited, num):
        self.start_city = start_city
        self.total_dist = total_dist
        self.visited = visited
        self.num_cities = num

    def completed(self, city):
        if city == self.start_city and self.visited == self.num_cities:
            return True
        else:
            return False

    def __str__(self):
        my_string = 'Start City: {}, Num of cities visited: {},' \
                    ' Cities left to visit: {}'.format(self.start_city, self.visited, self.num_cities - self.visited)

        return my_string


# Functions
def get_dict(file):
    csv_file = open(file, 'r')
    city_dict = {}
    csv_reader = csv.reader(csv_file)
    count = 0

    for line in csv_reader:
        if count == 0:
            count += 1
            continue
        else:
            city_dict[line[0]] = line[1:]

    return city_dict


def get_distance(cities_dict, city1, city2):
    count = -1
    for city in cities_dict.keys():
        if city == city2:
            break
        count += 1

    return cities_dict[city1][count]


def generate_individual(cities_dict, num_cities, start_city):
    initial_cities_list = []
    for key in cities_dict.keys():
        initial_cities_list.append(key)

    numbers = random.sample(range(num_cities), num_cities)
    cities_list = [start_city]
    for number in numbers:
        if initial_cities_list[number] == start_city:
            continue
        else:
            cities_list.append(initial_cities_list[number])

    return Traveler(start_city, fitness_function(cities_list, cities_dict), cities_dict, num_cities)


def generate_child(best_connection, cities_dict, num_cities, start_city):
    count = 0
    initial_cities_list = []
    for key, value in cities_dict.iteritems():
        initial_cities_list[count] = value
        count += 1

    numbers = random.sample(range(num_cities), num_cities)
    cities_list = []
    if best_connection.start == start_city:
        cities_list.append(best_connection.start)
        cities_list.append(best_connection.end)
    else:
        cities_list.append(start_city)
    for number in numbers:
        city = initial_cities_list[number]
        if city not in cities_list:
            if city == best_connection.start:
                cities_list.append(best_connection.start)
                cities_list.append(best_connection.end)
            else:
                cities_list.append(initial_cities_list[number])

    return Traveler(start_city, fitness_function(cities_list, cities_dict), cities_list, num_cities)


def mutate(child, num_cities, cities_dict, mutation_chance):
    if mutation_chance <= random.random():
        number = random.nextint(0, num_cities)
        i = child.visited.index(child.visited[number])
        if i + 1 == num_cities:
            child.visited[i], child.visited[i - 1] = child.visited[i - 1], child.visited[i]
        else:
            child.visited[i], child.visited[i + 1] = child.visited[i + 1], child.visited[i]
        child.total_distance = fitness_function(child.visited, cities_dict)
    return child


def fitness_function(solution, cities_dict):
    """
    The fitness function for the genetic algorithm sums up the total distance
    traveled following the order of cities provided by the solution given.
    This sum is the solutions score, and it is returned.
    IN THE FUTURE: Maybe don't return the score, only compare it if it is
    better. This would save on storage space, but it may negatively affect
    performance. Just an idea to think about.
    """
    score = 0
    iterator = 0
    while iterator < len(solution):
        score += get_distance(cities_dict, solution[iterator], solution[iterator + 1])
        iterator += 1
    score += get_distance(cities_dict, solution[iterator], solution[0])
    return score


def find_parent(population, cities_dict):
    for traveler in population:
        if best_distance:
            if best_distance > traveler.total_dist:
                best_distance = traveler.total_dist
                best_traveler = traveler
        else:
            best_distance = traveler.total_dist
            best_traveler = traveler
    return best_traveler


def best_parent_connection(parent, cities_dict):
    """
    This grabs the best path of the parent, which will be what is passed on
    to all the children.
    """
    best_connection = 10000000
    i = 0
    while i < parent.num_cities:
        from_city = parent.visited[i]
        i += 1
        end_city = parent.visited[i]
        this_connection = get_distance(cities_dict, from_city, end_city)
        if this_connection < best_connection:
            best_connection = this_connection
            start = from_city
            end = end_city

    this_connection = get_distance(cities_dict, parent.visited[-1], parent.start_city)
    if this_connection < best_connection:
        best_connection = this_connection
        start = parent.visited[-1]
        end = parent.start_city
    best_connection_info = {
        "start": start,
        "end": end,
        "distance": best_connection
    }
    return best_connection_info


# def generate_and_mutate(p1_connetion, p2_connection, cities_dict):
#     """
#     This function will not only generate children, but it will mutate them
#     as well. The children will contain the best path available from
#     each of the parents, and then the rest of the paths will be random.
#     """
#     return


# Main
if __name__ == "__main__":
    file1 = 'DE-all.csv'
    file2 = 'MI.xlsx'
    file3 = 'MI-part-19-miles.csv'

    cities = get_dict(file1)

    # print(get_distance(cities, 'Bear', 'Camden'))

    population = []

    for i in range(popsize):
        traveler = generate_individual(cities, len(cities.keys()), 'Bear')
        population.append(traveler)
    

    # seed = sys.argv[1]
    # maxgen = sys.argv[2]
    # popsize = sys.argv[3]
    # bestrate = sys.argv[4]
    # mutrate = sys.argv[5]
