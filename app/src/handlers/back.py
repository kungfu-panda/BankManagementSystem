from termcolor import colored
import time
import os

def handler() -> str:
    os.system("cls")
    print(colored("""
----------------------------------------------------------------------            
 Ｙｏｕ ｗｉｌｌ ｂｅ ｒｅｄｉｒｅｃｔｅｄ ｉｎ ５ ｓｅｃｏｎｄｓ．． 
----------------------------------------------------------------------
                  
""",color="yellow"))
    time.sleep(5)
    return "HOME"