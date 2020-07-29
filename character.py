class Character():

    # Create a character
    def __init__(self, char_name):
        self._name = char_name.lower().strip()
        self.conversation = None
        self._health = 100

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        self._health = health

    @property
    def name(self):
        """Getter for name attribute"""
        return self._name

    @name.setter
    def name(self, new_name):
        """Setter for name attribute"""
        self._name = new_name

    # Describe this character
    def describe(self):
        print(self._name + " is here!")

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self._name + " says]: " + self.conversation)
        else:
            print(self._name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, enemy, damage_dealt):
        print(f"\n{self._name.upper()} has dealt {damage_dealt} damage to {enemy.name.upper()}\n")
        enemy.health -= damage_dealt


# Enemy class inherited from Character class
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name)
        self.health = 50
        self._description = char_description
        self._damage = 15

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage

    def describe(self):
        """Use to describe an enemy, overridden from parent class"""
        print(f", {self._name} ", end="")


class Hero(Character):
    def __init__(self, name):
        super().__init__(name)
        self._backpack = []
        self.health = 100


    @property
    def backpack(self):
        return self._backpack

    @backpack.setter
    def backpack(self, new_backpack):
        self._backpack = new_backpack

    def backpack_listing(self):
        '''
        List all the items inside backpack
        :return: none
        '''
        print("My backpack: ", end=" ")
        for item in self._backpack:
            if self.backpack.index(item) == 0:
                print(f"{item.name} ", end=" ")
            else:
                print(f",{item.name} ", end=" ")
        print()

    def backpack_insert(self, item):
        '''
        Insert an item into backpack
        :param item: item to insert (string)
        :return: none
        '''
        self._backpack.append(item)


    def backpack_remove(self,item):
        """
        Remove an item from backpack
        :param item: item to remove
        :return: none
        """
        self._backpack.remove(item)

    def backpack_item(self, item_want):
        """
        Get the item from backpack
        :param item_want: item want to retrieve
        :return: that item
        """
        for item in self.backpack:
            if item.name.lower().strip() == item_want.lower().strip():
                return item
        else:
            return False