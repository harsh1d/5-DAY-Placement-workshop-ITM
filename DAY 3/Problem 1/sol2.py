import math
def distance(p1, p2, count=1):
    if count == 1:
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    else:
        return distance(p1, p2, count-1)
def area_of_triangle(a, b, c):
    side_ab = distance(a, b)
    side_bc = distance(b, c)
    side_ca = distance(c, a)
    s = (side_ab + side_bc + side_ca) / 2
    return math.sqrt(s * (s - side_ab) * (s - side_bc) * (s - side_ca))
def is_point_inside_triangle(p, a, b, c):
    total_area = area_of_triangle(a, b, c)
    area1 = area_of_triangle(p, b, c)
    area2 = area_of_triangle(a, p, c)
    area3 = area_of_triangle(a, b, p)
    return math.isclose(total_area, area1 + area2 + area3, rel_tol=1e-9)
a = tuple(map(float, input("Enter coordinates of A (x1 y1): ").split()))
b = tuple(map(float, input("Enter coordinates of B (x2 y2): ").split()))
c = tuple(map(float, input("Enter coordinates of C (x3 y3): ").split()))
p = tuple(map(float, input("Enter coordinates of point P (x y): ").split()))
side_ab = distance(a, b)
side_bc = distance(b, c)
side_ca = distance(c, a)
area = area_of_triangle(a, b, c)
inside = is_point_inside_triangle(p, a, b, c)
print(f"Length of AB: {side_ab:.2f}")
print(f"Length of BC: {side_bc:.2f}")
print(f"Length of CA: {side_ca:.2f}")
print(f"Area of triangle ABC: {area:.2f}")
print(f"Is point {p} inside triangle? {inside}")
