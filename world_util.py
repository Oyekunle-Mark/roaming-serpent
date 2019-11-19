import random
import math

class Room:
    def __init__(self, name, description, id=0, x=None, y=None):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.getExitsString()}\n"

    def printRoomDescription(self, player):
        print(str(self))

    def getExits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits

    def getExitsString(self):
        return f"Exits: [{', '.join(self.getExits())}]"

    def connectRooms(self, direction, connectingRoom):
        if direction == "n":
            self.n_to = connectingRoom
            connectingRoom.s_to = self
        elif direction == "s":
            self.s_to = connectingRoom
            connectingRoom.n_to = self
        elif direction == "e":
            self.e_to = connectingRoom
            connectingRoom.w_to = self
        elif direction == "w":
            self.w_to = connectingRoom
            connectingRoom.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None

    def getRoomInDirection(self, direction):
        if direction == "n":
            return self.n_to
        elif direction == "s":
            return self.s_to
        elif direction == "e":
            return self.e_to
        elif direction == "w":
            return self.w_to
        else:
            return None

    def getCoords(self):
        return [self.x, self.y]



class World:
    def __init__(self):
        self.startingRoom = None
        self.rooms = {}
        self.roomGrid = []
        self.gridSize = 0

    def loadGraph(self, roomGraph):
        numRooms = len(roomGraph)
        rooms = [None] * numRooms
        gridSize = 1
        for i in range(0, numRooms):
            x = roomGraph[i][0][0]
            gridSize = max(gridSize, roomGraph[i][0][0], roomGraph[i][0][1])
            self.rooms[i] = Room(
                f"Room {i}", f"({roomGraph[i][0][0]},{roomGraph[i][0][1]})", i, roomGraph[i][0][0], roomGraph[i][0][1])
        self.roomGrid = []
        gridSize += 1
        self.gridSize = gridSize
        for i in range(0, gridSize):
            self.roomGrid.append([None] * gridSize)
        for roomID in roomGraph:
            room = self.rooms[roomID]
            self.roomGrid[room.x][room.y] = room
            if 'n' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms(
                    'n', self.rooms[roomGraph[roomID][1]['n']])
            if 's' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms(
                    's', self.rooms[roomGraph[roomID][1]['s']])
            if 'e' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms(
                    'e', self.rooms[roomGraph[roomID][1]['e']])
            if 'w' in roomGraph[roomID][1]:
                self.rooms[roomID].connectRooms(
                    'w', self.rooms[roomGraph[roomID][1]['w']])
        self.startingRoom = self.rooms[0]

    def printRooms(self):
        rotatedRoomGrid = []
        for i in range(0, len(self.roomGrid)):
            rotatedRoomGrid.append([None] * len(self.roomGrid))
        for i in range(len(self.roomGrid)):
            for j in range(len(self.roomGrid[0])):
                rotatedRoomGrid[len(self.roomGrid[0]) -
                                j - 1][i] = self.roomGrid[i][j]
        f = open("map.txt", "w")
        f.write("#####")
        print("#####")
        str = ""
        for row in rotatedRoomGrid:
            allNull = True
            for room in row:
                if room is not None:
                    allNull = False
                    break
            if allNull:
                continue
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
        f.write(str)
        f.write("#####")
        f.close()
        print(str)
        print("#####")
