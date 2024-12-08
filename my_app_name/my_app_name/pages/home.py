import reflex as rx

from rxconfig import config
from my_app_name.template.template import base_page


@rx.page(route='/')
def home() -> rx.Component:
    return base_page(
                rx.flex(
                    rx.flex(
                        rx.flex(
                            rx.box(
                                width="100%",
                                height="10%",
                            ),
                            rx.hstack(
                                rx.image(
                                    src="/icon.jpg", 
                                    width="100px", 
                                    height="auto",
                                    border_radius="50px 50px",
                                ),
                                rx.heading(
                                    "Yue in", 
                                    size="9",
                                    font_family="MyFont",
                                    font_size="6em"
                                ),
                                width="100%",
                                height="30%",
                                align_items="center",
                            ),
                            rx.box(
                                rx.text(
                                    '"Just some bits and bobs'
                                    ),
                                rx.text(
                                    'Hope you have fun ~"'
                                    ),
                                background_color="#d5d9de",
                                font_size="2.5em",
                                text_align="center",
                                color="#ffffff",
                                width="100%",
                                height="40%",
                            ),
                            rx.hstack(
                                rx.icon(
                                    "mail",
                                    size=25
                                    ),
                                rx.text(
                                    "e-mail:",
                                ),
                                rx.text(
                                    "s2320387@u.tsukuba.ac.jp",
                                ),
                                rx.text(
                                    "/  YU.Yueying@nims.go.jp",
                                ),
                                background_color="#d5d9de",
                                font_size="1em",
                                color="black",
                                width="100%",
                                height="10%",
                                align_items="center",
                                justify="center"
                            ),
                            spacing="4",
                            padding="1em",
                            flex_direction="column",
                            height="100%",
                            width="100%",
                        ),
                        rx.flex(
                            rx.box(
                                rx.text(
                                    "About me"
                                ),
                                background_color="#d5d9de",
                                color="#ffffff",
                                font_size="1.5em",
                                width="100%",
                                height="10%",
                                padding="4px",
                            ),
                            rx.flex(
                                    rx.box(
                                        bg=rx.color("accent", 5),
                                        width="33%",   
                                        height="100%",
                                    ),
                                    rx.box(
                                        bg=rx.color("accent", 5),
                                        width="33%",   
                                        height="100%",
                                    ),
                                    rx.box(
                                        bg=rx.color("accent", 5),
                                        width="33%",   
                                        height="100%",
                                    ),
                                    height="40%",
                                    width="100%",
                                    spacing="4",
                                    flex_direction="row",
                                ),
                            rx.box(
                                rx.text(
                                    "My workes"
                                ),
                                background_color="#d5d9de",
                                font_size="1.5em",
                                color="#ffffff",
                                width="100%",
                                height="10%",
                                padding="4px",
                            ),
                            rx.flex(
                                rx.card(
                                    rx.hstack(
                                        rx.icon(
                                            "notebook-pen",
                                            size=25,
                                        ),
                                        rx.box(  
                                            rx.link(
                                                rx.heading("Tittle"),
                                                href="/workes"
                                            ),   
                                            width="85%",
                                            height="100%",
                                        ),
                                        align_items="top",
                                        spacing="2",
                                    ),
                                    width="50%",
                                    height="100%",
                                ),
                                rx.card(
                                    rx.hstack(
                                        rx.icon(
                                            "notebook-pen",
                                            size=25,
                                        ),
                                        rx.box(  
                                            rx.link(
                                                rx.heading("Tittle"),
                                                href="/workes"
                                            ),   
                                            width="85%",
                                            height="100%",
                                        ),
                                        align_items="top",
                                        spacing="2",
                                    ),
                                    width="50%",
                                    height="100%",
                                ),
                                height="40%",
                                width="100%",
                                spacing="4",
                                flex_direction="row",
                            ),
                            spacing="4",
                            padding="1em",
                            flex_direction="column",
                            height="100%",
                            width="100%",
                        ),
                        width="100%",
                        height="100%",
                        spacing="4",
                        flex_direction="row",
                    ),
                    spacing="4",
                    padding="1em",
                    flex_direction="column",
                    height="85vh",
                    width="100%",
                    font_family="MyFont",
                ),
            )