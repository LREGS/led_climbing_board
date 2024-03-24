# from nicegui import events, ui


# #tl, tr, bl, br coords of a square

# def checkInSquare(square, coords):
#     point = coords
#     tl = square[0]
#     tr = square[1]
#     bl = square[2]
#     br = square[3]
#     minX = bl[0]
#     maxX = tr[0]
#     minY = tl[1]
#     maxY = br[1]
#     x = coords[0]
#     y = coords[1]

#     if (x >= minX and x <= maxX) and (y >= minY and y <= maxY):
#         return True 

#     # if point[0] >= tl[0] & bl[0] & point[0] <= tr[0] & br[0]:
#     #     if point[1] >= bl[1] & br[1] & point[1] <= tl[1] & tr[1]:
#     #         return True





# def mouse_handler(e: events.MouseEventArguments):
#     square = [[336, 189],[535, 195],[336, 290],[547, 291]]
#     # color = 'SkyBlue' if e.type == 'mousedown' else 'SteelBlue'
#     # ii.content += f'<circle cx="{e.image_x}" cy="{e.image_y}" r="15" fill="none" stroke="{color}" stroke-width="4" />'
#     coords = [e.image_x, e.image_y]

#     if checkInSquare(square, coords):
#         ui.notify(f'square clicked')
#     else:
#         ui.notify(f'keep trying to find the square {coords}')

# src = 'https://picsum.photos/id/565/640/360'
# ii = ui.interactive_image(src, on_mouse=mouse_handler, events=['mousedown', 'mouseup'], cross=True)

# ui.run()
import random
from shapely.geometry import Point, Polygon
from nicegui import events, ui


class polygon():
    def __init__(self):
        self.coords = []
    def addCoordToPolygon(self, coords: list):
        self.coords.append(coords)


def generate_random_polygon():
    hold = [[660,1305],[811,1311], [811,1346], [660,1344]]# , 
    # num_vertices = random.randint(3, 6)  # You can adjust the number of vertices as needed
    # polygon_coords = [[random.randint(100, 500), random.randint(100, 300)] for _ in range(num_vertices)]
    return hold

def input_polygon()-> list:
    polygon = []

    return polygon 

def check_in_polygon(polygon_coords, point_coords):
    polygon = Polygon(polygon_coords)
    point = Point(point_coords[0], point_coords[1])
    return polygon.contains(point)

def mouse_handler(e: events.MouseEventArguments):
    poly = polygon()
    global random_polygon_coords

    coords = [e.image_x, e.image_y]

    if check_in_polygon(random_polygon_coords, coords):
        ui.notify('Hold Clicked')
        random_polygon_coords = generate_random_polygon()
        draw_polygon(random_polygon_coords)
    else:
        ui.notify(f'No hold')

def draw_polygon(polygon_coords):
    ii.content = f'<polygon points="{",".join(map(lambda p: str(p[0])+","+str(p[1]), polygon_coords))}" fill="none" stroke="red" stroke-width="2" />'

random_polygon_coords = generate_random_polygon()

src = '/home/william/personal/board.jpg'
ii = ui.interactive_image(src, on_mouse=mouse_handler, events=['mousedown', 'mouseup'], cross=True)

# Draw the initial random polygon
draw_polygon([[660,1305],[811,1311], [811,1346], [660,1344]])

ui.run()
