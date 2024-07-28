import math

def euclideanDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

points = [(12, 5), (22, 35), (6, 9), (15, 22)]

distances = []

for i in range(len(points)):
    for j in range(i + 1 , len(points)):
        distance = euclideanDistance(points[i] , points[j])
        distances.append(distance)

min_distance = min(distances)

print(distances)
print(min_distance)
