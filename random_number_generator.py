import math
import csv
import random

def main():
    while True:
        distribution_prompt = "Select type of distribution for random numbers.\n '1' for uniform distribution, '2' for exponential distribution, '0' for None"
        distribution_type = int(input(distribution_prompt))
        if distribution_type not in range(0, 3):
            print("Not valid. Try Again with 1 or 2.")
            continue

        if (distribution_type == 0):
            return

        technique_prompt = "Select technique for generating random numbers. \n 1 for LCG, 2 for additive, 3 for quadratic and 0 for None"
        technique_type = int(input(technique_prompt))
        if technique_type not in range(0, 4):
            print("Not valid. Try Again with 1, 2 or 3")
            continue
        if (technique_type == 0):
            return

        break
    rng_to_file(distribution_type, technique_type)

def rng_to_file(distribution_type, technique_type):
    if(technique_type == 1):
        random_num = lcg(249513)
        if (distribution_type == 2):
            exp = exponential_distribution(random_num)
            write_to_file("Exponential", "LCG", exp)
        else:
            write_to_file("Uniform", "LCG", random_num)

    elif(technique_type == 2):
        random_num = additive()
        if (distribution_type == 2):
            exp = exponential_distribution(random_num)
            write_to_file("Exponential", "additive", exp)
        else:
            write_to_file("Uniform", "additive", random_num)
                        
    elif(technique_type == 3):
        random_num = quadratic()
        if (distribution_type == 2 ):
            exp = exponential_distribution(random_num)
            write_to_file("Exponential","quadratic", exp)
        else:
            write_to_file("Uniform", "quadratic", random_num)


def write_to_file(distribution_type, technique_type, random_num):
    fileName = "Khadka_Ranjan_{}_{}.csv".format(distribution_type, technique_type)
    with open(fileName, 'w') as csv_file:
        write = csv.writer(csv_file)
        for number in random_num:
            write.writerow([number])

def exponential_distribution(random_num):
    mean = 0.5
    for i in range(0, 100):
        exp_value = (-mean * math.log(1-random_num[i]))
        random_num[i] = exp_value
    return random_num

def lcg(starting_value):
    c = 12345
    m = 2147483647
    rep_multiplier = 1.0 / m
    random_num = []

    current = starting_value
    for i in range(0, 100):
        next_value = (m * current + c) % m
        random_num.append(next_value * rep_multiplier)
        current = next_value
    return random_num

def additive():
    m = 2147483647
    rep_multiplier = 1.0 / m
    temp_array = []
    random_num = []
    for j in range(0, 55):
        temp_array.append(random.randint(0, m))
    for i in range(55, 155):
        next_value = (temp_array[i-24] + temp_array[i-55]) % m
        random_num.append(next_value * rep_multiplier)
        temp_array.append(next_value)
    return random_num


def quadratic():
    c = 12345
    m = 2147483647
    a = 1103515245
    b = 1
    rep_multiplier = 1.0 / m
    random_num = []
    current_num = random.randint(0, m)
    for i in range(100):
        next_value = (a * current_num * current_num + b * current_num + c) % m 
        random_num.append(next_value * rep_multiplier)
        current_num = next_value
    return random_num


main()
