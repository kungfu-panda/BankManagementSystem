import termcolor
import survey

def login_page_main_menu() -> None:

    print("""
---------------------------------------------------------
| ▄▀█ █░█ ▀█▀ █░█ █▀▀ █▄░█ ▀█▀ █ █▀▀ ▄▀█ ▀█▀ █ █▀█ █▄░█ |
| █▀█ █▄█ ░█░ █▀█ ██▄ █░▀█ ░█░ █ █▄▄ █▀█ ░█░ █ █▄█ █░▀█ |      
---------------------------------------------------------
          
""")
    
def redirect() -> str:
    options = ['Ｌｏｇｉｎ\n', 'Ｓｉｇｎ Ｕｐ\n', 'Ｂａｃｋ\n']
    index = survey.routines.select('Ｐｌｅａｓｅ  ｓｅｌｅｃｔ  ｏｎｅ  ｏｆ  ｔｈｅ  ｆｏｌｌｏｗｉｎｇ  ｏｐｔｉｏｎｓ:\n',  options = options,  focus_mark = '> ',  evade_color = survey.colors.basic('white'), insearch_color=survey.colors.basic('green'))
    return index
