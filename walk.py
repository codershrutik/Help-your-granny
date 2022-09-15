from math import sqrt,floor

def tour(friends,friends_towns,homw_to_town_distance):
    distance = 0
    n = [homw_to_town_distance[t[1]] for f in friends for t in friends_towns if f == t[0]]
    index = 0
    for i in n:
        if index < len(n) - 1:
            distance += sqrt(round(abs(pow(i,2) - pow(n[index+1],2))))
            index += 1
    return floor(distance + n[0] + n[-1])

friends1 = ["A1", "A2", "A3", "A4", "A5"]
fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
print(tour(friends1, fTowns1, distTable1), 889)
