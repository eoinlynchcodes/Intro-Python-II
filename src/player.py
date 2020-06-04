# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:

    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"{self.name}\t{self.current_room}"

    def move_player(self, newroom):
        self.current_room = newroom
        
