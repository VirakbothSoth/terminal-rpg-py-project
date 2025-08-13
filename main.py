from func import *
import data
from data import usr

clear()
play_intro()

while True:
    term = usr.term.format(usr.name, usr.host).replace(">", str(usr.pts))
    cmd = str(input(term))
    scan_cmd(cmd)