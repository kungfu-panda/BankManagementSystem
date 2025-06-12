from ui.authenticate import login_page_main_menu,redirect

def handler() -> str:
    login_page_main_menu()
    result = redirect()
    if result == 0:
        return "Login"
    elif result==1:
        return "Signup"
    elif result==2:
        return "Back"
    return "err"
