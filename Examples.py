# Import Library
import winreg

# Global variables
sub_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\\"
key = "Run"
path = sub_path + key

############### CREATE KEY ################
def createKey():
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # sub_path can be empty
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, path)

############### SET VALUE ################
def setValueEx():   # Only String and ExpandString
    # Example: Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    # Open key
    open_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path)    # Error if key is emply
    name_value = "Valor"
    value = "soy un valor"
    # Create value
    winreg.SetValueEx(open_key, value, 0, winreg.REG_EXPAND_SZ, name_value)


# Read Documentation:
# https://docs.python.org/3/library/winreg.html