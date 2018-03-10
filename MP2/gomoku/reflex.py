class Reflex:
    def __init__(self):
        pass
    
    def find_move(self, board, player):
        if player == 'x':
            opponent = 'o'
        elif player == 'o':
            opponent = 'x'
        else:
            print('I don\'t know you.')
            return -1, -1
        
        row, col = board.row_has_four(player)
        if (row, col) == (-1, -1):
            row, col = board.col_has_four(player)
            if (row, col) == (-1, -1):
                row, col = board.l2r_has_four(player)
                if (row, col) == (-1, -1):
                    row, col = board.r2l_has_four(player)
                    if (row, col) == (-1, -1):
                        pass
                    elif board.is_movable(row + 4, col - 4):
                        return row + 4, col - 4
                    elif board.is_movable(row - 1, col + 1):
                        return row - 1, col + 1
                elif board.is_movable(row - 1, col - 1):
                    return row - 1, col - 1
                elif board.is_movable(row + 4, col + 4):
                    return row + 4, col + 4
            elif board.is_movable(row + 4, col):
                return row + 4, col
            elif board.is_movable(row - 1, col):
                return row - 1, col
        elif board.is_movable(row, col - 1):
            return row, col - 1
        elif board.is_movable(row, col + 4):
            return row, col + 4
        
        row, col = board.row_has_four(opponent)
        if (row, col) == (-1, -1):
            row, col = board.col_has_four(opponent)
            if (row, col) == (-1, -1):
                row, col = board.l2r_has_four(opponent)
                if (row, col) == (-1, -1):
                    row, col = board.r2l_has_four(opponent)
                    if (row, col) == (-1, -1):
                        pass
                    elif board.is_movable(row + 4, col - 4):
                        return row + 4, col - 4
                    elif board.is_movable(row - 1, col + 1):
                        return row - 1, col + 1
                elif board.is_movable(row - 1, col - 1):
                    return row - 1, col - 1
                elif board.is_movable(row + 4, col + 4):
                    return row + 4, col + 4
            elif board.is_movable(row + 4, col):
                return row + 4, col
            elif board.is_movable(row - 1, col):
                return row - 1, col
        elif board.is_movable(row, col - 1):
            return row, col - 1
        elif board.is_movable(row, col + 4):
            return row, col + 4
        
        row, col = board.row_has_three(opponent)
        if (row, col) == (-1, -1):
            row, col = board.col_has_three(opponent)
            if (row, col) == (-1, -1):
                row, col = board.l2r_has_three(opponent)
                if (row, col) == (-1, -1):
                    row, col = board.r2l_has_three(opponent)
                    if (row, col) == (-1, -1):
                        pass
                    elif board.is_movable(row + 3, col - 3) and board.is_movable(row - 1, col + 1):
                        return row + 3, col - 3
                elif board.is_movable(row - 1, col - 1) and board.is_movable(row + 3, col + 3):
                    return row - 1, col - 1
            elif board.is_movable(row + 3, col) and board.is_movable(row - 1, col):
                return row + 3, col
        elif board.is_movable(row, col - 1) and board.is_movable(row, col + 3):
            return row, col - 1
            
        return -1, -1
        
        # test for consecutive four
        