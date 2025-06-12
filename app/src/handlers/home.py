from ui.home import home_page_menu
from ui.home import redirect

def handler() -> str:
    home_page_menu()
    redirect()
    return "AUTHENTICATE"
