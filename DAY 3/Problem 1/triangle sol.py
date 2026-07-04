def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def area_of_triangle(a, b, c):
    # Using Heron's formula
    side_a = distance(a, b)
    side_b = distance(b, c)
    side_c = distance(c, a)
    s = (side_a + side_b + side_c) / 2
    return math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))

def is_point_inside_triangle(p, a, b, c):
    # Using barycentric coordinates to check if point is inside the triangle
    def sign(p, a, b):
        return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])

    b1 = sign(p, a, b)
    b2 = sign(p, b, c)
    b3 = sign(p, c, a)

    if (b1 > 0 and b2 > 0 and b3 > 0) or (b1 < 0 and b2 < 0 and b3 < 0):
        return True
    else:
        return False

# Get input from user
a = tuple(map(float, input("Enter coordinates of A (x1, y1): ").split()))
b = tuple(map(float, input("Enter coordinates of B (x2, y2): ").split()))
c = tuple(map(float, input("Enter coordinates of C (x3, y3): ").split()))
p = tuple(map(float, input("Enter coordinates of the point (x, y): ").split()))

# Calculate lengths of sides
side_ab = distance(a, b)
side_bc = distance(b, c)
side_ca = distance(c, a)

# Calculate area of triangle
area = area_of_triangle(a, b, c)

# Check if point is inside the triangle
inside = is_point_inside_triangle(p, a, b)

# Output results
print(f"Length of AB: {side_ab}")
print(f"Length of BC: {side_bc}")
print(f"Length of CA: {side_ca}")
print(f"Area of triangle ABC: {area}")
print(f"Is the point ({p[0]}, {p[1]}) inside the triangle? {inside}")