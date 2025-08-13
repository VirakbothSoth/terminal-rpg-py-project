import os, time, random as r
from data import usr, shop, iptarget, guess_nmap
import data

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def play_intro():
    print("Setting Terminal..."); time.sleep(0.5)

    for _ in range(15):
        print(f"Setting up \033[32m{r.choice(data.sys_file_name) + r.choice(data.sys_file_ex)}\033[0m")
        time.sleep(0.1)

    clear()
    print("Welcome to TerminalRPG!\nSay help to begin!")


def scan_cmd(prompt=""):
    parts = prompt.strip().split()

    if not parts:
        return

    cmd, *args = parts

    if cmd.lower() == "help":
        cmd_help()
    elif cmd.lower() == "save":
        usr.save()
    elif cmd.lower().startswith("load"):
        if args:
            usr.load(" ".join(args).strip())
    elif cmd.startswith("nameto"):
        usr.cmd_change("name", args[0])
    elif cmd.startswith("hostto"):
        usr.cmd_change("host", args[0])
    elif cmd in ["whoami", "info"]:
        usr.cmd_who()
    elif cmd == "get":
        cmd_get()
    elif cmd == "ls":
        usr.cmd_ls()
    elif cmd.startswith("shop"):
        if len(args) == 2 and args[0] == "buy":
            shop.buy_item(usr, args[1])
        else:
            shop.menu()
    elif cmd == "map":
        if usr.rank == "promini":
            cmd_map()
    elif cmd.startswith("nmap"):
        if args and usr.rank == "promini":
            cmd_nmap(args[0])
    else:
        if guess_nmap and cmd == guess_nmap[0] and args and args[0].isdigit():
            cmd_nmapguess(args[0])


def cmd_help():
    print("""
nameto <name>     - Change your name
hostto <host>     - Change your host
whoami/info       - Show info
get               - Earn points, and maybe get a file
ls                - List files you own
shop              - Open shop

map               - [PRO MINI NEEDED]
nmap <ip>         - [PRO MINI NEEDED]
""")


def cmd_get():
    for c in "⠁⠉⠋⠛⠟⠿":
        print(c, end="\r", flush=True)
        time.sleep(0.2)
    print(f"⠿ Collected {6 * usr.multi} Pts")
    usr.pts += 6 * usr.multi
    if r.randint(1,6) == 1:
        file = r.choice(data.file_name) + r.choice(data.file_ex)
        usr.files.append(file)
        print(f"You got a file named {file}!")


def cmd_map():
    while len(iptarget) < 5:
        iptarget.append(".".join(str(r.randint(0, 255)) for _ in range(4)))
    print(iptarget)


def cmd_nmap(ip):
    if ip not in iptarget: return print("Invalid target!")

    iptarget.remove(ip)
    service = r.choice(["ssh", "ftp", "redis"])
    port = r.randint(1000, 9999)
    guess_nmap[:] = [service, port]

    print(f"Starting Nmap 1.00 ( http://nmap.org ) at 2025-01-01 24:00 BST\n")
    print(f"""Nmap scan report for {ip}
Host is up (0.41s latency).
Not shown: Real IP Ports (reset)
PORT - STATE - SERVICE
{port} - OPEN - {service}

Command to claim: <service> <port>
Example: ssh 1234""")


def cmd_nmapguess(guess):
    if int(guess) in guess_nmap:
        print("You have hacked the user!\n⠿ Collected 10 Pts")
        usr.pts += 10