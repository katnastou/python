from termcolor import cprint
from pyfiglet import Figlet
msg = input("what message do you want to print? ")
col = input("what color?")

allowed_colors =["magenta","blue","green","yellow","red","cyan", "white"]
if col in allowed_colors:
    f = Figlet(font='starwars')
    cprint(f.renderText(msg), col)
else:
    f = Figlet(font='starwars')
    cprint(f.renderText(msg), "magenta")