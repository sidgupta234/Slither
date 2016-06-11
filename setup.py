import cx_Freeze

executables =[cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name="Slither",
    options={"build_exe":{"packages":["pygame"], "include_files":["apple.png","Untitled.png" ]}},

    description ="Slither Game Tutorial",
    executables=executables
    )
