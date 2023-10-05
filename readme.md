# Short Changed
### A URL Shortener built using Python, FastApi, CustomTkinter and MySQL

This is a response to John Crickett's URL Shortener Coding Challenge.

See the challenge specification [here](https://codingchallenges.fyi/challenges/challenge-url-shortener).

### Installation
**Run Python:**
   - Navigate to the directory containing the code.
   - Run the code using Python: 
     - For Python 2: `python filename.py`.
     - For Python 3: `python3 filename.py`.
- Install fastapi: `pip install fastapi`  
- Install uvicorn: `pip install "uvicorn[standard]"`  
- Install mysql-connector: `pip install mysql-connector-python`
- Install customtkinter: `pip install customtkinter`
- Install validators: `pip install validators`

### Installation
- Enter terminal command: `api:shortchanged --reload`  
If successful you should see this message at localhost:8000  

![local host message](images/localhostmessage.png)
- In database.py file, replace value of password (lines 18) with your own MySQL password
- Before running the program for the first time, go to the database.py file
and uncomment lines 6-14 and 21-23 - this will allow the creation of a
MySQL database named ShortChanged the first time the program is run
(these lines will need to be commented out before the program is run again)
- Run the main.py file  

![gui screenshot](images/gui_screenshot.png)







