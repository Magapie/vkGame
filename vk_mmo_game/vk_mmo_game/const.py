
admins = 1, 385124486
db_name = "Users.db"

class State():
    normal = '1'
    forest = '2'

class PlayersFields():
    id = 0
    gold = 1
    exp = 2
    lvl = 3
    countryId = 4
    winscounter = 5
    state = 6
    attack = 7
    health = 8
    quest_end = 9



class LvlsFields():
    lvl = 0
    exp = 1

wait = 10



class Begin():
    country = '0'
    gold = '0'
    exp = '0'
    lvl = '1'
    win = '0'
    attack = '1'
    health = '10'
    state = State.normal
    quest_end = 'NULL'