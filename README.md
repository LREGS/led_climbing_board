# Introduction

This a simple attempt to make your home climbing wall controllable using WS2811 addressable LEDs using the PySide GUI library and a Flask server running on a microcontroller. 

This is my first ever software project so yes its messy, yes its probably wrong, no I didn't follow an MVC architecture, yes my code is all over the place and its very buggy, but it does work... kind of. 

I'm really keen to see if others are up for contributing and helping make this an app people can really get some use out of!

# Installation 

There is no build step for the application. 

Simply clone this repo and install the requirements.txt and the application should run. 

# Home Set-Up

There isn't a no-code way of getting this application to work on your homeboard. 

At the moment the minimal number of steps required to get this working on your home wall will be the following:

## Software Set-Up
1. Create a new BoardUI.ui file using QDesigner. 
2. Add QLabel to a widget and add a QPixMap to the QLabel containing a 400x400 image of your board (feel free to rezie/change the layout of the application to your needs)
3. Overlay QPushbuttons ontop of the QLabel that will act as the buttons for your climbing wall - I set mine to transparent
4. Navigate to your UI file and do pyside6-uic BoardUI.ui - BoardUi.ui.py 
5. Now import the Widget inside of the BoardWidget class
6. You will now need to update the create_button_group function within the board widget class as it is using a magic number to build the button group for the hold buttons. The loop range should 
include all the QPushButtons you just created in QDesigner
7. Run the server.py file on your microcontroller - I used an RPI 3b+ running raspian. You will need to run the requirements.txt on your PI as well. 
8. Change the url in tools/sendClimbRequest to match your localhost. 
9. edit hold2ledconvert.py to map your led string reference with the hold number within the pyside application - this is how the server knows which light to change when you press buttons inside the app. 

## Hardware Set-Up 
1. Get a string of WS2811 addressable led strings and a 5v barrel plug adapter and plug 
2. Connect a ground to your board, and the green wire into a GPIO pin. 

Once this is completed you should have LEDs powered by a 5v cable, that is plugged into a microcontroller/pi running a flask server. You can then start the PySide application up and assuming the above is correct, you should be able to click "create route" and click on holds it will illuminate leds. 


# Contributing

I'd love for some people to start contributing to this project so that it can be improved for myself and future visitors. Selfishly, I'd also love to learn from future contributors and increase my own skill at the same time! 

I have a number of issues already in the repo, please feel free to fork and send a PR. 

If you want to chat about contributing then feel free to message me on here, william-cullum@hotmail.co.uk, or discord William#7401