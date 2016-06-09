from cx_Freeze import setup, Executable

exe = Executable(
        script="mario.py",
        base="Win32Gui",
        icon="images/mario.png"
        )

includefiles=["images/mario.png", "images/plant.png", "images/coin.png"]
includes=[]
excludes=[]
packages=[]
 
setup(
    name = "mario",
    author = "PangS",
    version = "0.1",
    description = "mario",
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables = [Executable("mario.py")]
    )
