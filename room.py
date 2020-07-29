"""
Room class is used to represent a room in my text based adventure game
"""


class Room():
    def __init__(self):
        self._name = None
        self._description = None
        self._linked_rooms = {}
        self._character = []
        self._item = None

    @property
    def name(self):
        """
        Getter for name attribute
        :return: room's name (string)
        """
        return self._name

    @name.setter
    def name(self, room_name):
        """
        Setter for name attribute
        :param room_name: new room's name
        :return: none
        """
        self._name = room_name

    @property
    def description(self):
        """
        Getter for room's description
        :return: room's description (string)
        """
        return self._description

    @description.setter
    def description(self, room_description):
        """
        Setter for room's description
        :param room_description: new room description (string)
        :return: none
        """
        self._description = room_description

    @property
    def character(self):
        """ Get the Current characters"""
        return self._character

    @character.setter
    def character(self, new_character):
        """Set the Characters"""
        self._character = new_character

    @property
    def item(self):
        """
        Get the item
        :return: none
        """
        return self._item

    @item.setter
    def item(self, new_item):
        '''
        Set item
        :param new_item: item to set
        :return: none
        '''
        self._item = new_item

    def character_listing(self):
        """
        Listing out all the character inside the room
        :return:
        """
        if self._character:
            print("Enemy: ", end=" ")
            for inhabitant in self.character:
                if self.character.index(inhabitant) == 0:
                    print(inhabitant.name, end=" ")
                else:
                    inhabitant.describe()
        print("\n")


    def remove_item(self):
        '''
        Remove an item from the room
        :return: none
        '''
        self._item = None

    def descibe(self):
        """
        Give a room description
        :return: none
        """
        print(self.description)

    def link_room(self, room_to_link, direction):
        """
        Link a room to another room
        :param room_to_link: name of the room to link ( Room object)
        :param direction: direction of the room to link (string)
        :return: none
        """
        self._linked_rooms[direction.lower()] = room_to_link

    def get_details(self):
        """
        Display the information of the room
        :return:
        """
        print(f"The {self._name}")
        print("-------------------------")
        print(self._description + "\n")
        for direction in self._linked_rooms.keys():
            room = self._linked_rooms[direction]
            print(f"The {room.name} is {direction}")
        print("\n")


    def move(self, direction):
        """
        Move from one room to another
        :param direction: direction to move
        :return: the room moved to
        """
        if direction in self._linked_rooms:
            return self._linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def describe_characters(self):
        """
        Listing out all the characters information
        :return: none
        """
        for char in self._character:
            char.describe()


    def get_specific_character(self, character_name):
        for char in self.character:
            if char.name == character_name:
                return char

    def has_enemy(self):
        """
        Check to if if there are enemy in the room
        :return: True if there's else none
        """
        if self._character:
            return True
        return False
