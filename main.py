import os
from infi.systray import SysTrayIcon
import yaml

config = 0

def run_commande(cmd):
    print(cmd)
    os.system(cmd)

def demarrage_systray():
    icon=''
    hover_text = "PySystray"
    config = yaml.safe_load(open("config.yml"))
    print("config", config)

    menu_options=[]
    for item in config.get('commandes'):
        print(item)
        print(item.items())
        for k, v in item.items():
            print(k, v)
            descr=v.get('description')
            cmd=v.get('execution')
            print(descr, '->', cmd)
            func = lambda x, cmd=cmd : run_commande(cmd)
            menu_options.append((descr, None, func))

    print('menu_options2', menu_options)

    menu_options=tuple(menu_options)
    print('menu_options3', menu_options)

    with SysTrayIcon(icon, hover_text, menu_options) as systray:
        for item in ['item1', 'item2', 'item3']:
            systray.update(hover_text=item)
            print('Hello', item)

    print('fin du programme')



if __name__ == '__main__':
    demarrage_systray()

