from common import parse, driver

FILENAME = "day7.txt"

def puzzle1(data):
    min_fuel = float('inf')
    for tester in data:
        fuel_cost = 0
        for num in data:
            fuel_cost += abs(tester-num)
        min_fuel = min(fuel_cost, min_fuel)
    return min_fuel

def find_cost(distance):
    cost = 0
    step = 1
    for i in range(distance):
        cost += step
        step += 1
    return cost

def puzzle2(data):
    min_fuel = float('inf')
    cost_dict = {} # map distance to fuel cost
    for tester in range(int(max(data)/2)):
        fuel_cost = 0
        for num in data:
            
            distance = abs(tester - num)
            if distance in cost_dict:
                fuel_cost += cost_dict[distance]
            else:
                # calculate the cost, add to fuel cost, and add to dictionary
                cost = find_cost(distance)
                fuel_cost += cost
                cost_dict[distance] = cost
                
        min_fuel = min(fuel_cost, min_fuel)
    return min_fuel

if __name__ == "__main__":
    data = [int(x) for x in parse(FILENAME)[0].strip().split(',')]
    driver(puzzle1, data=data, p=1)
    driver(puzzle2, data=data, p=2)