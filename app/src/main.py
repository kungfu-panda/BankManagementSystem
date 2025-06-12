from handlers import home
from handlers import authenticate

CURRENT_SLIDE = "HOME"
SLIDES = {
    "HOME":home.handler,
    "AUTHENTICATE":authenticate.handler
}

while True:
    try:
        next_frame = SLIDES[CURRENT_SLIDE]()
        CURRENT_SLIDE = next_frame
        
    except KeyboardInterrupt:
        break