# cURL commands

## init

### Request

```sh
curl -X GET -H 'Authorization: Token b84b4bca57fd4281c66e58d085e812be51cb389b' https://lambda-treasure-hunt.herokuapp.com/api/adv/init/
```

### Response

```sh
{"room_id": 0, "title": "A Dark Room", "description": "You cannot see anything.", "coordinates": "(60,60)", "exits": ["n", "s", "e", "w"], "cooldown": 1.0, "errors": [], "messages": []}
```

## move

### Request

```sh
curl -X POST -H 'Authorization: Token b84b4bca57fd4281c66e58d085e812be51cb389b' -H "Content-Type: application/json" -d '{"direction":"n"}' https://lambda-treasure-hunt.herokuapp.com/api/adv/move/
```

### Response

```sh
{"room_id": 10, "title": "A Dark Room", "description": "You cannot see anything.", "coordinates": "(60,61)", "exits": ["n", "s", "w"], "cooldown": 100.0, "errors": [], "messages": ["You have walked north."]}
```

Making a request before the cooldown period will incur a penalty

```sh
{"cooldown": 86.606674, "errors": ["Cooldown Violation: +5s CD"]}
```

## status/inventory

### Request

```sh
curl -X POST -H 'Authorization: Token b84b4bca57fd4281c66e58d085e812be51cb389b' -H "Content-Type: application/json" https://lambda-treasure-hunt.herokuapp.com/api/adv/status/
```

### Response

```sh
{"name": "player361", "cooldown": 1.0, "encumbrance": 0, "strength": 10, "speed": 10, "gold": 0, "bodywear": null, "footwear": null, "inventory": [], "status": [], "has_mined": false, "errors": [], "messages": []}
```
