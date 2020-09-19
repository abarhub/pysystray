# pysystray

Programme en python pour executer des commandes avec le system tray.
Le programme est en Python 3 et il fonctionne sous windows 10.

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
