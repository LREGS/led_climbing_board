import os
import csv
import json 

from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtWidgets import QSizePolicy, QApplication, QMainWindow, \
QLabel,QPushButton, QToolButton, QVBoxLayout, QWidget, QDialog, QButtonGroup, \
QTableWidget, QGridLayout, QTableWidgetItem, QMenuBar, QMenu
from PySide6.QtCore import QObject, Signal, QTimer
from PySide6.QtGui import QPalette, QColor



from ui_py_files.create_climb_formUI import Ui_Form
from widgets.BoardWidget import BoardWidget
from widgets.CreateCimbForm import CreateClimbForm
from widgets.SavedClimbsTable import SavedClimbsTable
from widgets.SaveClimbPopup import SaveClimbPopup
from widgets.MenuBar import MenuBar
from tools.JsonHandler import JsonHanlder
from widgets.SignInForm import SignInForm
# from configuration import Configuartion
from configuration_copy import UserAccountTable, Climbs, ClimbsHistory

from ui_py_files.save_climb_popup_widget import Ui_input_climb_data


class MainWidget(QWidget):
    def __init__(self, parent: QWidget = None) -> None:
        super(MainWidget, self).__init__(parent)

        self.route = []
        
        self.main_layout = QGridLayout(self)
        self.setLayout(self.main_layout)

        self.UserAccountsTable = UserAccountTable()
        self.UserAccountsTable.create_table()

        self.ClimbsTable = Climbs()
        self.ClimbsTable.create_table()

        self.ClimbsHistoryTable = ClimbsHistory()
        self.ClimbsHistoryTable.create_table()

        self.board_widget = BoardWidget()
        self.board_widget.hold_buttons_group.buttonClicked.connect\
        (self.collect_route)
        
        self.create_climb_btn = QPushButton('Create Climb')
        self.create_climb_btn.clicked.connect(self.handle_create_climb)
        self.save_climb_btn = QPushButton('Save Climb')
        self.save_climb_btn.clicked.connect(self.onSavedClimbClicked)

        self.user_button_one = QPushButton('User One')
        self.user_button_one.isCheckable()
        # self.user_button_one.clicked.connect(self.handle_sign_in)
        self.user_button_two = QPushButton('User Two')
        self.user_button_two.isCheckable()

        self.user_buttons = QButtonGroup()
        self.user_buttons.addButton(self.user_button_one)
        self.user_buttons.addButton(self.user_button_two)
        self.user_buttons.setExclusive(True)

        self.climb_ticked_button = QPushButton('Ticked')
        self.climb_ticked_button.clicked.connect(self.handle_climb_tick)

        # self.save_climb_data = SaveClimbPopup(route = self.route, db=self.ClimbsTable)
        # self.save_climb_data.widget.buttonBox.accepted.connect(self.save_climb)
        # self.save_climb_data.widget.buttonBox.rejected.connect(self.handle_cancel_create_climb)

        self.saved_climbs = SavedClimbsTable(db= self.ClimbsTable)
        # self.saved_climbs.populate_table()
        self.saved_climbs.widget.tableWidget.cellClicked.connect(self.get_route)

        # self.menu = MenuBar()

        # self.sign_in_form = SignInForm()
        # self.sign_in_form.SendUsername.connect(self.update_user_login)

        self.main_layout.addWidget(self.board_widget, 1,0)
        self.main_layout.addWidget(self.create_climb_btn, 2,0)
        self.main_layout.addWidget(self.save_climb_btn, 2,1)
        self.main_layout.addWidget(self.user_button_one, 3,0) 
        self.main_layout.addWidget(self.user_button_two, 3,1)   
        self.main_layout.addWidget(self.saved_climbs, 1,1)
        # self.main_layout.addWidget(self.menu, 0,0)
        self.main_layout.addWidget(self.climb_ticked_button, 4,0)

        self.route = []

        self.selected_climb = None

        self.climbsJSON = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'climbs_dict.json')

        
    def handle_create_climb(self):
        self.create_climb_btn.setEnabled(False)
        self.board_widget.enable_buttons()
        self.default_board()


    def collect_route(self, button):
        if button.isChecked() == True:
            self.route.append(self.board_widget.hold_buttons_group.id(button))
            button.setStyleSheet("background-color: green;")
        else:
            self.route.remove(self.board_widget.hold_buttons_group.id(button))
            button.setStyleSheet("background-color: transparent;")

    # def save_climb(self):
    #     self.create_climb_btn.setEnabled(True)
        
    #     if self.save_climb_data.climb_name and\
    #         self.save_climb_data.climb_grade and\
    #         len(self.route) > 1:
                
    #             climb_data = JsonHanlder.openJson(self.climbsJSON)
    #             climb_data[self.save_climb_data.climb_name] = \
    #                    {'route' : self.route,
    #                     'grade' : self.save_climb_data.climb_grade,
    #                     'ticks' : 0}
    #             JsonHanlder.writeJson(climb_data, self.climbsJSON)
    #     else:
    #         print('please input climb information')
    #     self.defaultUi()
    #     self.saved_climbs.populate_table()  


    def handle_cancel_create_climb(self):
        print('creating climb cancelled')
        self.defaultUi()
            
    def defaultUi(self):        
        self.create_climb_btn.setEnabled(True)
        self.route.clear()
        self.default_board()
        self.board_widget.disable_buttons()
        self.board_widget.uncheck_buttons()
      
    def get_route(self, row, column):
        self.defaultUi()

        climb_name = \
        self.saved_climbs.widget.tableWidget.item(row, column).text()
        
        climbs_dict = json.openJson(self.climbsJSON)
        
        self.display_route(climbs_dict[climb_name]['route'])

        #populating selected climb so other elements can see what programmes have been selected - not really following solid
        self.selected_climb = climb_name
        
        
    def display_route(self, route):
        for button in route:
            button_to_display = self.board_widget.hold_buttons_group.button(button)
            button_to_display.setStyleSheet("background-color: green;")
            
    def default_board(self):
        for button in self.board_widget.hold_buttons_group.buttons():
            button.setStyleSheet("background-color: transparent;")

    def onSavedClimbClicked(self):
        serialized_route = json.dumps(self.route)
        save_climb_form = SaveClimbPopup(route= serialized_route, db= self.ClimbsTable)
        save_climb_form.exec() 

    def update_user_login(self, username):
        self.user_button_one.setText(username)

    def handle_sign_in(self):
        # self.sign_in_form.exec()
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

