class Item():
    def __init__(self, name=None, damage=0):
        self._name = name
        self._description = None
        self._damage = damage

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, new_damage):
        self._damage = new_damage

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description


    def describe(self):
        print(f'Available item to pick up: {self.name}\n{self.description}')

    def __str__(self):
        return self.name