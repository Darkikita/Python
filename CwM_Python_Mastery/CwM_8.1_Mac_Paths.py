# Python Standard Library 
#   - Python Standard Library (Intro) 
#   - Working with Paths
#   - Working with Directories
#   - Working with Files
#   - Working with ZipFiles
#   - 
#   - 

#------------------------------------------------------------------------------
# Working with Paths

from pathlib import Path

# Zeigt das aktuelle Arbeitsverzeichnis
import os
print(os.getcwd())  



Path("/Users/nikita/Documents/Python/nikita_git/nikita/CwM_Python_Mastery/CwM_Module_Direct/CwM_Module_sales2.py")
Path()  # current folder
Path("CwM_Module_Sales.py")
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



#------------------------------------------------------------------------------
#   - Working with Directories

from pathlib import Path


path3 = Path("/Users/nikita/Documents/Python/nikita_git/nikita/CwM_Python_Mastery/ecommerce")


# Überprüfen ob es existiert
print(path3.exists())


# Ordner erstellen
path3.mkdir(parents=True, exist_ok=True)


# Ordner umbennen 
new_path = path3.parent / "ecommerce2"  # Neuer Pfad im selben Verzeichnis
path3 = path3.rename(new_path)
print(path3)


# Ordner entfernen (nur leer)
path3.rmdir()


# Gesamten Ordner mit Inhalt entfernen
import shutil
#shutil.rmtree(path3)  



# Alle Objecte in einem Ordner listen
#iterdir()
path4 = Path("/Users/nikita/Documents/Python/nikita_git/nikita/CwM_Python_Mastery/CwM_Module_Direct")
print(path4.iterdir())  #Generator Object
for p in path4.iterdir():
    print(p)

path5 = Path("nikita/CwM_Python_Mastery/CwM_Module_Direct")
paths = [p for p in path5.iterdir()]
print(paths)


#glob()
paths2 = [p for p in path5.glob("*.*")]
print(paths2)

path5 = Path("nikita/CwM_Python_Mastery/CwM_Module_Direct")
paths2 = [p for p in path5.glob("*")]   # *.* ; **/*.*
print(paths2)

#Rekursiv alle Unterordnerinhalte aufzählen
paths3 = [p for p in path5.rglob("*")] 
print(paths3)


#------------------------------------------------------------------------------
# Working with Files

#Dateistatus
path6 = Path("nikita/CwM_Python_Mastery/CwM_Module_Direct")

print(path6.stat())

path6 = Path("nikita/CwM_Python_Mastery/CwM_Module_Direct")

print(path6.stat().st_ctime)


from time import ctime

print(ctime(path6.stat().st_ctime))

# Datei lesen, schreiben, überschreiben
path7 = Path("nikita/CwM_Python_Mastery/CwM_File.txt")

print(path7.read_bytes())
print(path7.read_text())

print("---")
#open(Filename, Mode)
with open(path7, "r") as f:
    print(f)
    content = f.read()
    print(content)

print("---")
path7.write_text("write_text, override")
print(path7.read_text())

print("---")
path7.write_bytes(b"wirte_bytes, override")
print(path7.read_text())


#Datei bewegen

import shutil

source = Path("nikita/CwM_Python_Mastery/CwM_Module_Direct/CwM_Move.txt")
target = Path("nikita/CwM_Python_Mastery")

shutil.move(str(source), str(target))   


#------------------------------------------------------------------------------
# Working with ZipFiles

from zipfile import ZipFile

#Creating a ZipFile
zip = ZipFile("nikita/CwM_Python_Mastery/files.zip", "w") # we create a zipfile we want to write in
for path in Path("nikita/CwM_Python_Mastery/CwM_Module_Direct").rglob("*.*"):
    zip.write(path)
zip.close()
#alternativ:
# with ZipFile("files.zip, w") as zip:
#     for path in Path("nikita/CwM_Python_Mastery").rglob("*.*"):
#         zip.write(path)


#Reading a ZipFile
with ZipFile("nikita/CwM_Python_Mastery/files.zip") as zip:
    print(zip.namelist())
    
    info = zip.getinfo("nikita/CwM_Python_Mastery/CwM_Module_Direct/CwM_Module_sales2.py")
    print(info.file_size)
    print(info.compress_size)
    
    
#ChatGBT: ZipFile Inhaltsgröße
with ZipFile("nikita/CwM_Python_Mastery/files.zip") as zip:
    total_size = sum(info.file_size for info in zip.infolist())
    total_compressed = sum(info.compress_size for info in zip.infolist())

    print(f"📦 Gesamtgröße: {total_size} Bytes")
    print(f"📦 Komprimiert: {total_compressed} Bytes")