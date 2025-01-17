import reflex as rx
from rxconfig import config

def footer() -> rx.Component:
    return rx.el.footer(
            rx.flex(
                rx.hstack(
                    rx.image(
                        src="/icon_2.png",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "Copyright © Yue in 2024",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        font_family="MyFont",
                        font_size="1em",
                        color="#4b4641"
                    ),
                    spacing="2",
                    align="center",
                    justify_content=[
                        "center",
                        "center",
                        "start",
                    ],
                    width="100%",
                ),
                rx.color_mode.button(),
                rx.image(
                        src="/footer.png",
                        width="4.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                spacing="1",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            spacing="5",
        width="100%",
        bg="#d5d9de",
    )