class Reflex:
    def __init__(self, player):
        self.blue_alfa = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.red_alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 'e', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.move = 0
        if player == 'blue':
            self.player = 'blue'
            self.opponent = 'red'
            self.all_alfa = self.blue_alfa
        elif player == 'red':
            self.player = 'red'
            self.opponent = 'blue'
            self.all_alfa = self.red_alfa
        else:
            print('I don\'t know you.')
    
    def force_move(self, row, col):
        alfa = self.all_alfa[self.move]
        self.move += 1
        return row, col, alfa
    
    def find_move(self, board):
        alfa = self.all_alfa[self.move]
        self.move += 1
        
        row, col = board.row_has_four(self.player)
        if (row, col) == (-1, -1):
            row, col = board.col_has_four(self.player)
            if (row, col) == (-1, -1):
                row, col = board.l2r_has_four(self.player)
                if (row, col) == (-1, -1):
                    row, col = board.r2l_has_four(self.player)
                    if (row, col) == (-1, -1):
                        pass
                    elif board.is_movable(row - 1, col + 1):
                        return row - 1, col + 1, alfa
                    elif board.is_movable(row + 4, col - 4):
                        return row + 4, col - 4, alfa
                elif board.is_movable(row - 1, col - 1):
                    return row - 1, col - 1, alfa
                elif board.is_movable(row + 4, col + 4):
                    return row + 4, col + 4, alfa
            elif board.is_movable(row - 1, col):
                return row - 1, col, alfa
            elif board.is_movable(row + 4, col):
                return row + 4, col, alfa
        elif board.is_movable(row, col - 1):
            return row, col - 1, alfa
        elif board.is_movable(row, col + 4):
            return row, col + 4, alfa
        
        row, col = board.row_has_four(self.opponent)
        if (row, col) == (-1, -1):
            row, col = board.col_has_four(self.opponent)
            if (row, col) == (-1, -1):
                row, col = board.l2r_has_four(self.opponent)
                if (row, col) == (-1, -1):
                    row, col = board.r2l_has_four(self.opponent)
                    if (row, col) == (-1, -1):
                        pass
                    elif board.is_movable(row - 1, col + 1):
                        return row - 1, col + 1, alfa
                    elif board.is_movable(row + 4, col - 4):
                        return row + 4, col - 4, alfa
                elif board.is_movable(row - 1, col - 1):
                    return row - 1, col - 1, alfa
                elif board.is_movable(row + 4, col + 4):
                    return row + 4, col + 4, alfa
            elif board.is_movable(row - 1, col):
                return row - 1, col, alfa
            elif board.is_movable(row + 4, col):
                return row + 4, col, alfa
        elif board.is_movable(row, col - 1):
            return row, col - 1, alfa
        elif board.is_movable(row, col + 4):
            return row, col + 4, alfa
        
        row, col = board.row_has_three(self.player)
        if (row, col) == (-1, -1):
            row, col = board.col_has_three(self.player)
            if (row, col) == (-1, -1):
                row, col = board.l2r_has_three(self.player)
                if (row, col) == (-1, -1):
                    row, col = board.r2l_has_three(self.player)
                    if (row, col) == (-1, -1):
                        pass
                    elif board.is_movable(row + 3, col - 3) and board.is_movable(row - 1, col + 1):
                        return row - 1, col + 1, alfa
                elif board.is_movable(row - 1, col - 1) and board.is_movable(row + 3, col + 3):
                    return row - 1, col - 1, alfa
            elif board.is_movable(row + 3, col) and board.is_movable(row - 1, col):
                return row -1 , col, alfa
        elif board.is_movable(row, col - 1) and board.is_movable(row, col + 3):
            return row, col - 1, alfa
        
        row, col = board.find_winning_block(self.player)
        return row, col, alfa
            
        return -1, -1, alfa
        
        # test for consecutive four
        