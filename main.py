from browser import document, window
import random

scale = 1.0
no_clicks = 0
hover_enabled = False
forced_under_yes = False

yes = document["yes"]
no  = document["no"]
msg = document["msg"]
q   = document["q"]

app = document["app"]
final = document["final"]
finalTitle = document["finalTitle"]
finalText = document["finalText"]

NO_TEXTS = [
    "Nie",
    "Co za harpia...",
    "No weeeeź Iza",
    "Budzik, obudź się",
    "Iza plis 🙏",
    "Jak możesz ;__;",
    "Na pewno nie?",
    "Szkoda strzępić ryja",
]

idx = 0

def set_no_text():
    global idx
    no.text = NO_TEXTS[idx]
    if idx < len(NO_TEXTS) - 1:
        idx += 1

def apply_transform():
    yes.style.transform = f"translate(70px, -50%) scale({scale})"

def move_no_anywhere_avoiding_yes():
    _ = no.offsetHeight
    
    vw = window.innerWidth
    vh = window.innerHeight
    
    nor = no.getBoundingClientRect()
    yesr = yes.getBoundingClientRect()
    
    no_w = nor.width
    no_h = nor.height
    
    safe_margin = 50
    buf = 30
    
    min_x = safe_margin + no_w/2
    max_x = vw - safe_margin - no_w/2
    min_y = safe_margin + no_h/2  
    max_y = vh - safe_margin - no_h/2
    
    if min_x >= max_x or min_y >= max_y:
        no.style.left = "100px"
        no.style.top = "100px"
        no.style.transform = "translate(-50%, -50%)"
        return
    
    yes_forbidden = {
        "l": yesr.left - buf,
        "t": yesr.top - buf,
        "r": yesr.right + buf,
        "b": yesr.bottom + buf
    }
    
    for _ in range(200):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        
        l = x - no_w/2
        r = x + no_w/2
        t = y - no_h/2
        b = y + no_h/2
        
        if r <= yes_forbidden["l"] or l >= yes_forbidden["r"] or b <= yes_forbidden["t"] or t >= yes_forbidden["b"]:
            no.style.left = f"{x}px"
            no.style.top = f"{y}px"
            no.style.transform = "translate(-50%, -50%)"
            return
    
    no.style.left = "100px"
    no.style.top = "100px"
    no.style.transform = "translate(-50%, -50%)"

def put_no_under_yes():
    global forced_under_yes, hover_enabled
    forced_under_yes = True
    hover_enabled = False

    r = yes.getBoundingClientRect()
    cx = r.left + r.width / 2
    cy = r.top + r.height / 2

    no.style.position = "fixed"
    no.style.left = f"{cx}px"
    no.style.top = f"{cy}px"
    no.style.transform = "translate(-50%, -50%)"

    no.style.zIndex = "10001"
    yes.style.zIndex = "10002"

    msg.text = "Dumna z siebie jesteś?"

def on_no(ev):
    global scale, no_clicks, hover_enabled

    bgm = document["bgm"]
    bgm.volume = 0.1
    bgm.play()

    no_clicks += 1
    set_no_text()

    scale *= 1.35
    apply_transform()

    if no_clicks >= 7 and not forced_under_yes:
        put_no_under_yes()
        return

    if no_clicks >= 3 and not hover_enabled:
        hover_enabled = True
        no.style.transition = "left 0.12s ease, top 0.12s ease"
        move_no_anywhere_avoiding_yes()

def on_no_hover(ev):
    if hover_enabled and not forced_under_yes:
        move_no_anywhere_avoiding_yes()

def on_yes(ev):
    bgm = document["bgm"]
    bgm.volume = 0.1
    bgm.play()

    app.style.display = "none"
    final.style.display = "block"

    finalTitle.text = "Less GOOOOO!! 💘💘💘"
    finalText.text = "To randka! Widzimy się po powrocie ❤️"

    window.party()

no.bind("click", on_no)
no.bind("mouseover", on_no_hover)
yes.bind("click", on_yes)

set_no_text()
apply_transform()
