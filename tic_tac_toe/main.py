# random library for toss related thing
import random

# game class for every game
class Game : 
    
    def __init__(self, player_1, player_2):
        self.__player_1 = player_1
        self.__player_2 = player_2
        self.__player_1_char = random.choice(["x", "o"])
        if(self.__player_1_char == "x"):
            self.__player_2_char = "o"
        else:
            self.__player_2_char = "x"
        self.__current_winner = ""
        
        # performing a choice for first chance of char
        self.__current_chance_char = random.choice([self.__player_1_char, self.__player_2_char])
        
        if(self.__current_chance_char == self.__player_1_char):
            self.__current_chance_player = self.__player_1
        else:
            self.__current_chance_player = self.__player_2

        self.__game_grid = [['', '', ''],['', '', ''],['', '', '']]
    
    def info(self):
        return f""" 
                [  
                Player 1 : {self.__player_1}  
                Player 2 : {self.__player_2}  
                Player 1 Char : {self.__player_1_char}  
                Player 2 Char : {self.__player_2_char} 
                Game Winner : {self.__current_winner}  
                Current Chance Char : {self.__current_chance_char}
                Current Chance Player: {self.__current_chance_player}  
                Game Positions : {self.__game_grid} 
                ]"""
    
    # winning sets for current grid
    winning_sets = [
        # horizontal move sets
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # vertical move sets
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        # diagonal mover sets
        [(0,0), (1,1), (2,2)],
        [(2,2), (1,1), (0,0)],
        ]
    
    # get game attributes
    def get_attribute(self, attribute):
        if(attribute == "game_grid"):
            return self.__game_grid
        elif(attribute == "player_1"):
            return self.__player_1
        elif(attribute == "player_2"):
            return self.__player_2
        elif(attribute == "player_1_char"):
            return self.__player_1_char
        elif(attribute == "player_2_char"):
            return self.__player_2_char
        elif(attribute == "current_chance_char"):
            return self.__current_chance_char
        elif(attribute == "current_chance_player"):
            return self.__current_chance_player
        elif(attribute == "current_winner"):
            return self.__current_winner
        else:
            print(f"Please provide valid attribute, the attribute provided : {attribute} is not valid. ")
    
    # get game grid data at specific position
    def get_game_grid_position (self, row, col):
        return self.__game_grid[row-1][col-1]

    # set game char positions
    def enter_game_char_positions (self, char, row, col):
        self.__game_grid[row - 1][col-1] = char
        if(self.__current_chance_char == "x"):
            self.__current_chance_char = "o"
        else:
            self.__current_chance_char = "x"
        
        if(self.__current_chance_char == self.__player_1_char):
            self.__current_chance_player = self.__player_1
        else:
            self.__current_chance_player = self.__player_2
    
    # checking for winner
    def check_winner(self):
        game_grid = self.__game_grid
        winning_sets = self.winning_sets
        for winning_row in winning_sets:
            # all row positions
            row_position_1 = winning_row[0][0]
            row_position_2 = winning_row[1][0]
            row_position_3 = winning_row[2][0]
            # all col positions
            col_position_1 = winning_row[0][1]
            col_position_2 = winning_row[1][1]
            col_position_3 = winning_row[2][1]
            # print(winning_row)
            # print(game_grid[row_position_1][col_position_1] ,
            #        game_grid[row_position_2][col_position_2] , game_grid[row_position_3][col_position_3])

            if(len(game_grid[row_position_1][col_position_1]) > 0 and len(game_grid[row_position_2][col_position_2]) > 0 and len(game_grid[row_position_3][col_position_3]) > 0 ):    
                if(game_grid[row_position_1][col_position_1] == game_grid[row_position_2][col_position_2] == game_grid[row_position_3][col_position_3] ) :
                    # print("winner")
                    if(self.__player_1_char == game_grid[row_position_3][col_position_3]):
                        self.__current_winner = self.__player_1
                    else:
                        self.__current_winner = self.__player_2
                    
            else:
                self.__current_winner = ''
        return self.__current_winner
                
        
# game start function
def enter_game_details() : 
    # getting names of players
    player_1 = str(input('Enter player 1 name : \n =>  '))
    player_2 = str(input('Enter player 2 name : \n =>  '))

    if(player_1 == player_2):
        print("Both players should have different names")
        return
    # starting new game
    new_game = Game(player_1, player_2)
    return new_game

start_game = enter_game_details()


def play_game(player) :
    
    winner = start_game.check_winner()
    # print(winner)
    if(len(winner) > 0):
        print(f"Player {winner} has won the game")
        return
    
    # printing player and its char 
    print('Player : ', start_game.get_attribute("current_chance_player"))
    print('Char : ', start_game.get_attribute("current_chance_char"))

    # printing tutorial for current chance player
    print(f"""
          {player} your turn.
          To play your turn simply enter the row number from (1,2,3)
          and column number (1,2,3) to place your character there,
          if the place is already filled you will be prompted to play again.
    """)

    # asking positions to enter the player's char in game grid
    def choose_position_to_play():
        play_position_row = int(input('Enter row position : \n => '))
        if(not 0 < play_position_row < 4) :
            play_position_row = int(input('Row position could be 1,2,or 3 Enter row position : \n => '))
        play_position_col = int(input('Enter col position : \n => '))
        if(not 0 < play_position_col < 4) :
            play_position_col = int(input('Col position could be 1,2,or 3 Enter Col position : \n => '))

        return{"row" : play_position_row ,"col" : play_position_col}
    
    player_positions = choose_position_to_play()
    play_position_row = player_positions.get('row')
    play_position_col = player_positions.get('col')

    # getting entered grid status
    current_grid_position_status = start_game.get_game_grid_position(play_position_row, play_position_col)
    print(current_grid_position_status)

    # entering char only if grid is empty
    if(current_grid_position_status == ""):
        start_game.enter_game_char_positions(start_game.get_attribute("current_chance_char"),play_position_row, play_position_col)
    else:
        print(f"""
              Grid Position {play_position_row, play_position_col} already filled.
              Please Enter another position.
              """)
        player_positions = choose_position_to_play()
    # showing grid status after entering char
    print(start_game.get_attribute("game_grid"))
    play_game(start_game.get_attribute("current_chance_player"))



    

play_game(start_game.get_attribute("current_chance_player"))
