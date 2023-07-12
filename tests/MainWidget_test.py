import unittest
import sys 
import os.path 

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from PySide6.QtCore import QtMsgType, QObject, Qt
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtTest import QTest
from PySide6.QtGui import QPalette, QColor

from main import MainWindow
from widgets.MainWidget import MainWidget



class TestGui(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])
        
    @classmethod
    def tearDownClass(cls):
        cls.app.quit()
        cls.app.exit()
    
    def setUp(self):
        self.window = MainWindow(self.app)
        self.main_widget = self.window.main_widget
        
    def tearDown(self):
         self.app.quit()
         self.app.exit()
         
         
    def test_holdbuttons(self):
        
        for button in self.main_widget.board_widget.hold_buttons_group.buttons():
            QTest.mouseClick(button, Qt.LeftButton)
            assert self.main_widget.route == []
            #self.assertFalse(button.isEnabled())
    
    
    def test_CreateClimb(self):
    
        
        QTest.mouseClick(self.main_widget.create_climb_btn, Qt.LeftButton)
        self.assertFalse(self.main_widget.create_climb_btn.isEnabled()) 
        self.assertTrue(self.main_widget.create_climb_form_widget.widget.saveClimb.isEnabled()) 
        self.assertTrue(self.main_widget.create_climb_form_widget.widget.cancelcreation.isEnabled())
        for button in self.main_widget.board_widget.hold_buttons_group.buttons():
            self.assertTrue(button.isEnabled())
            
    def test_CancelCreateClimb(self):
    
        QTest.mouseClick(self.main_widget.create_climb_btn, Qt.LeftButton)
        
        for button in self.main_widget.board_widget.hold_buttons_group.buttons():
            QTest.mouseClick(button, Qt.LeftButton)
        
        QTest.mouseClick(self.main_widget.create_climb_form_widget\
                        .widget.cancelcreation, Qt.LeftButton)
        self.assertTrue(self.main_widget.create_climb_btn.isEnabled())
        self.assertFalse(self.main_widget.\
                        create_climb_form_widget.widget.saveClimb.isEnabled())
        self.assertFalse(self.main_widget.create_climb_form_widget.\
                        widget.cancelcreation.isEnabled())
        for button in self.main_widget.board_widget.hold_buttons_group.buttons():
            
            #self.assertFalse(button.isEnabled())
            #assert button.palette() == QColor("transparent")
            self.assertFalse(button.isChecked())

        
if __name__ == '__main__':
    unittest.main()