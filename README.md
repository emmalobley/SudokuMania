# CFG-Final-Project
Final project for the CFGDegree

# Initial Ideas

We started out by brainstorming what we all enjoyed and discussed making some sort of puzzle game. We found an API which generates sudoku grids and solutions of varying difficulty.

Upon reviewing the API we discussed user interaction to select sudoku difficulty and the option of having a running timer.

[Sudoku API web link](https://sudoku-api.vercel.app/)

[Sudoku API](https://sudoku-api.vercel.app/api/dosuku)


# What we are building

We are building an app to play the game sudoku on.👾

# What it does

| Allows the user to play a game of sudoku, where they can choose the difficulty. | Uses an existing API to generate a sudoku board. | 
| :-------- | :------- | 
| Stores info to a DB: the uncompleted and completed sudoku, the timestamps for completion of the sudoku and the difficulty of the sudoku. | The user can request to see their highscores for each difficulty. | 


# Key Features of System
1. Menu to choose options between start a new game, continue a game, see highscores or quit.

2. When starting a new game, the system asks the user for their choice of difficulty and generates a board of the desired difficulty.

3. The user can then add numbers to the sudoku board. They cannot change numbers that are already given, but can change their inputted numbers.

4. After completing the sudoku, the system checks that the solution is correct, i.e that there are unique numbers in each row, column and box. The system also times how long it takes for the user to complete the sudoku.

5. The user has the option to restart the sudoku which would remove all their answers and leave the starting numbers. The restart starts the timer again.

6. If there is a mistake with the sudoku in the final check the system alerts the user that the sudoku has a mistake.

7. Throughout the game the user has the option to save their uncompleted sudoku game to the database where they can then continue at a later time, in this case the time pauses.

8. If the user chooses to continue and if there is a saved game currently in the database they can continue playing that game and their time starts again.

9. User can request to see their highscores for each difficulty.

    

# Sample architecture diagram of system 

![image](https://github.com/emmalobley/CFG-Final-Project/assets/147548717/5ab5f476-4c77-42ee-b46e-b6ce30535e21)


# Team approach to project work
- [workload distribution]
1. Meeting twice weekly on Wednesdays and Sundays with set goals determined at each meet. Tasks assigned on Trello board.

2. Build the database to be able to store difficulty, time and uncompleted and completed boards and the user name.
   
2.1 In python add the api calls to the api that can request the sudoku with the desired difficulty.
2.2 In python create the functions that can allow the user to add numbers to the sudoku.
2.3 In python create a function that can check whether a solution is correct.
2.4 In python add a timer function to the sudoku that ends when the sudoku has been filled and passes the correct check.



  
- [managing code]
Using GitHub we will each create a new branch when we want to add a new feature or a chore. When the code is finished we create a pull request and it requires at least one person to review before it can be merged to the main branch.




- [testing system]
In the project we will have at least one folder where we will keep unit tests. As we write the code we will add unit tests and test the functionality of the code.
After we have created the system we will run user tests to check that the system works for the user and has all the functionality that we aimed to have.








