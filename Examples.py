# Create in Python 3.8.5
# Import Library
import winreg

# Global variables
from msilib.schema import File

sub_path = "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\"
key = "Run"
path = sub_path + key


def createKey(self):
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # sub_path can be empty
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, path)


############### SET VALUE EX ################
def setValueEx(self):
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # Open key
    opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)  # Error if key is emply
    name_value = "Valor"
    value = "soy un valor"
    # Create value
    winreg.SetValueEx(opened_key, name_value, 0, winreg.REG_EXPAND_SZ, value)


############### SET VALUE ################
def setValue(self):
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    name_value = "Valor"  # not use name value // (default)
    value = "soy un valor"
    # Create value
    winreg.SetValue(winreg.HKEY_CURRENT_USER, key, winreg.REG_SZ, value)


############### DELETE VALUE ################
def deleteValue(self):
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # Open key
    opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)  # Error if key is emply
    name_value = "Valor"
    # Create value
    winreg.DeleteValue(opened_key, name_value)


############### DELETE KEY ################
def deleteKey(self):
    # This method can not delete keys with subkeys.
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, path)


############### DELETE KEY  ################
def deleteKeyEx(self):
    # This method can not delete keys with subkeys.
    winreg.DeleteKeyEx(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)


class WinRegistry(path):
    def __init__(self):
        self.path = path
        pass
    def create_key(self):
        pass
    def delete_key(self):
        pass
    def read_value(self):
        pass
    def create_value(self):
        pass
    def delete_value(self):
        pass




"""
def saveKey():
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # Open key
    opened_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path, 0, winreg.KEY_ALL_ACCESS)  # Error if key is emply
    name_value = "Valor"
    # Create value
    file = open("file.txt", "w")  # Read file
    #winreg.LoadKey(opened_key, name_value, file)
    winreg.SaveKey(opened_key, file.name)
    """


# Read Documentation:
# https://docs.python.org/3/library/winreg.html