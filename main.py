from js import document

scale = 1.0

def setup():
    global scale
    yes = document.getElementById("yes")
    no  = document.getElementById("no")
    msg = document.getElementById("msg")
    q   = document.getElementById("q")

    def on_no(event=None):
        global scale
        scale *= 1.35
        yes.style.fontSize = f"{22 * scale}px"
        yes.style.padding = f"{12 * scale}px {22 * scale}px"

        if scale > 6:
            msg.innerText = "Ups… chyba jednak TAK 😄"
            no.disabled = True
            yes.style.width = "90%"
            yes.style.height = "180px"

    def on_yes(event=None):
        q.innerText = "Yay!! 💘💘💘"
        msg.innerText = "To randka! 😍"
        yes.disabled = True
        no.disabled = True

    yes.addEventListener("click", on_yes)
    no.addEventListener("click", on_no)

# upewniamy się, że elementy HTML już istnieją
setup()
