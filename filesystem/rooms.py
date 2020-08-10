# Room System.
import json, time, random

# Create Dungeon.
class Dungeon:
	room_array = []
	# Create Dungeon Map.
	def create_map(self):
		for x in range(0, 5):
			x.append([])
			for y in range (0, 5):
				self.room_array[x].append(Room())

	def print_map(self, room_with_player):


# Create Room.
class Room:
	# todo: implement

dung_ex = Dungeon()