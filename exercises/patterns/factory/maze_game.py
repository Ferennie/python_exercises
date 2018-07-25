# borrowed from http://pythoninthepink.blogspot.com/

from exercises.patterns.factory.maze import Maze
from exercises.patterns.factory.direction import Direction
from exercises.patterns.factory.room import Room
from exercises.patterns.factory.door import Door
from exercises.patterns.factory.wall import Wall
from exercises.patterns.factory.player import Player
from exercises.patterns.factory.wizard import Wizard
from exercises.patterns.factory.enchanted_room import EnchantedRoom
from exercises.patterns.factory.enchanted_door import EnchantedDoor
from exercises.patterns.factory.maze_factory import MazeFactory
from exercises.patterns.factory.enchanted_maze_factory import EnchantedMazeFactory


def create_maze(factory):
    maze = factory.make_maze()
    room1 = factory.make_room(1)
    room2 = factory.make_room(2)
    thedoor = factory.make_door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, factory.make_wall())
    room1.set_side(Direction.EAST, thedoor)
    room1.set_side(Direction.SOUTH, factory.make_wall())
    room1.set_side(Direction.WEST, factory.make_wall())

    room2.set_side(Direction.NORTH, factory.make_wall())
    room2.set_side(Direction.EAST, thedoor)
    room2.set_side(Direction.SOUTH, factory.make_wall())
    room2.set_side(Direction.WEST, factory.make_wall())

    return maze


def create_enchanted_maze():
    """Series of operations which create our Maze."""
    """Series of operations which create our Maze."""
    maze = Maze()
    room1 = EnchantedRoom(1, 'Alohomora!')
    room2 = EnchantedRoom(2, 'Alohomora!')
    themagicdoor = EnchantedDoor(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, Wall())
    room1.set_side(Direction.EAST, Wall())
    room1.set_side(Direction.SOUTH, themagicdoor)
    room1.set_side(Direction.WEST, Wall())

    room2.set_side(Direction.NORTH, Wall())
    room2.set_side(Direction.EAST, Wall())
    room2.set_side(Direction.SOUTH, themagicdoor)
    room2.set_side(Direction.WEST, Wall())

    return maze


# these are the ones we care the most about!
def create_factory_maze_type_a(factory):
    """Series of operations which create our Maze."""

    maze = factory.make_maze()
    room1 = factory.make_room(1)
    room2 = factory.make_room(2)
    thedoor = factory.make_door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, factory.make_wall())
    room1.set_side(Direction.EAST, thedoor)
    room1.set_side(Direction.SOUTH, factory.make_wall())
    room1.set_side(Direction.WEST, factory.make_wall())

    room2.set_side(Direction.NORTH, factory.make_wall())
    room2.set_side(Direction.EAST, thedoor)
    room2.set_side(Direction.SOUTH, factory.make_wall())
    room2.set_side(Direction.WEST, factory.make_wall())

    return maze


def create_factory_maze_type_b(factory):
    """Series of operations which create our Maze."""

    maze = factory.make_maze()
    room1 = factory.make_room(1)
    room2 = factory.make_room(2)
    thedoor = factory.make_door(room1, room2)

    maze.add_room(room1)
    maze.add_room(room2)

    room1.set_side(Direction.NORTH, factory.make_wall())
    room1.set_side(Direction.EAST, factory.make_wall())
    room1.set_side(Direction.SOUTH, thedoor)
    room1.set_side(Direction.WEST, factory.make_wall())

    room2.set_side(Direction.NORTH, factory.make_wall())
    room2.set_side(Direction.EAST, factory.make_wall())
    room2.set_side(Direction.SOUTH, thedoor)
    room2.set_side(Direction.WEST, factory.make_wall())

    return maze


if __name__ == "__main__":

    # tinker here?

    pass

