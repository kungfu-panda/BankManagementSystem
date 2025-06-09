from handlers.homepage import handler

CURRENT_SLIDE = "HOME"
SLIDES = {
    "HOME":handler
}

while True:
    try:
        next_frame = SLIDES[CURRENT_SLIDE]()
        CURRENT_SLIDE = next_frame
        
    except KeyboardInterrupt:
        break