import os
import csv
import json 
import pickle

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup, \
QTableWidget, QGridLayout, QTableWidgetItem, QMenuBar, QMenu
from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtGui import QPalette, QColor



from ui_py_files.CreateClimbFormUI import Ui_Form
from widgets.BoardWidget import BoardWidget
from widgets.CreateCimbForm import CreateClimbForm
from widgets.SavedClimbsTable import SavedClimbsTable
from widgets.SaveClimbPopup import SaveClimbPopup
from widgets.MenuBar import MenuBar
from tools.JsonHandler import JsonHanlder as js
from widgets.SignInForm import SignInForm
# from configuration import Configuartion
from DBConfig import UserAccountTable, Climbs, ClimbsHistory
from tools.hold2ledconvert import routeToLeds

from ui_py_files.SaveClimbWindow import Ui_input_climb_data
from tools.sendClimbRequest import sendRouteToServer


class MainWidget(QWidget):
    def __init__(self, ClimbsDb : Climbs, ClimbsHistoryDb = ClimbsHistory, UserAccountDb = UserAccountTable, parent: QWidget = None) -> None:
        super(MainWidget, self).__init__(parent)


        """SAVED CLIMB NOT WORKING ERROR REGARDING WORKING ON A CLOSED DATA BASE 
        ALSO CANNOT GET THE ROUTE TO LOAD AS IT IS COMING AS A LIST WITH A SINGLE ELEMENT
        WHICH IS A TUPLE THAT HOLDS A STRING THAT IS OUR ROUTE
        
        ITS ALSO ALLOWING ME TO ADD CLIMBS WITH THE SAME NAME, BUT JUST ADDS TH ROUTE
        AS A SECOND ROUTE AGAINST THE SAME CLIMB NAME 
        
        ITS SCUFFEEEDDDD"""
        self.route = []
        
        self.main_layout = QGridLayout(self)
        self.setLayout(self.main_layout)

        self.UserAccountsDb = UserAccountDb

        self.ClimbsDb = ClimbsDb
        # self.ClimbsTable.create_table()

        # self.ClimbsHistoryTable = ClimbsHistory()
        # self.ClimbsHistoryTable.create_table()
        self.ClimbsHistoryDb = ClimbsHistoryDb


        self.board_widget = BoardWidget()
        self.board_widget.hold_buttons_group.buttonClicked.connect\
        (self.collect_route)
        
        self.create_climb_btn = QPushButton('Create Climb')
        self.create_climb_btn.clicked.connect(self.handle_create_climb)
        self.save_climb_btn = QPushButton('Save Climb')
        self.save_climb_btn.clicked.connect(self.onSavedClimbClicked)
        self.save_climb_btn.setEnabled(False)

        self.user_button_one = QPushButton('User One')
        self.user_button_one.isCheckable()
        self.user_button_one.clicked.connect(self.handle_sign_in)
        self.user_button_two = QPushButton('User Two')
        self.user_button_two.isCheckable()

        self.user_buttons = QButtonGroup()
        self.user_buttons.addButton(self.user_button_one)
        self.user_buttons.addButton(self.user_button_two)
        self.user_buttons.setExclusive(True)

        self.climb_ticked_button = QPushButton('Ticked')
        self.climb_ticked_button.clicked.connect(self.handle_climb_tick)

        self.saved_climbs = SavedClimbsTable(db= self.ClimbsDb)
        self.saved_climbs.populate_table()
        self.saved_climbs.widget.tableWidget.cellClicked.connect(self.get_route)

        self.menu = MenuBar(self.UserAccountsDb)

        self.sign_in_form = SignInForm(self.UserAccountsDb)
        self.sign_in_form.SendUsername.connect(self.update_user_login)

        self.main_layout.addWidget(self.board_widget, 1,0)
        self.main_layout.addWidget(self.create_climb_btn, 2,0)
        self.main_layout.addWidget(self.save_climb_btn, 2,1)
        self.main_layout.addWidget(self.user_button_one, 3,0) 
        self.main_layout.addWidget(self.user_button_two, 3,1)   
        self.main_layout.addWidget(self.saved_climbs, 1,1)
        self.main_layout.addWidget(self.menu, 0,0)
        self.main_layout.addWidget(self.climb_ticked_button, 4,0)

        self.route = []
        self.activeuser = None
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        self.selected_climb = None

        self.climbsJSON = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'climbs_dict.json')

        
    def handle_create_climb(self):
        self.create_climb_btn.setEnabled(False)
        self.board_widget.enable_buttons()
        self.save_climb_btn.setEnabled(True)
        self.default_board()

    def collect_route(self, button):
        if button.isChecked() == True:
            self.route.append(self.board_widget.hold_buttons_group.id(button))
            # button.setStyleSheet("background-color: rgba(124,252,0,0);")
            conversion =  {
                1:1, 
                2:4,
                11:7,
                10:10,
                13:13,
                12:16,
                24:21,
                27:25,
                25:29,
                37:31,
                26:34,
                36:36,
                38:39,
                52:41,
                39:44,
                40:46,
                51:48,
                53:50,
                50:54,
                54:56,
                48:60,
                49:63,
                41:67,
                42:69,
                43:71,
                44:73,
                33:75,
                34:78,
                29:80,
                21:81,
                20:84,
                56:87,
                19:88,
                15:91,
                14:94,
                22:97
                    }
            led_to_light = []
            for hold in self.route:
                print(hold)
                if hold in conversion.keys():
                    led = conversion[hold]
                    led_to_light.append(led)
            data = {"leds": led_to_light}

            #displays route on the board
            
            sendRouteToServer(data['leds'])
        else:
            self.route.remove(self.board_widget.hold_buttons_group.id(button))
            button.setStyleSheet("background-color: transparent;")
            d = routeToLeds(self.route)
            sendRouteToServer(d['leds'])

    def save_cancelled(self):
        print('creating climb cancelled')
        self.defaultUi()
            
    def defaultUi(self):        
        self.create_climb_btn.setEnabled(True)
        self.save_climb_btn.setEnabled(False)
        self.route.clear()
        self.default_board()
        self.board_widget.disable_buttons()
        self.board_widget.uncheck_buttons()
      
    def get_route(self, row, column):

        self.defaultUi()

        climb_name = \
        self.saved_climbs.widget.tableWidget.item(row, column).text()
        
        #dont handle sql query in the main widget like this - needs moving and abstracting
        self.ClimbsHistoryDb.cursor.execute("SELECT route from climbs WHERE climb_name = ?", (climb_name,))
        data = self.ClimbsHistoryDb.cursor.fetchall()
        tuple = data[0]
        d = tuple[0]
        # route = [char for char in d]
        route = pickle.loads(d)

        # print(data )
        # for char in route:
        #     print(type(char))
        

        self.display_route(route)
    

        
    #should be in board widget
    def display_route(self, route):
        #displays route in ui
        for button in route:
            button_to_display = self.board_widget.hold_buttons_group.button(button)
            button_to_display.setStyleSheet("background-color: green;")
        #relates hold number to the led number in the led string
        conversion =  {
                        1:1, 
                        2:4,
                        11:7,
                        10:10,
                        13:13,
                        12:16,
                        24:21,
                        27:25,
                        25:29,
                        37:31,
                        26:34,
                        36:36,
                        38:39,
                        52:41,
                        39:44,
                        40:46,
                        51:48,
                        53:50,
                        50:54,
                        54:56,
                        48:60,
                        49:63,
                        41:67,
                        42:69,
                        43:71,
                        44:73,
                        33:75,
                        34:78,
                        29:80,
                        21:81,
                        20:84,
                        56:87,
                        19:88,
                        15:91,
                        14:94,
                        22:97
                    }
        led_to_light = []
        for hold in route:
            print(hold)
            if hold in conversion.keys():
                led = conversion[hold]
                led_to_light.append(led)
        data = {"leds": led_to_light}

        #displays route on the board
        print(data['leds'])
        sendRouteToServer(data['leds'])

        

    #should be in board widger            
    def default_board(self):
        for button in self.board_widget.hold_buttons_group.buttons():
            button.setStyleSheet("background-color: transparent;")
                    
    def climb_saved(self):
        print('climb saved')
        self.saved_climbs.populate_table()


    def onSavedClimbClicked(self):
        save_climb_form = SaveClimbPopup(route= self.route, db= self.ClimbsDb)
        save_climb_form.exec() 

        save_climb_form.SaveCancelled.connect(self.save_cancelled())
        save_climb_form.ClimbSaved.connect(self.climb_saved())

    def update_user_login(self, username):
        self.activeuser = username
        self.user_button_one.setText(username)

    def handle_sign_in(self):
        self.sign_in_form.exec()
        return

    def handle_climb_tick(self):
        #allows guests to log ticks 
        saved_climbs_data = json.openJson(self.climbsJSON)
        saved_climbs_data[self.selected_climb]['ticks'] = (saved_climbs_data[self.selected_climb]['ticks']) + 1
        json.writeJson(saved_climbs_data, self.climbsJSON)

        if self.user_button_one.text() != 'User One':
            print('adding climb')
            self.database.add_tick(self.selected_climb)
            print(self.selected_climb)
        else:
            pass
