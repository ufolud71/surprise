from js import document
from pyodide.ffi import create_proxy

scale = 1.0

# trzymamy referencje globalnie, żeby proxy nie zostało zniszczone
_yes_cb = None
_no_cb = None

yes = document.getElementById("yes")
no  = document.getElementById("no")
msg = document.getElementById("msg")
q   = document.getElementById("q")

def on_no(event):
    global scale
    scale *= 1.35
    yes.style.fontSize = f"{22 * scale}px"
    yes.style.padding  = f"{12 * scale}px {22 * scale}px"

    if scale > 6:
        msg.innerText = "Ups… chyba jednak TAK 😄"
        no.disabled = True
        yes.style.width = "90%"
        yes.style.height = "180px"

def on_yes(event):
    q.innerText = "Yay!! 💘💘💘"
    msg.innerText = "To randka! 😍"
    yes.disabled = True
    no.disabled = True

# tworzymy proxy i przypinamy
_no_cb  = create_proxy(on_no)
_yes_cb = create_proxy(on_yes)

no.addEventListener("click", _no_cb)
yes.addEventListener("click", _yes_cb)
