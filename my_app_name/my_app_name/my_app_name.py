import reflex as rx
from rxconfig import config
from my_app_name.pages.home import home
from my_app_name.pages.about import about
from my_app_name.pages.workes import workes

class State(rx.State):
    """The app state."""

    ...
    

app = rx.App(state=State,
    stylesheets=[
        "/font/my_font.css", 
    ],
)
app.add_page(home)
app.add_page(about)
app.add_page(workes)
app._compile()
hide_navbar=True
