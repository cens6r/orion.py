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
generator.MakeWindow(Name="Test GUI", HidePremium=False, SaveConfig=True, ConfigFolder="OrionTest")
```
4. make a tab
```py
generator.MakeTab(Name="Tab 1", Icon="rbxassetid://4483345998", PremiumOnly=False)
```
