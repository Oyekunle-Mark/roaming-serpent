# Handle file read/write

This code snippet helps with read/write operation from and to file

```py
# import the json module
import json

# presume there is chain_seed.py file in the same directory with the current file

# read from chain_seed file and set it as chain
with open("chain_seed.py", "r") as f:
    # f.read() returns a string, pass it to json.loads to convert it to python object
    self.chain = json.loads(f.read())

# write the chain to the chain_seed.py file
with open("chain_seed.py", "w") as f:
    # since f.write takes a string, convert the object to string with json.dumps
    f.write(json.dumps(self.chain))
```
