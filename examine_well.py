import requests
import time
from decouple import config
from goto import goto

TOKEN = config("TOKEN")

auth = {"Authorization": "Token " + TOKEN}


def get_current_room():
    res = requests.get(
        "https://lambda-treasure-hunt.herokuapp.com/api/adv/init/",
        headers=auth
    )
    res_json = res.json()
    time.sleep(res_json["cooldown"])
    return res_json["room_id"]


def examine():
    res = requests.post(
        "https://lambda-treasure-hunt.herokuapp.com/api/adv/examine/",
        headers=auth,
        json={"name": "well"}
    )

    res_json = res.json()
    time.sleep(res_json["cooldown"])

    return res.json()


if __name__ == "__main__":
    current_room = get_current_room()
    wishing_well_room = "55"

    goto(str(current_room), wishing_well_room)

    response = examine()

    with open("wishing_well_prophecy.txt", "w") as f:
        f.write(response["description"])

    print(response)
