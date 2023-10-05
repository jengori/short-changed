"""  To begin, enter the command
api:shortchanged --reload
in the terminal

Visit localhost:8000 in your web browser, and you should see the message:
"Hello! You have been": "short changed"

In database.py file, replace values of password (lines 18 and 19) with your own MySQL password

Run the main.py file
"""
from gui import Gui
gui = Gui()
gui.window.mainloop()
