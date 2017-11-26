from numpy import argmax
triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

triangle = triangle.split("\n")

triangle = [[int(i) for i in row.split(" ")] for row in triangle]


cursor = -1
largest = -1

# Finds the maximum sum of the bottom two rows
# first block checks the edges
cursor = argmax([triangle[-1][0] + triangle[-2][0], triangle[-1][-1] + triangle[-2][-1]])
cursor *= len(triangle[level])
largest = triangle[-1][cursor]

# second block checks the middle
for i in range(1, len(triangle[-1]) - 2):
    for direction in range(-1, 1):
        if triangle[-1][i] + triangle[-2][i + direction] > largest:
            largest = triangle[-1][i] + triangle[-2][i + direction]
            cursor = i + direction

# Now that the max for the bottom two rows is established, we work out way up the triangle
for level in xrange(len(triangle) - 3, -1, -1):
    if cursor == 0:·
        total += triangle[level][0]
    elif cursor == len(triangle[level]):
        total += triangle[level][-1]
        cursor = len(triangle[level]) -1
    else:
        direction = argmax([triangle[level][cursor - 1], triangle[level][cursor]])
        total += triangle[level][cursor + direction - 1]
        cursor += (direction - 1)
    triangle[level][cursor] = str(triangle[level][cursor])
    print triangle[level]

total
