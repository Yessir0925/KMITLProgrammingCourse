#from userdata import *
class Player:
    def __init__(self, Name, Level, HP, Weapon, Armor):
        self.Name = Name
        self.Level = Level
        self.HP = HP
        self.Weapon = Weapon
        self.Armor = Armor
    def move():
        pass
    
class Weapon:
    def __init__(self, Name, Damage):
        self.Name = Name
        self.Damage = Damage

class Armor:
    def __init__(self, Name, Defense):
        self.Name = Name
        self.Defense = Defense

class Guild:
    def __init__(self, Gamename):
        self.Gamename = Gamename
        self.PlayerList = []
    GuildLeader = None

Iron_Sword = Weapon('Iron Sword', 10)
Leather_Armor = Armor('Leather Armor', 5)
Player1 = Player('Hero_01', 1, 100, Iron_Sword, Leather_Armor)

Wooden_Bow = Weapon('Wooden Bow', 8)
Chain_Mail = Armor('Chain Mail', 10)
Player2 = Player('Archer_02', 2, 120, Wooden_Bow, Chain_Mail)

Guild1 = Guild('Guild1')
Guild1.PlayerList.append(Player1)
Guild1.PlayerList.append(Player2)
Guild1.GuildLeader = Player1

Counter = 1
for i in Guild1.PlayerList:
    print(f"=== Player {Counter} ===")
    print(f"Name: {i.Name}")
    print(f"HP: {i.HP}")
    print(f"Weapon: {i.Weapon.Name} (Damage: {i.Weapon.Damage})")
    print(f"Weapon: {i.Armor.Name} (Damage: {i.Armor.Defense})\n")
    Counter += 1

print(Guild1.GuildLeader.Name)