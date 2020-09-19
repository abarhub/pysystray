# pysystray

Programme en python pour executer des commandes avec le system tray.
Le programme est en Python 3 et il fonctionne sous windows 10.

# Installation

Pour installer le script, il faut executer les commandes suivantes :

```bat
cd c:\repertoire\installation
git clone https://github.com/abarhub/pysystray.git
cd pysystray
pip install -r requirements.txt
run.bat
```

Pour lancer le script, il faut executer :
```bat
run.bat
```
ou
```bat
python main.py
```

# Configuration

La liste des commandes doit être défini dans le fichier de configuration config.yml.

Exemple de fichier de configuration :

config.yml
```yaml
commandes:
  - commande1:
      description: Commande 1
      execution: dir
  - commande2:
      description: Commande 2
      execution: cmd /C test\run.bat
  - commande3:
      description: Commande 3
      execution: start test\run.bat
```
