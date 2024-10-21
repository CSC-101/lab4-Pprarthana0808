import data
import lab4
import unittest
import math
from lab4 import x_coordinates, are_in_positive_quadrant, manhattan_distance, distance


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input1 = [[1,2], [3,4]]
        result = lab4.first_element(input1)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        input = [[1,3], [4,5]]
        result = lab4.first_element(input)
        expected = [1, 4]
        self.assertEqual(expected, result)
    def test_first_element_3(self):
        input = [[10,9], [100,6]]
        result = lab4.first_element(input)
        expected = [10, 100]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates_1(self):
        input = [data.Point(1, 2), data.Point(3, 4)]
        result = x_coordinates(input)
        expected = [1,3]
        self.assertEqual(expected, result)
    def test_x_coordinates_2(self):
        input = [data.Point(-1, -2), data.Point(0, 0), data.Point(5,7)]
        result = x_coordinates(input)
        expected = [-1, 0, 5]
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        points = [data.Point(1,1), data.Point(-1, 2), data.Point(3, 4)]
        result = are_in_positive_quadrant(points)
        expected = [data.Point(1,1), data.Point(3,4)]
        self.assertEqual(result, expected)

    def test_are_in_positive_quadrant_2(self):
        points = [data.Point(0,0), data.Point(-1, -1), data.Point(5, 5)]
        result = are_in_positive_quadrant(points)
        expected = [data.Point(5,5)]
        self.assertEqual(result, expected)

    # Part 4
    def test_distance_1(self):
        result = distance(data.Point(0,0), data.Point(3,4))
        expected = 5.0
        self.assertEqual(expected, result)
    def test_distance_2(self):
        result = distance(data.Point(1,1), data.Point(4,5))
        expected = 5.0
        self.assertEqual(expected, result)

    # Part 5
    def test_manhattan_distance_1(self):
        result = manhattan_distance(data.Point(0,0), data.Point(3,4))
        expected = 7.0
        self.assertEqual(expected, result)
    def test_manhattan_distance_2(self):
        result = manhattan_distance(data.Point(1,1), data.Point(4,5))
        expected = 7.0
        self.assertEqual(expected, result)
    # Part 6
    def test_distance_all_1(self):
        input = [data.Point(3,4), data.Point(6,8)]
        result = lab4.distance_all(input)
        expected = [5.0, 10.0]
        self.assertEqual(expected, result)

    def test_distance_all_2(self):
        input = [data.Point(30,40), data.Point(10,24)]
        result = lab4.distance_all(input)
        expected = [50.0, 26.0]
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
