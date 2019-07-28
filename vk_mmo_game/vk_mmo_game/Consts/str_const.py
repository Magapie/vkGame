from enum import Enum
from vk import Emoji


str_end = ": " #comment!
quote = '"' #comment!


class Words: #words for messages to players
    lvl = "Уровень"
    exp = "Опыт"
    gold = "Золото"
    health = "Здоровье"
    attack = "Атака"
    guild_name = "[Имя гильдии]"


class Strs: #building strings for messages to players
    lvl = Emoji.lightning + Words.lvl + str_end
    exp = Emoji.fire + Words.exp + str_end
    gold = Emoji.gold + Words.gold + str_end
    health = Emoji.heart + Words.health + str_end
    attack = Emoji.dagger + Words.attack + str_end


level_exp = [5, 10, 20, 40, 9999] # список из количества опыта для каждого уровня


class NameCase: #падежи для вк (cases, for vk only for now)
    nom = "nom" #именительный
    gen = "gen" #родительный
    dat = "dat" #дательный
    acc = "acc" #винительный
    ins = "ins" #творительный
    abl = "abl" #предложный


frac_by_number = {1:"Сумрачный замок", 2:"Мятный замок", 3:"Пидорский замок"} #needed to change name + comments
fracs_quantity = len(frac_by_number)
number_by_frac = { }

users_tb = "users"


class Column: # колонка для бд
    def __init__(self, name, type, number):
        self.name = name
        self.type = type
        self.number = number


class DBTypes(): # types of sqlite3
    integer = "INTEGER"


class UsersColumns(Enum): # колонки пользователей
    id = Column("id", DBTypes.integer, 0)
    #gold = Column("gold", DBTypes.integer, 0) 
    exp = Column("exp", DBTypes.integer, 0)
    lvl =  Column("lvl", DBTypes.integer, 0)
    countryid = Column("countryid", DBTypes.integer, 0)
    winscounter = Column("winscounter", DBTypes.integer, 0)
    state = Column("state", DBTypes.integer, 0)
    #attack = Column("attack", DBTypes.integer, 0)
    #health = Column("health", DBTypes.integer, 0)
    quest_end = Column("quest_end", DBTypes.integer, 0)


def _fill_colomn_numbers(column_name): # заполнение номеров колонок
    n = 0
    for colums in column_name:
        colums.value.number = n
        n += 1

_fill_colomn_numbers(UsersColumns)


class Buttons():
    stats = "hero"
    quest = "exp +1"
    top = "Статистика"
    duel = "Дуэль"


class Messages():
    ok = 'Ok' #need comments here!!!
    admin_func = 'Функционал для админов'
    select_frac = 'Выберите фракцию'
    you_faction = "Вами выбрана фракция: "
    win = "Победа"
    lose = "Поражение"
    fight_yourself = "Нельзя драться с собой"
    wins = "Побед: "
    in_duel_with = "в сражении с"
    with_link = "по"
    finish_quest = "Квест окончен"
    you_in_duel = "Вы находитесь в дуэли,"
    you_in_quest = "Вы находитесь в квесте,"
    act_unnable = "действие недоступно"
    un_duel = you_in_duel + ' ' + act_unnable
    un_quest = you_in_quest + ' ' + act_unnable
    wrong_text = "Неизвестная команда"


plus = " + 1"


def set_fracs_list():
    for i in range(1, fracs_quantity + 1):
        number_by_frac[frac_by_number[i]] = i
