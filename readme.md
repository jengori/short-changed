# Short Changed
### A URL Shortener built using Python, FastApi, CustomTkinter and MySQL

This is a response to John Crickett's URL Shortener Coding Challenge.

See the challenge specification [here](https://codingchallenges.fyi/challenges/challenge-url-shortener).

To get started:
- pip install fastapi  
- pip install "uvicorn[standard]"  
- pip install mysql-connector-python
- pip install customtkinter
- pip install validators  
- Enter terminal command api:shortchanged --reload  
If successful you should see this message at localhost:8000  

![local host message](images/localhostmessage.png)
- In database.py file, replace value of password (lines 18) with your own MySQL password
- Before running the program for the first time, go to the database.py file
and uncomment lines 6-14 and 21-23 - this will allow the creation of a
MySQL database named ShortChanged the first time the program is run
(these lines will need to be commented out before the program is run again)
- Run the main.py file  

![gui screenshot](images/gui_screenshot.png)







