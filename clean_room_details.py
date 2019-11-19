import json

room_details = []

with open("room_details.py", "r") as f:
    # read the room details
    room_details = json.loads(f.read())

room_set = set()

# add the rooms to set to remove repetition
for room in room_details:
    room_set.add(room)

# write the result to the cleaned room_details file
with open("traverse_results/room_details.py", "w") as f:
    f.write(json.dumps(room_set))
