import termcolor
import os
import survey

def login_page_main_menu() -> None:
    os.system("cls")
    print("""
---------------------------------------------------------
| ▄▀█ █░█ ▀█▀ █░█ █▀▀ █▄░█ ▀█▀ █ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ |
| █▀█ █▄█ ░█░ █▀█ ██▄ █░▀█ ░█░ █ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ |      
---------------------------------------------------------
          
""")
    
def redirect() -> str:
    options = ['Ｌｏｇｉｎ\n', 'Ｓｉｇｎ Ｕｐ\n', 'Ｂａｃｋ\n']
    index = survey.routines.select('Ｐｌｅａｓｅ  ｓｅｌｅｃｔ  ｏｎｅ  ｏｆ  ｔｈｅ  ｆｏｌｌｏｗｉｎｇ  ｏｐｔｉｏｎｓ:\n',  options = options,  focus_mark = '> ',  evade_color = survey.colors.basic('white'), insearch_color=survey.colors.basic('green'))
    return options[index]
    survey.routines.select()
