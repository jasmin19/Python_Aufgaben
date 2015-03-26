AB = int(raw_input("Strecke AB:"))
BC = int(raw_input("Strecke BC:"))
CD = int(raw_input("Strecke CD:"))
DE = int(raw_input("Strecke DE:"))
EA = int(raw_input("Strecke EA:"))

ways_list = [AB, BC, CD, DE, EA]

all_ways = AB+BC+CD+DE+EA

possible_ways = []

for i in range(0, len(ways_list)-1, 1):
    cuted_list = list(ways_list)
    #here we could also access the way we removed
    cuted_list.pop(i)
    distance = cuted_list[0]*2 + cuted_list[1]*2 + cuted_list[2]*2 + cuted_list[3]*2
    possible_ways.append(distance)

possible_ways.append(all_ways)

shortest_way = min(possible_ways)

print "Shortes distance is: "+str(shortest_way)
