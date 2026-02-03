from pyscript import document, when

scale = 1.0

@when("click", "#no")
def on_no(event):
    global scale
    scale *= 1.35

    yes = document.querySelector("#yes")
    msg = document.querySelector("#msg")
    no  = document.querySelector("#no")

    yes.style.fontSize = f"{22 * scale}px"
    yes.style.padding  = f"{12 * scale}px {22 * scale}px"

    if scale > 6:
        msg.innerText = "Ups… chyba jednak TAK 😄"
        no.disabled = True
        yes.style.width = "90%"
        yes.style.height = "180px"

@when("click", "#yes")
def on_yes(event):
    q   = document.querySelector("#q")
    msg = document.querySelector("#msg")
    yes = document.querySelector("#yes")
    no  = document.querySelector("#no")

    q.innerText = "Yay!! 💘💘💘"
    msg.innerText = "To randka! 😍"
    yes.disabled = True
    no.disabled = True
