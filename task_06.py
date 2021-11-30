'''Разработать методы для программы Камень-Ножницы-Бумага.
Метод rps_game_winner должен принимать на вход массив следующей структуры
[ ["player1", "P"], ["player2", "S"] ], где P - бумага, S - ножницы, R - камень, и
функционировать следующим образом:

• если количество игроков больше 2 необходимо вызывать исключение
WrongNumberOfPlayersError
• если ход игроков отличается от ‘R’, ‘P’ или ‘S’ необходимо вызывать
исключение NoSuchStrategyError
• в иных случаях необходимо вернуть имя и ход победителя, если оба
игрока походили одинаково - выигрывает первый игрок.

Тесты для примеров и проверки:
rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) #
=> WrongNumberOfPlayersError
rps_game_winner([['player1', 'P'], ['player2', 'A']]) #
=> NoSuchStrategyError
rps_game_winner([['player1', 'P'], ['player2', 'S']]) #
=> 'player2 S'
rps_game_winner([['player1', 'P'], ['player2', 'P']]) #
=>'player1 P'
'''


class Error(Exception):
    pass


class NoSuchStrategyError(Error):
    pass


class WrongNumberOfPlayersError(Error):
    pass

def check(a, b):
    tr = {'R': 'S', 'S': 'P', 'P': 'R'}
    try:
        if a not in tr or b not in tr:
            raise NoSuchStrategyError

        for i, j in tr.items():
            if a == b:
                return 'player1 ' + a
            if a == i and b == j:
                return ("player1 " + a)
            elif b == i and a == j:
                return ("player2 " + b)
    except NoSuchStrategyError:
        return("NoSuchStrategyError")


def rps_game_winner(stats):
    try:
        if len(stats) > 2:
            raise WrongNumberOfPlayersError
        return check(stats[0][1], stats[1][1])
    except WrongNumberOfPlayersError:
        return("WrongNumberOfPlayersError")

if __name__ == '__main__':
    print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
