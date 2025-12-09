import matplotlib.path

with open("2025/files/day9input.txt") as file:
    fileLines = file.readlines()

coords = [tuple([int(num) for num in line.strip().split(",")]) for line in fileLines]
greenCoords = []
for i in range(len(coords)):
    coord1 = coords[i]
    if i == len(coords) - 1: coord2 = coords[0]
    else: coord2 = coords[i+1]

    for j in range(1, abs(coord1[0] - coord2[0])):
        greenCoord = (min(coord1[0], coord2[0]) + j, coord1[1]) 
        greenCoords.append(greenCoord)
    
    for j in range(1, abs(coord1[1] - coord2[1])):
        greenCoord = (coord1[0], min(coord1[1], coord2[1]) + j) 
        greenCoords.append(greenCoord)

coords.append(coords[0])
# I don't think using matplotlib to check whether a coordinate is inside the polygon is cheating... what the hell kinda algorithm are they using, anyway?!
polygon = matplotlib.path.Path(coords)

outerCoords = []
for i in range(len(coords)):
    coord = coords[i]
    print("CALCULATING OUTER POLYGON CORNERS: ", i + 1, "/", len(coords))
    coordx = coord[0]
    coordy = coord[1]
    
    if (coordx + 1, coordy) in greenCoords and (coordx, coordy + 1) in greenCoords: 
        if polygon.contains_point((coordx + 1, coordy + 1)): outerCoords.append((coordx - 1, coordy - 1))
        else: outerCoords.append((coordx + 1, coordy + 1))

    elif (coordx - 1, coordy) in greenCoords and (coordx, coordy + 1) in greenCoords: 
        if polygon.contains_point((coordx + 1, coordy - 1)): outerCoords.append((coordx - 1, coordy + 1))
        else: outerCoords.append((coordx + 1, coordy - 1))     
        
    elif (coordx - 1, coordy) in greenCoords and (coordx, coordy - 1) in greenCoords: 
        if polygon.contains_point((coordx - 1, coordy - 1)): outerCoords.append((coordx + 1, coordy + 1))
        else: outerCoords.append((coordx - 1, coordy - 1))  
        
    elif (coordx + 1, coordy) in greenCoords and (coordx, coordy - 1) in greenCoords:
        if polygon.contains_point((coordx - 1, coordy + 1)): outerCoords.append((coordx + 1, coordy - 1))
        else: outerCoords.append((coordx - 1, coordy + 1))

lineSegments = []
for i in range(len(outerCoords) - 1):
    lineSegments.append([outerCoords[i], outerCoords[i+1]])

areas = {}
for i in range(len(coords)):
    for j in range(len(coords)):
        if i == j or (i, j) in areas.keys() or (j, i) in areas.keys(): continue
        area = (abs(coords[i][0] - coords[j][0]) + 1) * (abs(coords[i][1] - coords[j][1]) + 1)
        areas[(i, j)] = area

areas = sorted(areas.items(), key=lambda item: item[1], reverse = True)

def getCorners(coords, area):
    baseCorner1 = coords[area[0][0]]
    baseCorner2 = coords[area[0][1]]

    corner1 = (min(baseCorner1[0], baseCorner2[0]), min(baseCorner1[1], baseCorner2[1]))
    corner2 = (min(baseCorner1[0], baseCorner2[0]), max(baseCorner1[1], baseCorner2[1]))
    corner3 = (max(baseCorner1[0], baseCorner2[0]), min(baseCorner1[1], baseCorner2[1]))
    corner4 = (max(baseCorner1[0], baseCorner2[0]), max(baseCorner1[1], baseCorner2[1]))
    
    return [corner1, corner2, corner3, corner4]

def isAreaValid(coords, area):
    corners = getCorners(coords, area)

    for corner1 in corners:
        for corner2 in corners:
            if corner1 == corner2: continue
            lineSegment = [corner1, corner2]

            for seg in lineSegments:
                if doIntersect([seg, lineSegment]): return False
    
    return True

# Below algorithm for intersecting line segments kindly taken from https://www.geeksforgeeks.org/dsa/check-if-two-given-line-segments-intersect/

# function to check if point q lies on line segment 'pr'
def onSegment(p, q, r):
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

# function to find orientation of ordered triplet (p, q, r)
# 0 --> p, q and r are collinear
# 1 --> Clockwise
# 2 --> Counterclockwise
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    # collinear
    if val == 0:
        return 0

    # clock or counterclock wise
    # 1 for clockwise, 2 for counterclockwise
    return 1 if val > 0 else 2


# function to check if two line segments intersect
def doIntersect(points):
    # find the four orientations needed
    # for general and special cases
    o1 = orientation(points[0][0], points[0][1], points[1][0])
    o2 = orientation(points[0][0], points[0][1], points[1][1])
    o3 = orientation(points[1][0], points[1][1], points[0][0])
    o4 = orientation(points[1][0], points[1][1], points[0][1])

    # general case
    if o1 != o2 and o3 != o4:
        return True

    # special cases
    # p1, q1 and p2 are collinear and p2 lies on segment p1q1
    if o1 == 0 and onSegment(points[0][0], points[1][0], points[0][1]):
        return True

    # p1, q1 and q2 are collinear and q2 lies on segment p1q1
    if o2 == 0 and onSegment(points[0][0], points[1][1], points[0][1]):
        return True

    # p2, q2 and p1 are collinear and p1 lies on segment p2q2
    if o3 == 0 and onSegment(points[1][0], points[0][0], points[1][1]):
        return True

    # p2, q2 and q1 are collinear and q1 lies on segment p2q2 
    if o4 == 0 and onSegment(points[1][0], points[0][1], points[1][1]):
        return True

    return False

for i in range(len(areas)):
    area = areas[i]
    print("LOOKING FOR A VALID AREA:", i + 1, "/", len(areas))
    if isAreaValid(coords, area): 
        print("VALID AREA FOUND:", area[1])
        break