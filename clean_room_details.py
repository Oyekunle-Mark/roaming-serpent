import json

# to hold the rooms
room_details = []

with open("room_details.py", "r") as f:
    # read the room details
    room_details = json.loads(f.read())

print("Length before cleaning is: ", len(room_details))

room_set = set()
cleaned_rooms = []

# add the rooms to set to remove repetition
for room in room_details:
    # check if the room id is not in the set
    if room["room_id"] not in room_set:
        # add the room_id
        room_set.add(room["room_id"])
        # add it to the cleaned_room list
        cleaned_rooms.append(room)

print("Length after cleaning is: ", len(cleaned_rooms))

# write the result to the cleaned room_details file
with open("traverse_results/room_details.py", "w") as f:
    f.write(json.dumps(cleaned_rooms))
