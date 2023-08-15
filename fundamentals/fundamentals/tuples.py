#Built-in Tuple Functions
'''
max(sequence) returns the largest value in the sequence
sum(sequence) return the sum of all values in sequence
enumerate(sequence) used in a for-loop context to return two-item-tuple for each item in the sequence indicating the index followed by the value at that index.
map(function, sequence) applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence) returns the lowest value in a sequence.
sorted(sequence) returns a sorted sequence
'''
import math

def get_circle_area(r):
    # Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)

radius = float(input("Enter the radius of the circle: "))

circle_data = get_circle_area(radius)

print("Circumference:", circle_data[0])
print("Area:", circle_data[1])