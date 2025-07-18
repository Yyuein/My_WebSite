import reflex as rx
from yue_in.pages.home import home
from yue_in.pages.about import about
from yue_in.pages.works import works

class State(rx.State):
    """The app state."""

    ...
    

app = rx.App(_state=State,
    stylesheets=[
        "/font/my_font.css", 
    ],
)
app.add_page(home)
app.add_page(about)
app.add_page(works)
app._compile()
hide_navbar=True
