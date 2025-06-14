import termcolor

def login_input_menu() -> tuple:
    print("""
----------------------
| █░░ █▀█ █▀▀ █ █▄░█ |
| █▄▄ █▄█ █▄█ █ █░▀█ |
----------------------
""")
    username = str(input("ＵＳＥＲＮＡＭＥ: "))
    password = str(input("ＰＡＳＳＷＯＲＤ: "))