# Run Simulation

import business_struct
import person
import environment


# construct simulation


def day(days):
    count = 1
    for i in range(days):
        for r in range(len(environment.land)):
            environment.land[r].day()
            #print("Day: " + str(count) + " for land with ID: " + environment.land[r].id)
            #print(environment.land[r].storage)
            if environment.land[r].storage >= (2*environment.land[r].size):
                environment.land[r].storage = (2*environment.land[r].size)
        count = count + 1


# generate land, define growth rate, construct 10 people, one farm, one bakery and hire persons


environment.land_generator("grass", 100)
person.person_generator(10)

business_struct.farm = business_struct.business_generator("Timmy Farm", 0, 5000, "corn", 20, "farmer")
business_struct.farm.hire(3, person.population)

business_struct.bakery = business_struct.business_generator("Joe's Bread", 0, 1000, "bread", 15, "baker")
business_struct.bakery.hire(2, person.population)

business_struct.farm.resource_source(environment.land) # make resource_source work with both environment and business file

business_struct.bakery.resource_source("Timmy Farm")
business_struct.bakery.import_all_goods()

business_struct.farm.productivity()
business_struct.bakery.productivity()

# Simulation start
day(100)




















