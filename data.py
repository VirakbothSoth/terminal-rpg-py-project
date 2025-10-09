import json
import base64

class User:
    def __init__(self, pts=0, name="usr", host="host", rank="basic", multi=1, files=[], term="{}@{}:~$ "):
        self.pts = pts

        self.name = name
        self.host = host

        self.rank = rank
        self.multi = multi
        self.files = files
        self.term = term

    def cmd_who(self):
        print(f"""
        {self.name}\\{self.host}
        Rank: {self.rank}
        Pts: {self.pts}
            """)
        
    def cmd_change(self, mode, to):
        if 0 < len(to) < 10:
            if mode == "name":
                self.name = to
            if mode == "host":
                self.host = to

    def cmd_ls(self):
        for i in self.files:
            print(i, end=" ")
        print()

    def save(self):
        data = {
            "pts": self.pts,
            "name": self.name,
            "host": self.host,
            "rank": self.rank,
            "multi": self.multi,
            "files": self.files,
            "term": self.term
        }
        json_str = json.dumps(data)
        encoded_data = base64.b64encode(json_str.encode()).decode()
        print(encoded_data)

    def load(self, encoded_str):
        try:
            encoded_str = encoded_str.strip().replace("\n", "")
            json_str = base64.b64decode(encoded_str).decode()
            obj = json.loads(json_str)

            self.pts = obj.get("pts", 0)
            self.name = obj.get("name", "usr")
            self.host = obj.get("host", "host")
            self.rank = obj.get("rank", "basic")
            self.multi = obj.get("multi", 1)
            self.files = obj.get("files", [])
            self.term = obj.get("term", "{}@{}:~$ ")

            print("Loaded!")
        except Exception as e:
            print(f"Invalid data! ({e})")



usr = User()

class Shop:
    def __init__(self):
        self.item = {
            "rank_pro_mini": 24
        }

        self.ranks = {
            "basic": 0,
            "pro_mini": 1,
            "pro": 2,
        }

    def menu(self):
        print("\nShop:")
        for name, price in self.item.items():
            print(f"• {name} - {price} pts")
        print("Say 'shop buy <item>' to buy\n")

    def buy_item(self, usr, pick):
        if pick not in self.item:
            print("Error: Item Not Found")
            return

        price = self.item[pick]

        if usr.pts >= price:
            usr.pts -= price

            print(f"\nBought {pick} for {price}!")
            if pick.startswith("rank_"):
                usr.rank = "promini"
                usr.term = "┌──({}㉿{})-[~]-[>]\n└─$ "
                usr.multi = 2
                print(f"Thanks for buying {usr.rank}!")
                print("Perks: Kali Terminal, 2x Pts, New Commands: map, nmap\n")
        else:
            print("Error: Not Enough Pts")

shop = Shop()

guess_nmap = []
iptarget = []

# Random file formats for loading screen
sys_file_ex = (".bat", ".sys", ".env", ".sh", ".reg", ".map", ".dll", "", ".drv", ".dfg", ".sec", ".tmp", ".bin")

# Random file name for loading screen
sys_file_name = ("system", "operating", "terminal", "drivers", "regis", "variable", "protocol", "faketermin", "easteregg")

# Random file formats for "get" random files
file_ex = (".exe", ".txt", ".png", ".jpg", ".jpeg", ".svg", ".htm", ".xml", ".c", ".py", ".md")

# Random file name for "get" random files
file_name = ("game", "homework", "image", "notes", "web", "code", "test", "cool")