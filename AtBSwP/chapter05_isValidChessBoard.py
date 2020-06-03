# Write a function that takes a dictionary argument and returns information if chessboard is correctly set up
#
# A valid board will have exactly one black king and exactly one white king. Each player can only have at most 16 pieces, at most 8 pawns, and all pieces must be on a valid space from '1a' to '8h'; that is, a piece can’t be on space '9z'. The piece names begin with either a 'w' or 'b' to represent white or black, followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'. This function should detect when a bug has resulted in an improper chess board.
# Edit: Plus some additional check invented by my self to check correctness of chessboard, colours of figures and something more.

perfectBoard = \
    dict(h8='b_rook', g8='b_knight', f8='b_bishop', e8='b_queen', d8='b_king', c8='b_bishop', b8='b_knight',
         a8='b_rook', h7='b_pawn', g7='b_pawn', f7='b_pawn', e7='b_pawn', d7='b_pawn', c7='b_pawn', b7='b_pawn',
         a7='b_pawn', h2='w_pawn', g2='w_pawn', f2='w_pawn', e2='w_pawn', d2='w_pawn', c2='w_pawn', b2='w_pawn',
         a2='w_pawn', h1='w_rook', g1='w_knight', f1='w_bishop', e1='w_queen', d1='w_king', c1='w_bishop',
         b1='w_knight', a1='w_rook')

workingBoard = \
    dict(h8=' ', g8='b_knight', f8='b_bishop', e8='b_queen', d8='b_king', c8='b_bishop', b8='b_knight', a8='b_rook',
         h7='b_pawn', g7='b_pawn', f7='b_pawn', e7='b_pawn', d7='b_pawn', c7='b_pawn', b7='b_pawn', a7='b_pawn',
         h2='w_pawn', g2='w_pawn', f2='w_pawn', e2='w_pawn', d2='w_pawn', c2='w_pawn', b2='x_pawn', a2='w_pawn',
         h1='w_rook', x1='w_knight', f1='w_biszkopt', e1='w_queen', d1='w_king', c1='w_bishop', b1='w_knight',
         a1='w_rook')


def correctchessboard(board):
    def checkiifigurespresent(board):  # Checking, if there are only white and black figures on chessboard
        for place, figure in board.items():
            if ((figure[:1] == 'b') or (figure[:1] == 'w')) is False:
                print(f'Possible issue of figure in {place}. There is now: \'{figure}\'')
            break

    def checkcolumns(board):
        dictCount = {'count' + char: len([place for place in board if place[:1] == char]) for char in 'hgfedcba'}
        if sum(dictCount.values()) == 32:
            print('Yeah, we have 32 figures on board')
        else:
            for column, value in dictCount.items():
                if value != 4:
                    wrongColumn = {column: value for (column, value) in dictCount.items() if value != 4}
                    for k, v in wrongColumn.items():
                        print(
                            f'There are some problems with chessboard. Check column: {k[-1:]}; It has {v} figure(s) instead of 4.')

    checkcolumns(board)
    checkiifigurespresent(board)


def correctfigurescolor(board):
    countW = 0
    countB = 0
    for location, figures in list(board.items()):
        if figures[:1] == 'b':
            countB += 1
        elif figures[:1] == 'w':
            countW += 1
        else:
            return f'There are figures in unknown colour on board, in example: \'{figures}\' at {location}'
    if countW == countB == 16:
        return f'Number of black({countB}) and white({countW}) figures is {countB + countB}'
    else:
        return f'Number of black({countB}) and white({countW}) figures is {countB + countB}\
         when expected is 16 white and 16 black'


def correctPosiotion(board, refBoard):
    if board == refBoard:
        print('Figures on chessboard are set in correct way!')
    else:
        boardSet = set(board.items())
        refBoardSet = set(refBoard.items())
        print(f'Figures on chessboard are NOT set in correct way!')
        wrongPosition = list(boardSet - refBoardSet)
        for position, figure in wrongPosition:
            if position in refBoard.keys():
                print(f'There is \'{figure}\' at {position} when expected is {refBoard[position]}')
            else:
                print(f'There is \'{figure}\' at strange position:{position} ')


def correctFigures(board, refBoard):
    if board.values() == refBoard.values():
        return ('All figures exist as expected')
    else:
        wrongFigures = set(board.values()) - set(refBoard.values())
        print("Problem with figures:", *list(wrongFigures), sep=',')


print(correctchessboard(workingBoard))
print('# # # # #')
print(correctfigurescolor(workingBoard))
print('# # # # #')
print(correctPosiotion(workingBoard, perfectBoard))
print('# # # # #')
print(correctFigures(workingBoard, perfectBoard))
