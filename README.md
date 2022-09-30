# orion.py
roblox orion ui lib, but python 

## tutorial
1. import library and initialize
```py
from orionlib import Orion

generator = Orion("original")
```
2.  create the script
```py
generator.Create("./", "script_test")
```
3. make a window
```py
generator.MakeWindow(name="Test GUI", HidePremium=False, SaveConfig=True, ConfigFolder="OrionTest")
```
