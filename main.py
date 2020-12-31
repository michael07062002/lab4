class Infected_yaharnamit:

    """
    Зараженный ярнамит умеет атаковать, также он получает урон от атак.
    Его здоровье равно 160. Он может наносить 20 единиц урона в секунду.
    Если его атакуют он получает 40 единиц урона за  секунду.
   """
    name = 'Зараженный ярнамит'
    time = 0
    def __init__(self):
        self.hp = 160
        self.damage = 20
        self.ultimate_damage = 0
        self.ultimate_hp = 0
        self.damage_recieved = 40

    def attack(self, t,damage=20 ):
        self.time = t
        self.ultimate_damage += damage*self.time
    def health (self, t, damage_recieved=40, hp=160 ):
        self.time = t
        if self.time <4:
            self.ultimate_hp = hp - damage_recieved*self.time
        else:
            self.ultimate_hp = 'мертв'
    def get_ultimate_damage(self):
        return self.ultimate_damage

    def get_ultimate_hp(self):
        return self.ultimate_hp

class Yaharnamit_with_shield(Infected_yaharnamit):
    """ Атакует факелом. Также щит защищает от половины урона"""""

    name = 'Зараженный ярнамит с щитом'
    def __init__(self):
        super().__init__()
        self.hp = 120
        self.damage_phys = 20
        self.damage_fire = 10
        self.ultimate_damage = 0
        self.ultimate_hp = 0
        self.damage_recieved = 40
        self.armour = 2
    def attack(self, t,damage_phys=20,damage_fire=10 ):
        self.time = t
        self.ultimate_damage += (damage_phys + damage_fire)*self.time
    def health (self, t, damage_recieved=40, hp=120, armour = 2 ):
        self.time = t
        if self.time <6:
            self.ultimate_hp = hp - damage_recieved*self.time/armour
        else:
            self.ultimate_hp = 'мертв'
class Hunter(Infected_yaharnamit):
    """ Если охотник теряет поливину здоровья, то он испоьзует пузыпек с кровью, который восстанавливает здоровье
    """
    name = 'Охотник'
    def __init__(self):
        super().__init__()
        self.hp = 520
        self.damage = 100
        self.ultimate_damage = 0
        self.ultimate_hp = 0
        self.damage_recieved = 40
        self.vial_of_blood = 3
    def attack(self, t,damage=100 ):
        self.time = t
        self.ultimate_damage += damage*self.time
    def health (self, t, damage_recieved=40, hp=520 ):
        for i in range(1, t+1):
            hp -= damage_recieved
            if (self.vial_of_blood > 0 and hp < 260) :
                hp += 100
                self.vial_of_blood -= 1
        if hp <= 0:
            self.ultimate_hp = 'мертв'
        else:
            self.ultimate_hp = hp
    def get_vial_of_blood(self):
        return self.vial_of_blood
class Hunter_of_Healing_church(Hunter):
    """Стреляет из пистолета раз в 3 секунды"""
    name = 'Охотник церкви Исцеления'

    def __init__(self):
        super().__init__()
        self.hp = 300
        self.damage_phys = 70
        self.damage_pistol = 50
        self.ultimate_damage = 0
        self.ultimate_hp = 0
        self.damage_recieved = 40
        self.vial_of_blood = 2
        self.ultimate_damage_pistol=0
        self.shot = 0
    def attack(self, t,damage_phys=70,damage_pistol=50 ):
        self.time = t
        self.shot = t//3
        self.ultimate_damage_pistol = damage_pistol*self.shot
        self.ultimate_damage += damage_phys*self.time + self.ultimate_damage_pistol
    def health (self, t, damage_recieved=40, hp=300 ):
        for i in range(1, t+1):
            hp -= damage_recieved
            if (self.vial_of_blood > 0 and hp < 150) :
                hp += 75
                self.vial_of_blood -= 1
        if hp <= 0:
            self.ultimate_hp = 'мертв'
        else:
            self.ultimate_hp = hp
    def get_damage_pistol(self):
        return self.shot
class Choir_hunter(Hunter_of_Healing_church):
    """Использует магию раз в 6 секунд"""
    name = 'Охотник Хора'
    def __init__(self):
        super().__init__()
        self.hp = 600
        self.damage_phys = 150
        self.damage_pistol = 60
        self.ultimate_damage = 0
        self.ultimate_hp = 0
        self.damage_recieved = 40
        self.vial_of_blood = 4
        self.ultimate_damage_pistol=0
        self.ultimate_damage_magic = 0
        self.shot = 0
        self.magic = 0
    def attack(self, t,damage_phys=70,damage_pistol=50, damage_magic = 200 ):
        self.time = t
        self.shot = t//3
        self.magic = t//6
        self.ultimate_damage_pistol = damage_pistol*self.shot
        self.ultimate_damage_magic = damage_magic*self.magic
        self.ultimate_damage += damage_phys*self.time + self.ultimate_damage_pistol +self.ultimate_damage_magic
    def health (self, t, damage_recieved=40, hp=600 ):
        for i in range(1, t+1):
            hp -= damage_recieved
            if (self.vial_of_blood > 0 and hp < 300) :
                hp += 125
                self.vial_of_blood -= 1
        if hp <= 0:
            self.ultimate_hp = 'мертв'
        else:
            self.ultimate_hp = hp
    def get_damage_magic(self):
        return self.magic
def show_full_information(input_obj):
    print('Информация о', input_obj.name, input_obj.__dict__)
obj_infected_yaharnamit = Infected_yaharnamit()
obj_infected_yaharnamit.attack(1)
obj_infected_yaharnamit.health(4)
print('Зараженный ярнамит','Нанесенный урон:', obj_infected_yaharnamit.get_ultimate_damage(),'Показатель здоровья:',obj_infected_yaharnamit.get_ultimate_hp())
obj_yaharnamit_with_shield = Yaharnamit_with_shield()
obj_yaharnamit_with_shield.attack(4)
obj_yaharnamit_with_shield.health(3)
print('Зараженный ярнамит с щитом','Нанесенный урон:',obj_yaharnamit_with_shield.get_ultimate_damage(),'Показатель здоровья:',obj_yaharnamit_with_shield.get_ultimate_hp())
obj_hunter = Hunter()
obj_hunter.attack(5)
obj_hunter.health(10)
print('Охотник','Нанесенный урон:',obj_hunter.get_ultimate_damage(),'Показатель здоровья:', obj_hunter.get_ultimate_hp(),'Оставшиеся пузырьки с кровью:',obj_hunter.get_vial_of_blood())
obj_hunter_of_Healing_church = Hunter_of_Healing_church()
obj_hunter_of_Healing_church.attack(2)
obj_hunter_of_Healing_church.health(5)
print('Охотник церкви Исцеления','Нанесенный урон:',obj_hunter_of_Healing_church.get_ultimate_damage(),'Показатель здоровья:',obj_hunter_of_Healing_church.get_ultimate_hp(),'Оставшиеся пузырьки с кровью:',obj_hunter_of_Healing_church.get_vial_of_blood(),'Выстрелы из пистолета:',obj_hunter_of_Healing_church.get_damage_pistol() )
obj_choir_hunter = Choir_hunter()
obj_choir_hunter.attack(6)
obj_choir_hunter.health(5)
print('Охотник Хора','Нанесенный урон:',obj_choir_hunter.get_ultimate_damage(),'Показатель здоровья:',obj_choir_hunter.get_ultimate_hp(),'Оставшиеся пузырьки с кровью:',obj_choir_hunter.get_vial_of_blood(),'Выстрелы из пистолета:',obj_choir_hunter.get_damage_pistol(),'Использование магии:',obj_choir_hunter.get_damage_magic())
show_full_information(obj_infected_yaharnamit)
show_full_information(obj_yaharnamit_with_shield)
show_full_information(obj_hunter)
show_full_information(obj_hunter_of_Healing_church)
show_full_information(obj_choir_hunter)