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

-- create completed boards for Jane so scoreboard can be generated
--INSERT INTO player (player_name) VALUE ("Jane");
--
--
--INSERT INTO boards (player_id, difficulty, completed, total_time, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9)
--VALUES (1, "medium", 1,
--CAST('00:18:53' AS TIME(0)),
--"3, 2, 1, 7, 9, 6, 5, 8, 4",
--"5, 7, 9, 1, 8, 4, 3, 2, 6",
--"6, 8, 4, 3, 2, 5, 1, 7, 9",
--"1, 4, 2, 7, 3, 9, 8, 6, 5",
--"7, 9, 3, 5, 6, 8, 2, 4, 1",
--"8, 5, 6, 4, 1, 2, 9, 3, 7",
--"9, 6, 8, 2, 7, 1, 4, 5, 3",
--"4, 1, 7, 8, 5, 3, 6, 9, 2",
--"2, 3, 5, 9, 4, 6, 7, 1, 8");
--
--INSERT INTO boards (player_id, difficulty, completed, total_time, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9)
--VALUES (1, "hard", 1,
--CAST('00:09:18' AS TIME(0)),
--"3, 2, 1, 7, 9, 6, 5, 8, 4",
--"5, 7, 9, 1, 8, 4, 3, 2, 6",
--"6, 8, 4, 3, 2, 5, 1, 7, 9",
--"1, 4, 2, 7, 3, 9, 8, 6, 5",
--"7, 9, 3, 5, 6, 8, 2, 4, 1",
--"8, 5, 6, 4, 1, 2, 9, 3, 7",
--"9, 6, 8, 2, 7, 1, 4, 5, 3",
--"4, 1, 7, 8, 5, 3, 6, 9, 2",
--"2, 3, 5, 9, 4, 6, 7, 1, 8");
--
--
--INSERT INTO boards (player_id, difficulty, completed, total_time, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9)
--VALUES (1, "medium", 1,
--CAST('00:25:03' AS TIME(0)),
--"3, 2, 1, 7, 9, 6, 5, 8, 4",
--"5, 7, 9, 1, 8, 4, 3, 2, 6",
--"6, 8, 4, 3, 2, 5, 1, 7, 9",
--"1, 4, 2, 7, 3, 9, 8, 6, 5",
--"7, 9, 3, 5, 6, 8, 2, 4, 1",
--"8, 5, 6, 4, 1, 2, 9, 3, 7",
--"9, 6, 8, 2, 7, 1, 4, 5, 3",
--"4, 1, 7, 8, 5, 3, 6, 9, 2",
--"2, 3, 5, 9, 4, 6, 7, 1, 8");
--
--INSERT INTO boards (player_id, difficulty, completed, total_time, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9)
--VALUES (1, "hard", 1,
--CAST('00:29:11' AS TIME(0)),
--"3, 2, 1, 7, 9, 6, 5, 8, 4",
--"5, 7, 9, 1, 8, 4, 3, 2, 6",
--"6, 8, 4, 3, 2, 5, 1, 7, 9",
--"1, 4, 2, 7, 3, 9, 8, 6, 5",
--"7, 9, 3, 5, 6, 8, 2, 4, 1",
--"8, 5, 6, 4, 1, 2, 9, 3, 7",
--"9, 6, 8, 2, 7, 1, 4, 5, 3",
--"4, 1, 7, 8, 5, 3, 6, 9, 2",
--"2, 3, 5, 9, 4, 6, 7, 1, 8");
--
--INSERT INTO boards (player_id, difficulty, completed, total_time, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9)
--VALUES (1, "easy", 1,
--CAST('00:03:33' AS TIME(0)),
--"3, 2, 1, 7, 9, 6, 5, 8, 4",
--"5, 7, 9, 1, 8, 4, 3, 2, 6",
--"6, 8, 4, 3, 2, 5, 1, 7, 9",
--"1, 4, 2, 7, 3, 9, 8, 6, 5",
--"7, 9, 3, 5, 6, 8, 2, 4, 1",
--"8, 5, 6, 4, 1, 2, 9, 3, 7",
--"9, 6, 8, 2, 7, 1, 4, 5, 3",
--"4, 1, 7, 8, 5, 3, 6, 9, 2",
--"2, 3, 5, 9, 4, 6, 7, 1, 8");
--
--INSERT INTO boards (player_id, difficulty, completed, total_time, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9)
--VALUES (1, "easy", 1,
--CAST('00:14:57' AS TIME(0)),
--"3, 2, 1, 7, 9, 6, 5, 8, 4",
--"5, 7, 9, 1, 8, 4, 3, 2, 6",
--"6, 8, 4, 3, 2, 5, 1, 7, 9",
--"1, 4, 2, 7, 3, 9, 8, 6, 5",
--"7, 9, 3, 5, 6, 8, 2, 4, 1",
--"8, 5, 6, 4, 1, 2, 9, 3, 7",
--"9, 6, 8, 2, 7, 1, 4, 5, 3",
--"4, 1, 7, 8, 5, 3, 6, 9, 2",
--"2, 3, 5, 9, 4, 6, 7, 1, 8");
--
--INSERT INTO boards (player_id, difficulty, completed, total_time, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9)
--VALUES (1, "hard", 1,
--CAST('01:50:22' AS TIME(0)),
--"3, 2, 1, 7, 9, 6, 5, 8, 4",
--"5, 7, 9, 1, 8, 4, 3, 2, 6",
--"6, 8, 4, 3, 2, 5, 1, 7, 9",
--"1, 4, 2, 7, 3, 9, 8, 6, 5",
--"7, 9, 3, 5, 6, 8, 2, 4, 1",
--"8, 5, 6, 4, 1, 2, 9, 3, 7",
--"9, 6, 8, 2, 7, 1, 4, 5, 3",
--"4, 1, 7, 8, 5, 3, 6, 9, 2",
--"2, 3, 5, 9, 4, 6, 7, 1, 8");
--
--
--INSERT INTO boards (player_id, difficulty, completed, total_time, row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9)
--VALUES (1, "hard", 1,
--CAST('01:50:22' AS TIME(0)),
--"3, 2, 1, 7, 9, 6, 5, 8, 4",
--"5, 7, 9, 1, 8, 4, 3, 2, 6",
--"6, 8, 4, 3, 2, 5, 1, 7, 9",
--"1, 4, 2, 7, 3, 9, 8, 6, 5",
--"7, 9, 3, 5, 6, 8, 2, 4, 1",
--"8, 5, 6, 4, 1, 2, 9, 3, 7",
--"9, 6, 8, 2, 7, 1, 4, 5, 3",
--"4, 1, 7, 8, 5, 3, 6, 9, 2",
--"2, 3, 5, 9, 4, 6, 7, 1, 8");