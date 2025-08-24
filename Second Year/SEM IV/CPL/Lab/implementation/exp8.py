class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def pick_theorem(vertices):
    n = len(vertices)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i].x * vertices[j].y - vertices[j].x * vertices[i].y
    area = abs(area) / 2 + 1  # Adjust for lattice points
    return area

def is_interior(point, vertices):
    # Simple check to avoid boundary points based on unit distance
    for vertex in vertices:
        if abs(point.x - vertex.x) <= 1 and abs(point.y - vertex.y) <= 1:
            return False
    return True

def main():
    # Input the number of vertices
    n = int(input("Enter the number of vertices: "))
    vertices = []

    # Input the coordinates of each vertex
    for i in range(n):
        x, y = map(int, input(f"Enter coordinates for vertex {i+1} (x y): ").split())
        vertices.append(Point(x, y))

    # Calculate the area of the polygon
    polygon_area = pick_theorem(vertices)
    print("Area of the polygon:", polygon_area)

    # Determine potential interior points for planting trees
    interior_points = []
    x_vals = [v.x for v in vertices]
    y_vals = [v.y for v in vertices]
    for x in range(min(x_vals) + 1, max(x_vals)):
        for y in range(min(y_vals) + 1, max(y_vals)):
            point = Point(x, y)
            if is_interior(point, vertices):
                interior_points.append(point)

    # Count the number of interior grid points
    num_trees = len(interior_points)
    print("Number of trees that can be planted:", num_trees)

if __name__ == "__main__":
    main()