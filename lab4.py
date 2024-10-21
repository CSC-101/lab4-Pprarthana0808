import data
import math

# Write your functions for each part in the space below.

# Part 1
def first_element(nested_list: list[list[int]]) -> list[int]:
    non_empty_lists = [lst for lst in nested_list if lst]
    first_elements = [lst[0] for lst in non_empty_lists]
    return first_elements

# Part 2
def x_coordinates(points: list[data.Point]) -> list[float]:
    return [point.x for point in points]
# Part 3
def are_in_positive_quadrant(points: list[data.Point]) -> list[data.Point]:
    return [point for point in points if point.x >0 and point.y>0]

# Part 4
def distance(p1: data.Point, p2: data.Point) -> float:
    return math.sqrt((p2.x - p1.x) **2 + (p2.y - p1.y)**2)
# Part 5
def manhattan_distance(p1: data.Point, p2: data.Point) -> float:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

# Part 6
def distance_all(points: list[data.Point]) -> list[float]:
    origin = data.Point(0,0)
    return [distance(origin, point) for point in points]


