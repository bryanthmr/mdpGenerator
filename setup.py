from cx_Freeze import setup, Executable
base = None
#Remplacer "monprogramme.py" par le nom du script qui lance votre programme
executables = [Executable("motdepasse.py", base=base)]
#Renseignez ici la liste complète des packages utilisés par votre application
packages = ["random","tkinter"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
#Adaptez les valeurs des variables "name", "version", "description" à votre programme.
setup(
    name = "GenMdp",
    options = options,
    version = "1.5",
    description = 'Programme permettant de générer des mots de passe sécurisés',
    executables = executables
)
