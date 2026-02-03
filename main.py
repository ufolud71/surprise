from browser import document
import random

scale = 1.0

yes = document["yes"]
no  = document["no"]
msg = document["msg"]
q   = document["q"]

# Teksty na przycisku "Nie"
NO_TEXTS = [
    "Nie",
    "Co za harpia...",
    "No weeeeź Iza",
    "Budzik, obudź się",
    "Iza plis 🙏",
    "Jak możesz ;__;",
    "Na pewno nie?",
]

idx = 0  # start

def set_no_text():
    global idx
    no.text = NO_TEXTS[idx]
    if idx < len(NO_TEXTS) - 1:
        idx += 1

def apply_transform():
    yes.style.transform = f"translate(60px, -50%) scale({scale})"

def on_no(ev):
    global scale
    set_no_text()

    scale *= 1.35
    apply_transform()

    if scale > 2.2:
        msg.text = "Ej no… 😄"

def on_yes(ev):
    q.text = "Yay!! 💘💘💘"
    msg.text = "To randka! 😍"
    yes.disabled = True
    no.disabled = True

no.bind("click", on_no)
yes.bind("click", on_yes)

set_no_text()
apply_transform()
