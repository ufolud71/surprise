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
    "Na pewno nie?",
    "Jak możesz ;__;",
    "No weeeeź Iza",
    "Co za harpia",
]

last_text = no.text

def random_no_text():
    global last_text
    choices = [t for t in NO_TEXTS if t != last_text]
    new_text = random.choice(choices)
    last_text = new_text
    return new_text

def apply_transform():
    yes.style.transform = f"translate(20px, -50%) scale({scale})"

def on_no(ev):
    global scale

    # zmiana tekstu "Nie"
    no.text = random_no_text()

    # powiększ "Tak"
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

apply_transform()
