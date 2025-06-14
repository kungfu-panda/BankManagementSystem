from handlers import home
from handlers import authenticate
from handlers import back
import os

CURRENT_SLIDE = "HOME"
SLIDES = {
    "HOME":home.handler,
    "AUTHENTICATE":authenticate.handler,
    "BACK":back.handler
}

while True:
    try:
        os.system("cls")
        next_frame = SLIDES[CURRENT_SLIDE]()
        CURRENT_SLIDE = next_frame
        
    except KeyboardInterrupt:
        break