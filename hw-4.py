# Nicholas J Bravata and Thaddus Warner
# CPS 480 Assignment 4 Genetic Algorithm
# Started: Oct 23, 2019

# Imports
import csv

import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt

# Seed for Random
seed = 0


# Class
class Traveler:

    def __init__(self, city, num):
        start_city = city
        total_dist = 0
        visited = []
        num_cities = num - 1

    def completed(self, city):
        if city == self.start_city and self.visited == self.num_cities:
            return True
        else:
            return False


# Functions
def get_dict(file):
    csv_file = open(file, 'r')
    city_dict = {}
    csv_reader = csv.reader(csv_file)
    count = 0

    for line in csv_reader:
        if count == 0:
            count += 1
            city_dict['idx'] = line[1:]
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


# Main
if __name__ == "__main__":
    file1 = 'DE-all.csv'
    file2 = 'MI.xlsx'
    file3 = 'MI-part-19-miles.csv'

    cities = get_dict(file1)

    print(get_distance(cities, 'Bear', 'Camden'))
