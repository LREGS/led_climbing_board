from create_clmb_dlg import CreateClimbDlg
import time

def create_climbs(self):
    """Starts tracking user input to create a climb ***POC*** """
    self.create_climb_btn.clicked.connect(self.create_climb_dialogue)

    dlg = CreateClimbDlg()
    
    #If user presses ok start tracking input
    if dlg.exec():
        self.creation_actv = True
    else:
        self.creation_actv = False
     
    #Isolates the UI state to allow user to create climb    
    self.create_climb_btn.setEnabled(False)
    
    while self.creation_actv:
        print('tracking clicks')
        time.sleep(2)