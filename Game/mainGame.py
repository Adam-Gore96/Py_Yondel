import MySQLdb
import mysql.connector
import self as self

import Part_One


# Connect
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="password",
                     db="yondel_game")

cursor = db.cursor()


class Games:
        def login(games_type: str):

            game_type = games_type.upper()
            new_username = ""
            new_password = ""
            login_accept = 0
            while login_accept == 0:
                if game_type == "NEW":
                    check = 0
                    while check == 0:
                        new_username = input("Enter a username")
                        new_password = input("Enter a password:")
                        check_password = input("Enter password again:")
                        if check_password == new_password:
                            try:
                                cursor.execute(f"INSERT INTO PLAYERS (username,password,game_state) Values('{new_username}','{new_password}',1)")
                                check = 1
                            except:
                                print("Error Username already exists")
                                check = 0
                        else:
                            print("Passwords do not match")

                elif game_type == "SAVED":
                    check = 0
                    password_wrong_count = 0
                    while check == 0:
                        if check != 2:
                            input_username = input("Please Enter your Username")
                            input_password = input("Please Enter Your Password")
                            cursor.execute(f"select * from players where username = '{input_username}' AND password ='{input_password}'")
                            row = cursor.rowcount
                            if row == 1:
                                check = 1
                                login_accept = 1
                            elif password_wrong_count != 3:
                                print("Username or Password is incorrect, please try again")
                                password_wrong_count += 1
                                remaining_chances = 3 - password_wrong_count
                                print(f"You have {remaining_chances} chance(s) left")
                            else:
                                print("You have entered the wrong password too many times, closing")
                                check = 2
                        elif check == 2:
                            quit()


