# Person

import random
from random import randint

Male_names = ["Liam", "Noah", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason",
              "Logan", "Alexander", "Ethan", "Jacob", "Michael", "Daniel", "Henry", "Jackson",
              "Sebastian", "Aiden", "Matthew", "Samuel", "David", "Joseph", "Carter", "Owen",
              "Wyatt", "John", "Jack", "Luke", "Jayden"]

Female_names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Charlotte", "Mia", "Amelia", "Harper",
                "Evelyn", "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila",
                "Aria", "Scarlett", "Victoria", "Madison", "Luna", "Grace", "Chloe", "Penelope", "Layla",
                "Riley", "Zoey", "Nora"]

population = []


def person_generator(amount):
    for i in range(amount):
        id = "id" + str(randint(1000000, 9999999))
        for i in range(len(population)):
            if id == population[i].identity:
                id = "id" + str(randint(1000000, 9999999))
        male_female = random.choice(["male", "female"])
        if male_female == "male":
            name = random.choice(Male_names)
        else:
            name = random.choice(Female_names)
        id = Person(id, name, male_female, 100, 25, 25, 100, "no job", 0)
        population.append(id)


class Person:
    def __init__(self, identity, name, gender, health, food, water, money, job, salary):
        self.identity = identity
        self.name = name
        self.gender = gender
        self.health = health
        self.food = food
        self.water = water
        self.money = money
        self.job = job
        self.salary = salary

