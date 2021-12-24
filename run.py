import os
import sys
import platform
import colorama as c
import tools.alliance as aa


c.init()

red = c.Fore.RED
grn = c.Fore.GREEN
blu = c.Fore.BLUE
res = c.Fore.RESET


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def cmd(txt):
    args = txt.split()
    if args[0] == "q":
        sys.exit()
    if args[0] == "am":
        print(am(*args[1:]))


def am(aa_id):
    data = aa.get_mil(aa_id, key)
    out = []
    for k, v in data.items():
        label = str(k).rjust(8)
        mils = " ".join([
            "".join(v)
        ])
        out.append(f"{blu}{label}{red}{mils}{res}")
    return "\n".join(out)


try:
    key = open("key.txt").read().strip()
except FileNotFoundError:
    print(f"{blu}key.txt{red} not found.{res} Consider storing your {blu}API key{res} in {blu}key.txt{res}.")
    key = input("API Key: ")

while True:
    clear()
    print(f"{grn}PnUtil{res}")
    print(f" {red}Commands{res}")
    print(f"  {blu}Alliance Militarization{res} (by member)")
    print(f"   {grn}>{res} am {blu}<Alliance ID>{res}")
    print(f"  {blu}Exit{res}")
    print(f"   {grn}>{res} q")
    print()

    inp = input(f"{grn}>{res} ")
    try:
        cmd(inp)
    except Exception as e:
        print(e)
        print(f"{red}An error happened.{res}")
    finally:
        input(f"Press {blu}enter{res} to continue...")
