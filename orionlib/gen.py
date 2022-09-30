import os

def _getLoadstring(type):
    if type.lower() == "original":
        return "local OrionLib = loadstring(game:HttpGet(('https://raw.githubusercontent.com/shlexware/Orion/main/source')))()"
    elif type.lower() == "backup":
        return "local OrionLib = loadstring(game:HttpGet('https://raw.githubusercontent.com/cens6r/solaris-ui-lib/main/source.lua'))()"

class Generator:
    def __init__(self, loadsting: str):
        self.loadsting = _getLoadstring(loadsting)
        self.file = None

    def Create(self, directory, name):
        if os.path.exists(os.path.abspath(directory)):
            pass
        else:
            os.mkdir(os.path.abspath(directory))
        
        self.file = open(os.path.join(os.path.abspath, name+".lua"), "a")
        self.file.write(self.loadsting+"\n")

    
    def MakeWindow(self, Name, HidePremium=None, SaveConfig=None, ConfigFolder=None, IntroEnabled=None, IntroText=None, IntroIcon=None, Icon=None, CloseCallback=None):
        """
        Name = <string> - The name of the UI.\n
        HidePremium = <bool> - Whether or not the user details shows Premium status or not.\n
        SaveConfig = <bool> - Toggles the config saving in the UI.\n
        ConfigFolder = <string> - The name of the folder where the configs are saved.\n
        IntroEnabled = <bool> - Whether or not to show the intro animation.\n
        IntroText = <string> - Text to show in the intro animation.\n
        IntroIcon = <string> - URL to the image you want to use in the intro animation.\n
        Icon = <string> - URL to the image you want displayed on the window.\n
        CloseCallback = <function> - Function to execute when the window is closed.\n
        """
        if not self.file:
            print("You forgot to create the script!")
            return
        
        args = {Name: Name}
        if HidePremium:
            args[HidePremium] = str(HidePremium).lower()
        if SaveConfig:
            args[SaveConfig] = str(SaveConfig).lower()
        if ConfigFolder:
            args[ConfigFolder] = ConfigFolder
        if IntroEnabled:
            args[IntroEnabled] = str(IntroEnabled).lower()
        if IntroText:
            args[IntroText] = IntroText
        if IntroIcon:
            args[IntroIcon] = IntroIcon
        if Icon:
            args[Icon] = Icon
        if CloseCallback:
            args[CloseCallback] = CloseCallback

        luaArgs = str(args).replace(":", "=")
        finalPayload = f'local Window = OrionLib:MakeWindow({luaArgs})'

        self.file.write(finalPayload)+"\n"
