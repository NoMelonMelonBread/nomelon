# nomelon
# rock,scissors, paper game!!! Yeah!!!
def Game(player1, player2) :
    if str(player1) == '가위' :
        if str(player2) == '바위' : print("player2")
        elif str(player2) == '보' : print("player1")
        else : Game(player1, player2)
    if str(player1) == '바위' :
        if str(player2) == '가위' : print("player1")
        elif str(player2) == '보' : print("player2")
        else : Game(player1, player2)
    if str(player1) == '보' :
        if str(player2) == '가위' : print("player2")
        elif str(player2) == '바위' : print("player1")
        else : Game(player1, player2)
