# SudokuMania!

SudokuMania is Team 2's final project for the CFGDegree!

Completed in Python using MySQL for database creation and connection.

Test your sudoku skills by running this app! 👾👾👾

## Project Description


### API use 💡

This project uses an existing API which generates sudoku boards of varying difficulty.

This API is free and does not require any authentication!

You can retrieve sudoku from this 
[Sudoku API web link](https://sudoku-game-and-api.netlify.app)

### Database connection 🔢

We use a MySQL connector to access and store data to a database called sudoku.
The available code to create the database is stored in sql_code.sql file of this project.
Information on how to set up the database is included in the user instructions section of this file.

### Use of classes

This project creates objects of the class SudokuBoard.

### User interaction

When running this program the user is asked to input their name, which is stored to a players table in the database and allows the database to later store and retrieve relevant boards played by the user.

The user will then be asked to select from a list of available options:
1. Start a new game
2. Continue an existing game
3. View Highscores
4. Exit the program

These options will remain available until the user wishes to exit the program.

If the user chooses option 1 the program will make a call to the API and generate a new board.
The board is then converted to a readable format and the user is able to play the game -
i.e. can select number they wish to enter into a given row or column. Each play of a game is timed stored to the database.

If the user wishes to continue an existing game the program will return the most recent uncompleted game for that user
and the user is able to play the game as previous. The new time will get added to the old time for the game.

If the user wishes to view highscores the program will return all difficulties and times from the database and present
to the user as a scoreboard with relevant scoring based on difficulty and play time. 


## User instructions 👩‍💻

To run the program the user must first create the database in mysql by running the commands written in the file sql_code.sql.

The user must then allow a connection by updating the ‘HOST’, ‘USER’ and ‘PASSWORD’ values in the file config.py to the relevant values (username and password as set during MySQL installation).

If the user has not previously installed the mysql-connector then they must also run it in their terminal:

```bash
-m pip install mysql-connector-python 
```

Upon completion of these prerequisites, the user will be able to accurately and easily run the main.py file within their Python environment by pressing run.

Doing so will stimulate the beginning actions as described in the user interactions.


