import pygame
import pygame.gfxdraw
import math
import random

pygame.init()
def circumcenter(a, b, c):
    ad = a[0] * a[0] + a[1] * a[1]
    bd = b[0] * b[0] + b[1] * b[1]
    cd = c[0] * c[0] + c[1] * c[1]
    D = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
    return pygame.Vector2((1 / D * (ad * (b[1] - c[1]) + bd * (c[1] - a[1]) + cd * (a[1] - b[1])),
                           1 / D * (ad * (c[0] - b[0]) + bd * (a[0] - c[0]) + cd * (b[0] - a[0]))))

def LineIsEqual(line1,line2):
    if (line1[0] == line2[0] and line1[1] == line2[1]) or (line1[0] == line2[1] and line1[1] == line2[0]):
        return True
    return False

def distance(point1,point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)


def super_triangle(vertices):
    minx = miny = float('inf')
    maxx = maxy = float('-inf')
    for vertex in vertices:
        minx = min(minx, vertex.x)
        miny = min(miny, vertex.y)
        maxx = max(maxx, vertex.x)
        maxy = max(maxy, vertex.y)

    dx = (maxx - minx) * 10
    dy = (maxy - miny) * 10

    v0 = pygame.Vector2(minx - dx, miny - dy * 3)
    v1 = pygame.Vector2(minx - dx, maxy + dy)
    v2 = pygame.Vector2(maxx + dx * 3, maxy + dy)

    return Triangle(v0, v1, v2)
class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.edges = [[self.a,self.b],
                      [self.b,self.c],
                      [self.c,self.a]]
        self.circumcenter = circumcenter(a,b,c)
    def IsPointInCircumcircle(self,point):
        if (self.a.distance_to(self.circumcenter) > point.distance_to(self.circumcenter)
            or self.b.distance_to(self.circumcenter) > point.distance_to(self.circumcenter)
            or self.c.distance_to(self.circumcenter) > point.distance_to(self.circumcenter)):
            return True
        return False
    def HasVertex(self,point):
        if (self.a == point) or (self.b == point) or (self.c == point):
            return True
        return False
    def Show(self,screen,colour):
        for edge in self.edges:
            pygame.draw.aaline(screen,colour,edge[0],edge[1])


def DelaunayTriangulation(points):
    triangulation = []
    superTriangle = super_triangle(points)
    triangulation.append(superTriangle)

    for point in points:

        badTriangles = []
        for triangle in triangulation:
            if triangle.IsPointInCircumcircle(point):
                badTriangles.append(triangle)

        polygon = []
        for triangle in badTriangles:
            for triangleEdge in triangle.edges:
                isShared = False
                for other in badTriangles:
                    if triangle == other:
                        continue
                    for otherEdge in other.edges:
                        if LineIsEqual(triangleEdge,otherEdge):
                            isShared = True
                if isShared == False:
                    polygon.append(triangleEdge)

        for badTriangle in badTriangles:
            triangulation.remove(badTriangle)

        for edge in polygon:
            newTriangle = Triangle(edge[0],edge[1],point)
            triangulation.append(newTriangle)
    to_be_removed = []
    for triangle in triangulation:
        if triangle.HasVertex(superTriangle.a) and triangle in triangulation:
            to_be_removed.append(triangle)
        if triangle.HasVertex(superTriangle.b) and triangle in triangulation:
            to_be_removed.append(triangle)
        if triangle.HasVertex(superTriangle.c) and triangle in triangulation:
            to_be_removed.append(triangle)
    triangulation = [triangle for triangle in triangulation if triangle not in to_be_removed]

    return triangulation

def randomPoints(amount,width,height):
    points = []
    for i in range(amount):
        x = random.randint(1,width)
        y = random.randint(1,height)
        points.append(pygame.Vector2(x,y))
    return points
def get_sample_points():
    points = [
        pygame.Vector2(1.978029803416428978e-01, 9.113971402877307781e-02),
        pygame.Vector2(6.508961860968820456e-01, 1.730161641721069676e-01),
        pygame.Vector2(2.251677455532904437e-01 ,2.762800497063325755e-01),
        pygame.Vector2(2.223850717341324668e-02, 2.503835940444159025e-01),
        pygame.Vector2(4.680392943712008424e-02 ,7.483645576596771321e-01),
        pygame.Vector2(6.152856071753494138e-01, 9.491795580891586592e-01),
        pygame.Vector2(5.691689268663715495e-01, 5.957249433084483847e-01),
        pygame.Vector2(8.886475765102330726e-01, 5.422157381700745127e-01),
        pygame.Vector2(1.251978052319724366e-01, 5.191094326799222669e-01),
        pygame.Vector2(1.555081454372811978e-01, 4.941367022891524075e-01),
        pygame.Vector2(7.173435529989276027e-01, 7.666772186856247728e-01),
        pygame.Vector2(8.417660037734938649e-01, 8.023307403258042036e-01),
        pygame.Vector2(1.835236409165003080e-01, 1.985757350392464149e-01),
        pygame.Vector2(1.004434831816419793e-01, 1.431688606540125752e-01),
        pygame.Vector2(5.630905339550972277e-01, 1.407112517896764725e-01),
        pygame.Vector2(7.484628027139150763e-02, 1.104403852394537644e-01),
        pygame.Vector2(5.032605814632451491e-01, 3.659693219013806509e-01),
        pygame.Vector2(9.650485087215605606e-01, 5.193223865298413067e-02),
        pygame.Vector2(7.146024948936324783e-02, 5.639852833522054354e-01),
        pygame.Vector2(8.256091876857983847e-01, 6.545393590609183132e-02),
        pygame.Vector2(2.506930794706603294e-01, 4.532668368817679427e-01),
        pygame.Vector2(8.367946400968482301e-01, 2.832617295399242341e-02),
        pygame.Vector2(2.589375303668870476e-01, 6.792743981154487631e-01),
        pygame.Vector2(6.794439894416055559e-01, 3.278726992119568306e-01),
        pygame.Vector2(7.517817639498910465e-01, 4.974661473994379524e-01),
        pygame.Vector2(2.214499758142397523e-01, 3.096996086381774704e-01),
        pygame.Vector2(2.888726651949391488e-03, 9.471633731378522603e-01),
        pygame.Vector2(2.170498358338623923e-01, 5.207475106676567878e-01),
        pygame.Vector2(4.331623402878923557e-01, 3.561433386242225385e-01),
        pygame.Vector2(1.738322291021661137e-01, 3.441024067743247983e-02),
        pygame.Vector2(5.170942651935439560e-02, 5.479367015346068293e-01),
        pygame.Vector2(9.839298165786504180e-01, 9.871862536732842752e-01),
        pygame.Vector2(7.079555251206122168e-01, 4.828530260645713668e-02),
        pygame.Vector2(2.798155546831389007e-01, 5.233592529555652906e-02),
        pygame.Vector2(9.197994266352867987e-01, 6.541379369320531323e-01),
        pygame.Vector2(3.567470908793418660e-01, 5.093190537998146805e-01),
        pygame.Vector2(8.543482126386714448e-01, 2.352137424530930110e-01),
        pygame.Vector2(8.538334110552572298e-01, 7.817861691981772276e-01),
        pygame.Vector2(4.299588308502031442e-01, 3.281159387010627038e-01),
        pygame.Vector2(3.370175237538394208e-01, 6.333271317862571026e-01),
        pygame.Vector2(9.890180976227732623e-01, 3.301627232104259457e-01),
        pygame.Vector2(6.429884015200069136e-01, 6.093843414817965431e-01),
        pygame.Vector2(5.806555895918886767e-01, 4.333349911566914958e-01),
        pygame.Vector2(8.516500363069039459e-01, 4.577204209879628394e-01),
        pygame.Vector2(7.013897158386264152e-01, 4.161864356429584300e-01),
        pygame.Vector2(2.218446600740693331e-01, 5.385261752855001749e-01),
        pygame.Vector2(8.379125291710964873e-02, 5.412591715413912485e-01),
        pygame.Vector2(1.938367346395429847e-01, 4.750496011835669830e-01)
    ]
    return [pygame.Vector2(point.x * 500, point.y * 500) for point in points]
# user interface
background_color = 18,55,42
line_color =  251,250,218
width = 1000
height = 800
amount = 50
screen = pygame.display.set_mode((width,height))
# points = randomPoints(amount,width,height)
points = get_sample_points()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)

    delaunay = DelaunayTriangulation(points)

    for triangle in delaunay:
        triangle.Show(screen,line_color)
    pygame.display.update()
pygame.quit()


