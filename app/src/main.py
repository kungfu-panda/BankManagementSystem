from handlers import homepage
from handlers import loginpage

CURRENT_SLIDE = "HOME"
SLIDES = {
    "HOME":homepage.handler,
    "LOGIN":loginpage.handler
}

while True:
    try:
        next_frame = SLIDES[CURRENT_SLIDE]()
        CURRENT_SLIDE = next_frame
        
    except KeyboardInterrupt:
        break