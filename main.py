import os

from infi.systray import SysTrayIcon
import yaml

# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

config = 0

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def hello(sysTrayIcon):
    print ("Hello World.")

def simon(sysTrayIcon):
    print ("Hello Simon.")


def bye(sysTrayIcon):
    print ('Bye, then.')

def do_nothing(sysTrayIcon):
    pass

def run_commande(cmd):
    print(cmd)
    os.system(cmd)

def demarrage_systray():
    icon=''
    hover_text='message'
    hover_text = "SysTrayIcon Demo"
    config = yaml.safe_load(open("exemple1.yml"))
    print("config", config);
    menu_options = (('Say Hello', "hello.ico", hello),
                    ('Do nothing', None, do_nothing),
                    ('A sub-menu', "submenu.ico", (('Say Hello to Simon', "simon.ico", simon),
                                                   ('Do nothing', None, do_nothing),
                                                   ))
                    )
    print('menu_options', menu_options)

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
        #menu_options.append(())

    print('menu_options2', menu_options)

    menu_options=tuple(menu_options)
    print('menu_options3', menu_options)

    with SysTrayIcon(icon, hover_text, menu_options) as systray:
        for item in ['item1', 'item2', 'item3']:
            systray.update(hover_text=item)
            print('Hello', item)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    demarrage_systray()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
