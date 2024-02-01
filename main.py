import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

def BowyerWatson(pointList):
    # Initialize triangulation with a large super-triangle
    superTriangle = Triangle(Point(-1e4, -1e4), Point(1e4, -1e4), Point(0, 1e4))
    triangulation = [superTriangle]

    for point in pointList:
        badTriangles = []
        for triangle in triangulation:
            if isPointInCircumcircle(point, triangle):
                badTriangles.append(triangle)

        polygon = []
        for triangle in badTriangles:
            for edge in edges(triangle):
                if isEdgeShared(edge, badTriangles):
                    polygon.append(edge)

        triangulation = [t for t in triangulation if t not in badTriangles]

        for edge in polygon:
            triangulation.append(Triangle(edge[0], edge[1], point))

    # Remove triangles that contain vertices of the super-triangle
    triangulation = [t for t in triangulation if not containsSuperTriangleVertex(t, superTriangle)]

    return triangulation

def isPointInCircumcircle(p, triangle):
    ax, ay = triangle.p1.x - p.x, triangle.p1.y - p.y
    bx, by = triangle.p2.x - p.x, triangle.p2.y - p.y
    cx, cy = triangle.p3.x - p.x, triangle.p3.y - p.y

    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))

    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d

    return ux * ux + uy * uy > ax * ax + ay * ay

def edges(triangle):
    # Return the edges of a triangle
    return [(triangle.p1, triangle.p2), (triangle.p2, triangle.p3), (triangle.p3, triangle.p1)]

def isEdgeShared(edge, triangles):
    count = sum(edge in edges(triangle) for triangle in triangles)
    return count > 1

def containsSuperTriangleVertex(triangle, superTriangle):
    return triangle.p1 in [superTriangle.p1, superTriangle.p2, superTriangle.p3] or \
           triangle.p2 in [superTriangle.p1, superTriangle.p2, superTriangle.p3] or \
           triangle.p3 in [superTriangle.p1, superTriangle.p2, superTriangle.p3]


# Create a list of points
pointList = [Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]

# Call the BowyerWatson function
result = BowyerWatson(pointList)

# Print the result
for triangle in result:
    print(f"Triangle: ({triangle.p1.x}, {triangle.p1.y}), ({triangle.p2.x}, {triangle.p2.y}), ({triangle.p3.x}, {triangle.p3.y})")