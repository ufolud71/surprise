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

def rects_intersect(a, b):
    return not (a[2] <= b[0] or a[0] >= b[2] or a[3] <= b[1] or a[1] >= b[3])

def move_no_anywhere_avoiding_yes():
    """Ucieka po całym ekranie, ale NIGDY nie wychodzi poza viewport i nie ląduje pod 'Tak'."""
    yesr = yes.getBoundingClientRect()

    # Rozmiar "Nie" (po aktualnym tekście)
    nor = no.getBoundingClientRect()
    no_w = nor.width
    no_h = nor.height

    # Margines od krawędzi ekranu (żeby nie było przy samej krawędzi)
    edge = 12

    # Bufor wokół "Tak", żeby "Nie" nie lądowało pod nim / przy nim
    buf = 18

    vw = window.innerWidth
    vh = window.innerHeight

    # Zakres, w którym środek przycisku może się znaleźć, żeby CAŁY był na ekranie
    min_x = edge + no_w / 2
    max_x = vw - edge - no_w / 2
    min_y = edge + no_h / 2
    max_y = vh - edge - no_h / 2

    # Jeśli ekran jest zbyt mały na przycisk, po prostu przyklej go w bezpieczne miejsce
    if max_x < min_x or max_y < min_y:
        no.style.left = f"{vw * 0.5}px"
        no.style.top = f"{vh * 0.15}px"
        no.style.transform = "translate(-50%, -50%)"
        return

    def rects_intersect(a, b):
        return not (a[2] <= b[0] or a[0] >= b[2] or a[3] <= b[1] or a[1] >= b[3])

    yes_rect = (yesr.left - buf, yesr.top - buf, yesr.right + buf, yesr.bottom + buf)

    # Próbujemy znaleźć miejsce bez kolizji z "Tak"
    for _ in range(80):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)

        # prostokąt "Nie" w viewport
        no_rect = (x - no_w/2, y - no_h/2, x + no_w/2, y + no_h/2)

        if not rects_intersect(no_rect, yes_rect):
            # Clamp na wszelki wypadek (gwarancja 100%)
            x = max(min_x, min(x, max_x))
            y = max(min_y, min(y, max_y))

            no.style.left = f"{x}px"
            no.style.top = f"{y}px"
            no.style.transform = "translate(-50%, -50%)"
            return

    # awaryjnie: miejsce daleko od "Tak" (np. lewy górny róg)
    no.style.left = f"{min_x}px"
    no.style.top = f"{min_y}px"
    no.style.transform = "translate(-50%, -50%)"

def put_no_under_yes():
    """Ustaw 'Nie' dokładnie pod 'Tak' + niższy z-index, żeby zostało zasłonięte."""
    global forced_under_yes, hover_enabled
    forced_under_yes = True
    hover_enabled = False

    r = yes.getBoundingClientRect()
    cx = r.left + r.width / 2
    cy = r.top + r.height / 2

    # No musi być fixed, żeby trzymało się ekranu (jeśli masz fixed w CSS, super)
    no.style.position = "fixed"
    no.style.left = f"{cx}px"
    no.style.top = f"{cy}px"
    no.style.transform = "translate(-50%, -50%)"

    # Upewniamy się, że jest POD "Tak"
    no.style.zIndex = "10001"
    yes.style.zIndex = "10002"

    msg.text = "Dumna z siebie jesteś?"

def on_no(ev):
    global scale, no_clicks, hover_enabled

    # muzyka
    bgm = document["bgm"]
    bgm.volume = 0.1
    bgm.play()

    no_clicks += 1
    set_no_text()

    scale *= 1.35
    apply_transform()

    # po 7 kliknięciach: MUSI wylądować pod TAK i koniec uciekania
    if no_clicks >= 7 and not forced_under_yes:
        put_no_under_yes()
        return

    # po 3 kliknięciach: włącz uciekanie na hover
    if no_clicks >= 3 and not hover_enabled:
        hover_enabled = True
        no.style.transition = "left 0.12s ease, top 0.12s ease"

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
