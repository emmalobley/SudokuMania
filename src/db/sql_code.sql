CREATE DATABASE sudoku;
USE sudoku;

-- creating tables
CREATE TABLE player
	(player_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    player_name VARCHAR(50) NOT NULL
    );

CREATE TABLE boards
	(board_id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
    player_id INTEGER NOT NULL,
    difficulty VARCHAR(50) NOT NULL,
    completed BOOLEAN, -- can make NOT NULL later -- input can be True or False rather that 0 or 1
    total_time TIME,
	row_1 VARCHAR(25), -- varchar is used as there is a mix of numbers, commas, and spaces. 25 is the max number of characters in each row, i counted
    row_2 VARCHAR(25), -- can make NOT NULL later
    row_3 VARCHAR(25),
    row_4 VARCHAR(25),
    row_5 VARCHAR(25),
    row_6 VARCHAR(25),
    row_7 VARCHAR(25),
    row_8 VARCHAR(25),
    row_9 VARCHAR(25)
    );

-- assigning foreign keys

ALTER TABLE boards
	ADD CONSTRAINT fk_player_board
	FOREIGN KEY (player_id)
	REFERENCES player(player_id);
