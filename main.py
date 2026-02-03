from browser import document

scale = 1.0

yes = document["yes"]
no  = document["no"]
msg = document["msg"]
q   = document["q"]

def on_no(ev):
    global scale
    scale *= 1.35
    yes.style.fontSize = f"{22 * scale}px"
    yes.style.padding  = f"{12 * scale}px {22 * scale}px"

    if scale > 6:
        msg.text = "Ups… chyba jednak TAK 😄"
        no.disabled = True
        yes.style.width = "90%"
        yes.style.height = "180px"

def on_yes(ev):
    q.text = "Yay!! 💘💘💘"
    msg.text = "To randka! 😍"
    yes.disabled = True
    no.disabled = True

no.bind("click", on_no)
yes.bind("click", on_yes)
