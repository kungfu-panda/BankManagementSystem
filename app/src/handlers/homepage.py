from ui.homepage import home_page_menu
from ui.homepage import redirect

def handler() -> str:
    home_page_menu()
    redirect()
    return "LOGIN"
