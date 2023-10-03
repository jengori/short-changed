"""  To begin, enter the command
api:shortchanged --reload
in the terminal

Visit localhost:8000 in your web browser, and you should see the message:
"Hello! You have been": "short changed"

In database.py file, replace values of password (lines 18 and 19) with your own MySQL password

Before running the program for the first time, go to the database.py file
and uncomment lines 6-14 and 21-23 - this will allow the creation of a
MySQL database named ShortChanged the first time the program is run
(these lines will need to be commented out before the program is run again)

Run the main.py file
"""
from gui import Gui
gui = Gui()
gui.window.mainloop()