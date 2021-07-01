import random
import time
import math


class Timer(object):
    counter = 0


class Fighter(object):  # parent class
    counter = 0
    hp = 100
    maxhp = 100
    name = ''
    ap = 1
    armor = 10

    def __init__(self, hp, name, ap=1, armor=10, count=None):
        self.hp = hp
        self.maxhp = hp
        self.name = name
        self.ap = ap
        self.armor = armor
        self.count = count

    def attack(self, damage):
        damage = damage - ((damage * self.armor) // 100)
        self.hp = self.hp - damage

    def get_ap(self):
        return self.ap

    def __repr__(self):
        # print(self.__class__.mro())
        return self.get_name() + ': ' + str(self.get_hp())

    def is_fullhp(self):
        # if self.hp == self.maxhp:#можно так
        #   return True
        # else:
        #   return False
        return self.hp == self.maxhp  # а можно так


class Getters():
    def get_hp(self):
        return self.hp

    def get_armor(self):
        return self.armor

    def get_name(self):
        return self.name


class Nameforpriest():
    def __repr__(self):
        return 'HEALER ' + self.get_name() + ': ' + str(self.get_hp())


class Warrior(Fighter, Getters):
    def get_ap(self):
        return int(self.ap * random.random())


class Champion(Fighter, Getters):
    def get_ap(self):
        if random.random() > 0.25:
            return self.ap
        else:
            print(self.name, ' champion have critical attack')
            return self.ap * 2


class Captain(Fighter, Getters):

    def attack(self, damage):
        a = input(f'what {self.name}  should  do? if 1 then shield for 10 turns, damage :{damage}')
        if a == '1':
            self.counter = self.count.counter
            return
        if damage > 30:
            super().attack(damage)

    def get_ap(self):
        if self.count.counter <= self.counter + 10:
            return 0
        else:
            return super().get_ap()


class Healer(Nameforpriest, Fighter, Getters):
    mana = 100
    maxmana = 100

    def heal(self, items):
        currentcounter = self.count.counter
        sec = currentcounter - self.counter
        manareg = sec * 2
        self.mana += manareg
        if self.mana > self.maxmana:
            self.mana = self.maxmana
        target = items[0]
        for i in items:
            if i.get_hp() < target.get_hp() and not target.is_fullhp():
                target = i
        print('healer status ', target.is_fullhp(), self.mana)
        if not target.is_fullhp() and self.mana >= 20:

            hp = target.get_hp() + 30
            self.mana -= 20
            if hp > target.maxhp:
                hp = target.maxhp
            target.hp = hp
            print('HEALER ', self.name, ' target: ', target.name, ' new hp: ', target.hp)
            self.counter = self.count.counter


count = Timer()

orcs = []

humans = []

for i in range(15):
    orc = Warrior(120, 'orc barbarian' + str(i), ap=50, armor=0, count=count)
    orcs.append(orc)
orcchampion = Champion(160, "orgrim champion" + str(i), ap=80, armor=0, count=count)
orcs.append(orcchampion)
orcchampion = Champion(160, "zak-zak champion" + str(i), ap=80, armor=0, count=count)
orcs.append(orcchampion)
orcchampion = Champion(160, "samuro champion" + str(i), ap=85, armor=0, count=count)
orcs.append(orcchampion)
orchero = Captain(480, "rexxar hero" + str(i), ap=200, armor=10, count=count)
orcs.append(orchero)
orchealer = Healer(100, "druid healer", ap=0, armor=50, count=count)
orcs.append(orchealer)
orchealer = Healer(100, "druid healer", ap=0, armor=50, count=count)
orcs.append(orchealer)

for i in range(10):
    human = Warrior(100, 'human soldier' + str(i), ap=40, armor=20, count=count)
    humans.append(human)
humanchampion = Champion(160, "varian champion" + str(i), ap=75, armor=30, count=count)
humans.append(humanchampion)
humanchampion = Champion(160, "anduin champion" + str(i), ap=75, armor=25, count=count)
humans.append(humanchampion)
humanchampion = Champion(160, "sedogriv champion" + str(i), ap=90, armor=0, count=count)
humans.append(humanchampion)
humanhero = Captain(400, "lotar hero" + str(i), ap=160, armor=40, count=count)
humans.append(humanhero)
humanhealer = Healer(100, "priest healer", ap=0, armor=50, count=count)
humans.append(humanhealer)
humanhealer = Healer(100, "priest healer", ap=0, armor=50, count=count)
humans.append(humanhealer)

print(orcs)
print(humans)
while orcs and humans:
    count.counter += 1
    time.sleep(1)
    if random.random() > 0.5:
        # unit2.attack(20)
        # print('unit1 attacks unit2')
        # print('unit2 have', unit2.get_hp())
        attackers = orcs
        victims = humans
    else:
        # unit1.attack(20)
        # print('unit2 attacks unit1')
        # print('unit1 have', unit1.get_hp())
        attackers = humans
        victims = orcs
    attacker = random.choice(attackers)
    victim = random.choice(victims)
    if type(attacker) is Healer:
        attacker.heal(attackers)
    else:
        ap = attacker.get_ap()
        victim.attack(ap)
        print('unit ', attacker.get_name(), ' attacks ', victim.get_name(), ' via ap ', ap, ' victim hp = ',
              victim.get_hp())
        if victim.get_hp() <= 0:
            print(victim.get_name(), ' have died')
            victims.remove(victim)

print(orcs)
print(humans)

# if unit1.get_hp() > 0:
# print('unit1 win,he have ',unit1.get_hp())
# else:
# print ('unit2 win,he have ',unit2.get_hp())

