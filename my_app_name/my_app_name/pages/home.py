import reflex as rx

from rxconfig import config
from my_app_name.template.template import base_page


@rx.page(route='/')
def home() -> rx.Component:
    # Welcome Page (Index)
    return base_page(rx.container(
        rx.vstack(
            rx.hstack(
                rx.image(src="/icon_2.png", width="100px", height="auto"),
                rx.heading("泥嚎~窝系一个小网页", size="9"),
                ),
            rx.text(
                "来尽情地使用窝吧~ ",
                #rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Github"),
                href="https://github.com/Yyuein",
            ),
            
            #rx.image(src="/icon.jpg", width="100px", height="auto"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.color_mode.button(),
    )
    )