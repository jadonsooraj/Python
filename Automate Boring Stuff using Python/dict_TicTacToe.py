def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-*-*-')
    print(board['ML']+ '|'+ board['MM']+ '|'+ board['MR'])
    print('-*-*-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
    the_board = {'TL':'', 'TM':'', 'TR':'',
                 'ML':'', 'MM':'', 'MR':'',
                 'BL':'', 'BM':'', 'BR':'' }

     
    turn='X'
    

    for i in range(9):
        print('/n ======================= /n')
        print_board(the_board)
        
        print('Turn for ' + turn + '. Move on with space?')
        move=input()

        the_board[move]=turn

        if turn =='X':
            turn='0'
        else:
            trun='X'
        
        print_board(the_board)
        print('/n =======================/n')


if __name__ == "__main__":
    main()