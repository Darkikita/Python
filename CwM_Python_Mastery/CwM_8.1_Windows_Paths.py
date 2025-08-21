# Python Standard Library 
#   - Python Standard Library (Intro) 
#   - Working with Paths
#   - Working with Directories
#   - 
#   - 
#   - 
#   - 

#------------------------------------------------------------------------------
# Working with Paths

from pathlib import Path

Path("C:\\Users\\nikita.dakhno\\SynologyDrive\\Nikita\\Python\\Code\\CwM_8.1.2_Paths")
# we have to use \\ because \ is an escape character

Path(r"C:\Users\nikita.dakhno\SynologyDrive\Nikita\Python\Code\CwM_8.1.2_Paths")
# r for raw String

#Path("/usr/local/bin")  #Mac or Linux
Path()  # current folder
Path("CwM_Module_Direct")   # current folder, sub folder
Path() / Path("CwM_Module_Direct") # comibing Paths
Path() / "CwM_Module_Direct" / "__init__.py"   # combining with strings
Path.home() #home directory of the user


path = Path("CwM_Module_Direct/CwM_Module_sales2.py") 

path.exists()
path.is_file()
path.is_dir()

print(path.exists())
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)

print("old path:", path)
path = path.with_name("file.txt")   # ersetzt with_name("file.txt") den Dateinamen im Pfad durch "file.txt", ohne den Verzeichnispfad zu ändern.
print(".withname: ", path)


path2 = Path("CwM_Module_Direct/CwM_Module_sales2.py") 
print(path2.absolute())





