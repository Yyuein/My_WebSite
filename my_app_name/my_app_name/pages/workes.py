import reflex as rx

from rxconfig import config
from my_app_name.template.template import base_page


@rx.page(route="/workes")
def workes() -> rx.Component:
    return base_page(
        rx.flex(
            rx.box(
                background_color="#d5d9de",
                color="#ffffff",
                font_size="1.5em",
                width="100%",
                height="90%",
                padding="4px",
            ),
            rx.box(
                background_color="#d5d9de",
                color="#ffffff",
                font_size="1.5em",
                width="100%",
                height="90%",
                padding="4px",
            ),
            width="100%",
            height="85vh",
            spacing="3",
            padding="1em",
            flex_direction="column",
            font_family="MyFont",
        )
    )
