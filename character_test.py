from room import Room
from item import Item
from character import Character, Enemy, Hero
from rpginfo import RPGInfo



hero = Hero("Hero")
enemy = Enemy("enemy","Example enemy")
item = Item("Sword",25)


print(hero.health)
print(enemy.health)

hero.fight(enemy,item.damage)
hero.fight(enemy,item.damage)
enemy.fight(hero,5)
print(hero.health)
print(enemy.health)