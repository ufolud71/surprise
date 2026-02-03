from browser import document

scale = 1.0

yes = document["yes"]
no  = document["no"]
msg = document["msg"]
q   = document["q"]

def apply_transform():
    # Ważne: zachowujemy translate, a dokładamy skalę
    yes.style.transform = f"translate(20px, -50%) scale({scale})"

def on_no(ev):
    global scale
    scale *= 1.35
    apply_transform()

    # opcjonalnie: jak już jest spore, to można zablokować "Nie"
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
