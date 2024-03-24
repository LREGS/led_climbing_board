from nicegui import events, ui
from shapely.geometry import Point, Polygon
from dataclasses import dataclass

@dataclass
class Climb:
    name: str
    grade: int
    route: list

climb_ready = False
class iBoardImage():
    def __init__(self):
        self.boardImage = "/home/william/personal/board.jpg"
        self.holdsList = [[(660,1305),(811,1311), (811,1346), (660,1344)], [(100, 200), (200, 100), (300, 100), (100,300)]]
        self.sortedHolds = self.sortHolds()
        self.iBoard = self.iBoard()
        self.climbReady = False
        self.recordReady = False
        self.climb = Climb(
                    name="",
                    grade=0,
                    route=[]
                )   

    def iBoard(self):
        iImage = ui.interactive_image(self.boardImage, on_mouse=self.mouseHandler)
        iImage.on_mouse = self.newMouse
        self.drawHolds(self.holdsList, iImage)
        return iImage
    
    def newMouse(self, e: events.MouseEventArguments):
        print("hi")
        ui.notify(f'New mouse handler: {e.type} at ({e.image_x:.1f}, {e.image_y:.1f})')


    def drawHolds(self, holdsList,  iImage):

        polygons_svg = ""
        for hold in holdsList:
            points = ",".join([f"{p[0]},{p[1]}" for p in hold])
            polygons_svg += f'<polygon points="{points}" fill="none" stroke="red" stroke-width="2" />'

        iImage.content = polygons_svg
 
    
    def mouseHandler(self, e: events.MouseEventArguments):
        coords = [e.image_x, e.image_y]
        if self.recordReady:
             
            clicked, hold = self.check_hold_clicked(coords)
            if clicked == True:
                self.climb.route.append(hold)
                print(self.climb.route)
            




    def check_hold_clicked(self, coords):
        """When the list grows we want to sort the holdsList list by the first x value 
        using in built sorted function then use a search alg to check the hold quicker"""
        for hold in self.holdsList:
            polygon = Polygon(hold)
            point = Point(coords[0], coords[1])
            if polygon.contains(point):
                return True, polygon
        return False, None
        
    def sortHolds(self):
        return
    
    def prepareRecordClimb(self):

        # self.iBoard = ui.interactive_image(self.boardImage, on_mouse=self.recordClimb(climb), events=['mouseup'])

        self.drawHolds(self.holdsList, self.iBoard)
    
    def recordClimb(self, climb):
        ui.notify(f'climb {climb.name} Clicked')

    def toggleSaveReady(self, bool):
        if bool != True or False:
            exit
        if bool == True:
            self.climbReady = bool 
            self.recordReady = False

    def toggleRecordReady(self, inp):
        if inp != True or False:
            exit
        if inp == True:
            self.recordReady = inp 
            self.climbReady = False
    
    def startRecordingClimb(self):
        #so dumb in python cause I can just use self and access the variables from within the class cant i
        self.drawHolds(self.holdsList, self.boardImage)
        self.toggleRecordReady(True)
        
    def saveClimb(self):
        #wants to actually be implemented using async
        self.recordReady = False
        print(self.climb)





def content():

    board = iBoardImage()
    climbs = []
    createButton = ui.button('Create Climb', on_click=lambda: board.toggleRecordReady(True))
    ui.button('save climb', on_click= board.saveClimb)
    climbs.append(board.climb)
    print(climbs)

    # src = '/home/william/personal/board.jpg'
    
    # iImage = ui.interactive_image(src, on_mouse=mouse_handler, events=['mousedown', 'mouseup'], cross=True)
    # holdsList = [(660,1305),(811,1311), (811,1346), (660,1344)]

    # drawHolds(holdsList, iImage)

def changeReadyState(state):
    climb_ready == state
    

def drawHolds(holdsList, image):
    newIm = image.content = f'<polygon points="{",".join(map(lambda p: str(p[0])+","+str(p[1]), holdsList))}" fill="none" stroke="red" stroke-width="2" />'
    return newIm



def mouse_handler(e: events.MouseEventArguments):
    holdsList = [[(660,1305),(811,1311), (811,1346), (660,1344)]]

    ui.notify(f'{e.type} at ({e.image_x:.1f}, {e.image_y:.1f})')

ui.run()