from ui.loginpage import login_page_main_menu,redirect

def handler() -> str:
    login_page_main_menu()
    redirect()
    return "err"
