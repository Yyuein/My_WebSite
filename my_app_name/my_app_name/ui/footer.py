import reflex as rx
from rxconfig import config

def footer() -> rx.Component:
    return rx.el.footer(
            rx.flex(
                rx.hstack(
                    rx.image(
                        src="/icon_2.png",
                        width="3em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.text(
                        "Contact: ",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        font_family="MyFont",
                        font_size="3em",
                    ),
                    rx.vstack(
                    rx.text(
                        "s2320387@u.tsukuba.ac.jp",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        font_family="MyFont",
                        font_size="1em",
                    ),
                    rx.text(
                        "YU.Yueying@nims.go.jp",
                        size="3",
                        white_space="nowrap",
                        weight="medium",
                        font_family="MyFont",
                        font_size="1em",
                    ),
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
                rx.image(
                        src="/footer.png",
                        width="6em",
                        height="auto",
                        border_radius="25%",
                    ),
                spacing="4",
                flex_direction=["column", "column", "row"],
                width="100%",
            ),
            spacing="5",
        width="100%",
        bg="#d5d9de",
    )