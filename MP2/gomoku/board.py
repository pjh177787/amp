import numpy as np

class Board:
    def __init__(self):
        self.board = np.array([['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.']])
    
    def prt(self):
        for row in self.board:
            prt_str = ''
            for cell in row:
                prt_str += cell + ' '
            print(prt_str)
        print()
        
    def get_board(self):
        return self.board
        
    def get_space(self):
        spaces = []
        for row in self.board:
            for cell in row:
                if cell == '.':
                    spaces.append((row, cell))
        return spaces
    
    def is_movable(self, row, col):
        if row < 0 or row > 6 or col < 0 or col > 6:
            return False
        return self.board[row][col] == '.'
    
    def is_friend(self, row, col, player):
        if row < 0 or row > 6 or col < 0 or col > 6:
            return False
        if player == 'red':
            return self.board[row][col].islower()
        else:
            return self.board[row][col].isupper()
    
    def make_move(self, row, col, alfa):
        if not self.board[row][col] == '.':
            print('Can\'t  play here.')
        else:
            self.board[row][col] = alfa
                
    def get_player_places(self, player):
        if player == 'red':
            red_places = []
            for row in self.board:
                for cell in row:
                    if cell.islower():
                        red_places.append((row, cell))
            return red_places
        elif player == 'blue':
            blue_places = []
            for row in self.board:
                for cell in row:
                    if cell.isupper():
                        blue_places.append((row, cell))
            return blue_places
        else:
            print('I don\'t know you.')
        return places
    
    def find_winning_block(self, player):
        row_wb_list = sorted(self.row_has_winning_block(player), reverse = True)
        # print(row_wb_list)
        col_wb_list = sorted(self.col_has_winning_block(player), reverse = True)
        # print(col_wb_list)
        l2r_wb_list = sorted(self.l2r_has_winning_block(player), reverse = True)
        # print(l2r_wb_list)
        r2l_wb_list = sorted(self.r2l_has_winning_block(player), reverse = True)
        # print(r2l_wb_list)
        
        max_wb_list = max(row_wb_list[0][0], col_wb_list[0][0], l2r_wb_list[0][0], r2l_wb_list[0][0])
        
        moves = []
        
        for wb in l2r_wb_list:
            if wb[0] == max_wb_list:
                row_s, col_s = wb[1]
                row_t, col_t = wb[2]
                if self.is_movable(row_s - 1, col_s - 1) and self.is_friend(row_s, col_s, player):
                    moves.append((row_s - 1, col_s - 1))
                    break
                else:
                    for i in range(5):
                        if self.is_movable(row_s + i, col_s + i) and (self.is_friend(row_s + i + 1, col_s + i + 1, player) or self.is_friend(row_s + i - 1, col_s + i - 1, player)):
                            moves.append((row_s + i, col_s + i))
                            break
            else:
                break
                    
        for wb in row_wb_list:
            if wb[0] == max_wb_list:
                row_s, col_s = wb[1]
                row_t, col_t = wb[2]
                if self.is_movable(row_s, col_s - 1) and self.is_friend(row_s, col_s, player):
                    moves.append((row_s, col_s - 1))
                    break
                else:
                    for col in range(col_s, col_t + 1):
                        if self.is_movable(row_s, col) and (self.is_friend(row_s, col + 1, player) or self.is_friend(row_s, col - 1, player)):
                            moves.append((row_s, col))
                            break
            else:
                break
                
        for wb in r2l_wb_list:
            if wb[0] == max_wb_list:
                row_s, col_s = wb[1]
                row_t, col_t = wb[2]
                if self.is_movable(row_s - 1, col_s + 1) and self.is_friend(row_s, col_s, player):
                    moves.append((row_s - 1, col_s + 1))
                    break
                else:
                    for i in range(5):
                        if self.is_movable(row_s + i, col_s + i) and (self.is_friend(row_s + i + 1, col_s + i - 1, player) or self.is_friend(row_s + i - 1, col_s + i + 1, player)):
                            moves.append((row_s + i, col_s + i))
                            break
            else:
                break   
                
        for wb in col_wb_list:
            if wb[0] == max_wb_list:
                row_s, col_s = wb[1]
                row_t, col_t = wb[2]
                if self.is_movable(row_s - 1, col_s) and self.is_friend(row_s, col_s, player):
                    moves.append((row_s - 1, col_s))
                    break
                else:
                    for row in range(row_s, row_t + 1):
                        if self.is_movable(row, col_s) and (self.is_friend(row + 1, col_s, player) or self.is_friend(row - 1, col_s, player)):
                            moves.append((row, col_s))
                            break
            else:
                break             
                        
        if len(moves) == 0:
            return -1, -1
        else:
            moves = sorted(moves, key=lambda tup:(tup[1], tup[0]))
            print(moves)
            return moves[0]
                                      
         
    def check_winner(self):
        if not self.row_has_five('red') == (-1, -1):
            return 'red'
        if not self.col_has_five('red') == (-1, -1):
            return 'red'
        if not self.l2r_has_five('red') == (-1, -1):
            return 'red'
        if not self.r2l_has_five('red') == (-1, -1):
            return 'red'
        if not self.row_has_five('blue') == (-1, -1):
            return 'blue'
        if not self.col_has_five('blue') == (-1, -1):
            return 'blue'
        if not self.l2r_has_five('blue') == (-1, -1):
            return 'blue'
        if not self.r2l_has_five('blue') == (-1, -1):
            return 'blue'
        return 'not yet'
    
    def check_has_four(self, player):
        starts = self.l2r_has_four(player)
        if not len(starts) == 0:
            for start in starts:
                row, col = start
                if self.is_movable(row - 1, col - 1):
                    return row - 1, col - 1
                elif self.is_movable(row + 4, col + 4):
                    return row + 4, col + 4
        starts = self.row_has_four(player)
        if not len(starts) == 0:
            for start in starts:
                row, col = start
                if self.is_movable(row, col - 1):
                    return row, col - 1
                elif self.is_movable(row, col + 4):
                    return row, col + 4
        starts = self.r2l_has_four(player)
        if not len(starts) == 0:
            for start in starts:
                row, col = start
                if self.is_movable(row + 1, col - 1):
                    return row + 1, col - 1
                elif self.is_movable(row - 4, col + 4):
                    return row - 4, col + 4
        starts = self.col_has_four(player)
        if not len(starts) == 0:
            for start in starts:
                row, col = start
                if self.is_movable(row - 1, col):
                    return row - 1, col
                elif self.is_movable(row + 4, col):
                    return row + 4, col
        return -1, -1
        
       
        
    def check_has_three(self, player):
        starts = self.l2r_has_three(player)
        if not len(starts) == 0:
            for start in starts:
                row, col = start
                if self.is_movable(row - 1, col - 1):
                    return row - 1, col - 1
                elif self.is_movable(row + 3, col + 3):
                    return row + 3, col + 3
        starts = self.row_has_three(player)
        if not len(starts) == 0:
            for start in starts:
                row, col = start
                if self.is_movable(row, col - 1):
                    return row, col - 1
                elif self.is_movable(row, col + 3):
                    return row, col + 3
        starts = self.r2l_has_three(player)
        if not len(starts) == 0:
            for start in starts:
                row, col = start
                if self.is_movable(row + 1, col - 1):
                    return row + 1, col - 1
                elif self.is_movable(row - 3, col + 3):
                    return row - 3, col + 3
        return -1, -1
        starts = self.col_has_three(player)
        if not len(starts) == 0:
            for start in starts:
                row, col = start
                if self.is_movable(row - 1, col):
                    return row - 1, col
                elif self.is_movable(row + 3, col):
                    return row + 3, col
        return -1, -1

    
    def row_has_five(self, player):
        bd = self.get_board()
        for row in range(7):
            for col in range(3):
                flag = True
                for cell in bd[row, col:col+5]:
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    return row, col
        # print('Not found')
        return -1, -1
    
    def col_has_five(self, player):
        bd = self.get_board()
        for row in range(3):
            for col in range(7):
                flag = True
                for cell in bd[row:row+5, col]:
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    return row, col
        # print('Not found')
        return -1, -1
    
    def r2l_has_five(self, player):
        bd = self.get_board()
        for row in range(4, 7):
            for col in range(3):
                flag = True
                for i in range(5):
                    cell = bd[row-i, col+i]
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    return row, col
        # print('Not found')
        return -1, -1
    
    def l2r_has_five(self, player):
        bd = self.get_board()
        for row in range(3):
            for col in range(3):
                flag = True
                for i in range(5):
                    cell = bd[row+i, col+i]
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    return row, col
        # print('Not found')
        return -1, -1
    
    def row_has_four(self, player):
        bd = self.get_board()
        starts = []
        for row in range(7):
            for col in range(4):
                flag = True
                # print(bd[row, col:col+4])
                for cell in bd[row, col:col+4]:
                    if player == 'red' and not cell.islower():
                        # print(cell)
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:
                    # print(row, col, 'has four')
                    starts.append((row, col))
        return starts
        # print('Not found')
        return -1, -1
    
    def col_has_four(self, player):
        bd = self.get_board()
        starts = []
        for col in range(7):
            for row in range(4):
                flag = True
                # print(bd[row:row+4, col])
                for cell in bd[row:row+4, col]:
                    # print(flag)
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    # print(row, col, 'has four')
                    starts.append((row, col))
        return starts
        # print('Not found')
        return -1, -1
    
    def l2r_has_four(self, player):
        bd = self.get_board()
        starts = []
        for col in range(4):
            for row in range(4):
                flag = True
                for i in range(4):
                    cell = bd[row+i, col+i]
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:
                    starts.append((row, col))
        return starts
        # print('Not found')
        return -1, -1
    
    def r2l_has_four(self, player):
        bd = self.get_board()
        starts = []
        for col in range(4):
            for row in range(3, 7):
                flag = True
                for i in range(4):
                    cell = bd[row-i, col+i]
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:
                    starts.append((row, col))
        return starts
        # print('Not found')
        return -1, -1
    
    def row_has_three(self, player):
        bd = self.get_board()
        starts = []
        for row in range(7):
            for col in range(5):
                flag = True
                for cell in bd[row, col:col+3]:
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    starts.append((row, col))
        return starts
        # print('Not found')
        return -1, -1
    
    def col_has_three(self, player):
        bd = self.get_board()
        starts = []
        for col in range(7):
            for row in range(5):
                flag = True
                for cell in bd[row:row+3, col]:
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:       
                    starts.append((row, col))
        return starts
        # print('Not found')
        return -1, -1
    
    def l2r_has_three(self, player):
        bd = self.get_board()
        starts = []
        for col in range(5):
            for row in range(5):
                flag = True
                for i in range(3):
                    cell = bd[row+i, col+i]
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:
                    starts.append((row, col))
        return starts
        # print('Not found')
        return -1, -1
    
    def r2l_has_three(self, player):
        bd = self.get_board()
        starts = []
        for col in range(5):
            for row in range(2, 7):
                flag = True
                for i in range(3):
                    cell = bd[row-i, col+i]
                    if player == 'red' and not cell.islower():
                        flag = False
                        break
                    elif player == 'blue' and not cell.isupper():
                        flag = False
                        break
                if flag:
                    starts.append((row, col))
        return starts
        # print('Not found')
        return -1, -1
    
    def row_has_winning_block(self, player):
        bd = self.get_board()
        wb_list = []
        for row in range(7):
            for col in range(3):
                count = 0
                flag = True
                for cell in bd[row, col:col+5]:
                    if player == 'red':
                        if cell.islower():
                            count += 1
                        elif cell.isupper():
                            flag = False
                            break
                    elif player == 'blue':
                        if cell.isupper():
                            count += 1
                        elif cell.islower():
                            flag = False
                            break
                if flag:
                    wb_list.append((count, (row, col), (row, col + 4)))
        return wb_list
    
    def col_has_winning_block(self, player):
        bd = self.get_board()
        wb_list = []
        for row in range(3):
            for col in range(7):
                count = 0
                flag = True
                for cell in bd[row:row+5, col]:
                    if player == 'red':
                        if cell.islower():
                            count += 1
                        elif cell.isupper():
                            flag = False
                            break
                    elif player == 'blue':
                        if cell.isupper():
                            count += 1
                        elif cell.islower():
                            flag = False
                            break
                if flag:
                    wb_list.append((count, (row, col), (row + 4, col)))
        return wb_list 
    
    def l2r_has_winning_block(self, player):
        bd = self.get_board()
        wb_list = []
        for row in range(3):
            for col in range(3):
                count = 0
                flag = True
                for i in range(5):
                    cell = bd[row+i, col+i]
                    if player == 'red':
                        if cell.islower():
                            count += 1
                        elif cell.isupper():
                            flag = False
                            break
                    elif player == 'blue':
                        if cell.isupper():
                            count += 1
                        elif cell.islower():
                            flag = False
                            break
                if flag:
                    wb_list.append((count, (row, col), (row + 4, col + 4)))
        return wb_list
    
    def r2l_has_winning_block(self, player):
        bd = self.get_board()
        wb_list = []
        for row in range(4, 7):
            for col in range(3):
                count = 0
                flag = True
                for i in range(5):
                    cell = bd[row-i, col+i]
                    if player == 'red':
                        if cell.islower():
                            count += 1
                        elif cell.isupper():
                            flag = False
                            break
                    elif player == 'blue':
                        if cell.isupper():
                            count += 1
                        elif cell.islower():
                            flag = False
                            break
                if flag:
                    wb_list.append((count, (row, col), (row + 4, col - 4)))
        return wb_list
                     
    