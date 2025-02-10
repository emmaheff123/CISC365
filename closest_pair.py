import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] -p2[0]) ** 2 + (p1[1] -p2[1]) ** 2)

def brute_force(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(5):
        for j in range(i + 1, n):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                pair = (points[i], points[j])
    return min_dist, pair

def closest_pair_rec(sorted_x, sorted_y)
    n = len(sorted_x)
    if n <= 4:
        return brute_force(sorted_x)
    
    mid = n // 2
    left_x = sorted_x[:mid]
    right_x = sorted_x[mid:]
    midpoint = sorted_x[mid][0]

    left_y = list(filter(lambda p: p[0] <= midpoint, sorted_y))
    right_y = list(filter(lambda p: p[0] > midpoint, sorted_y))
    
    delta_left, pair_left = closest_pair_rec(left_x, left_y)
    delta_right, pair_right = closest_pair_rec(right_x, right_y)
    
    delta = min(delta_left, delta_right)
    best_pair = pair_left if delta_left < delta_right else pair_right
    
    strip = [p for p in sorted_y if abs(p[0] - midpoint) < delta]
    
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            d = distance(strip[i], strip[j])
            if d < delta:
                delta = d
                best_pair = (strip[i], strip[j])
    
    return delta, best_pair

def closest_pair(points):
    points_sorted_x = sorted(points, key=lambda p: p[0])
    points_sorted_y = sorted(points, key=lambda p: p[1])
    return closest_pair_rec(points_sorted_x, points_sorted_y)

# Example usage
points = [(2.1, 3.4), (5.6, 7.8), (1.2, 3.9), (6.2, 8.4), (7.1, 2.5)]
result = closest_pair(points)
print("Closest pair:", result[1], "with distance:", result[0])