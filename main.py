import logging
import os
import sys

from infi.systray import SysTrayIcon
import yaml

config = 0


def run_commande(cmd):
    print(cmd)
    logging.info('execution de la commande: ' + cmd)
    os.system(cmd)


def demarrage_systray():
    logging.basicConfig(filename='log/pysystray.log', level=logging.INFO,
                        format='%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s')
    logging.info('demarrage du systray')
    icon = ''
    hover_text = "PySystray"
    nom_fichier_config = "config.yml"
    try:
        config = yaml.safe_load(open(nom_fichier_config))
    except FileNotFoundError:
        # le fichier n'existe pas
        print("Erreur: Impossible de trouver le fichier " + nom_fichier_config, file=sys.stderr)
        logging.info("Erreur: Impossible de trouver le fichier " + nom_fichier_config)
        raise
    print("config", config)
    logging.info('config', config)

    menu_options = []
    for item in config.get('commandes'):
        print(item)
        print(item.items())
        for k, v in item.items():
            print(k, v)
            descr = v.get('description')
            cmd = v.get('execution')
            print(descr, '->', cmd)
            func = lambda x, cmd=cmd: run_commande(cmd)
            menu_options.append((descr, None, func))

    print('menu_options2', menu_options)

    menu_options = tuple(menu_options)
    print('menu_options3', menu_options)

    with SysTrayIcon(icon, hover_text, menu_options) as systray:
        for item in ['item1', 'item2', 'item3']:
            systray.update(hover_text=item)
            print('Hello', item)

    print('fin du programme')
    logging.info('attente action du systray')


if __name__ == '__main__':
    demarrage_systray()
