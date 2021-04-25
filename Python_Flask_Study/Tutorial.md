# How To Make a Web Application Using Flask in Python 3

<https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3>

## Launch virtual environment within Python after installing venv with pip : **pip install venv**

<https://docs.python.org/fr/3/library/venv.html>
**python3 -m venv /path/to/new/virtual/environment**
Lancer cette commande crée le dossier cible (en créant tous les dossiers parents qui n'existent pas déjà) et y ajoute un fichier pyenv.cfg contenant une variable home qui pointe sur l'installation Python depuis laquelle cette commande a été lancée (un nom habituel pour ce dossier cible est .venv). Cela crée également un sous-dossier bin (ou Scripts sous Windows) contenant une copie (ou un lien symbolique) du ou des binaires python (dépend de la plateforme et des paramètres donnés à la création de l'environnement). Elle crée aussi un sous-dossier (initialement vide) lib/pythonX.Y/site-packages (Sous Windows, c'est Lib\site-packages). Si un dossier existant est spécifié, il sera réutilisé.
Une fois qu'un environnement virtuel est créé, il peut être "activé" en utilisant un script dans le dossier binaire de l'environnement virtuel. L'invocation de ce script est spécifique à chaque plateforme **({venv} doit être remplacé par le chemin d'accès du répertoire contenant l'environnement virtuel)** :

|Plateforme|Invite de commande|Commande pour activer l'environnement virtuel|
|---------------------------------------------------------------------------|
|POSIX     |bash/zsh          |$ source {venv}/bin/activate                 |
|          |fish              |$ source {venv}/bin/activate.fish            |
|          |csh/tcsh          |$ source {venv}/bin/activate.csh             |
|          |PowerShell Core   |$ {venv}/bin/Activate.ps1                    |
|---------------------------------------------------------------------------|
|Windows   |cmd.exe           |C:\\{venv}\\Scripts\\activate.bat            |
|          |PowerShell        |**PS C:\\> {venv}\\Scripts\\Activate.ps1**   |
pour désactiver lancer **deactivate** sur la ligne de commande

## Launch Flask

how to launch the web aeg on local computer:
after installing flask with pip : pip install flask
go to your folder with app.py file (kind of main page)
then launch this :  **python3 -m flask run**
