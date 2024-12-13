import reflex as rx

from rxconfig import config
from my_app_name.template.template import base_page


@rx.page(route="/workes")
def workes() -> rx.Component:
    return base_page(
        rx.flex(
            rx.flex(
                rx.box(
                    rx.image(
                        src="/workes_1.png",
                        width="100%",
                        height="100%",
                        style={
                            "display": "block",
                            "margin": "auto",
                        },
                    ),
                    background_color="#d5d9de",
                    color="#ffffff",
                    width="30%",
                    height="100%",
                    padding="5px",
                ),
                rx.flex(
                    rx.box(
                        rx.link(
                            rx.heading(
                                """Exploration of antifouling 
                                        zwitterionic polyimide ultrafiltration membrane 
                                        based on novel aromatic diamine monomer""",
                                font_size="0.91em",
                            ),
                            href="https://www.sciencedirect.com/science/article/abs/pii/S1383586620322127",
                            target="_blank",
                        ),
                        background_color="#d5d9de",
                        color="#ffffff",
                        width="100%",
                        height="20%",
                        margin="auto",
                        padding="4px",
                    ),
                    rx.box(
                        rx.scroll_area(
                            rx.text(
                                "Graphical abstract:",
                                font_size="1em",
                                color="#8f5a50",
                                text_align="start",
                                justify="start",
                                align_items="top",
                            ),
                            rx.image(
                                src="/abstract_1.jpg",
                                width="100%",
                                height="auto",
                                style={
                                    "display": "block",
                                    "margin": "auto",
                                },
                            ),
                            type="hover",
                            scrollbars="vertical",
                            style={"overflow": "auto"},
                            width="100%",
                            height="100%",
                        ),
                        background_color="#d5d9de",
                        color="#ffffff",
                        width="100%",
                        height="80%",
                        padding="1em",
                    ),
                    spacing="2",
                    flex_direction="column",
                    height="100%",
                    width="70%",
                ),
                spacing="2",
                padding="1em",
                flex_direction="row",
                height="50vh",
                width="100%",
            ),
            rx.flex(
                rx.box(
                    rx.image(
                        src="/workes_1.png",
                        width="100%",
                        height="100%",
                        style={
                            "display": "block",
                            "margin": "auto",
                        },
                    ),
                    background_color="#d5d9de",
                    color="#ffffff",
                    width="30%",
                    height="100%",
                    padding="5px",
                ),
                rx.flex(
                    rx.box(
                        rx.dialog.root(
                            rx.dialog.trigger(
                            rx.heading('Superb anti-icing surface by infusing PG into a superhydrophobic skeleton composed of ZnO and PDMS', 
                            font_size="0.91em",
                            )
                            ),
                            rx.dialog.content(
                                rx.dialog.title("This work is still under research!"),
                                # rx.dialog.description(
                                #     "This is a dialog component. You can render anything you want in here.",
                                # ),
                                rx.dialog.close(
                                    rx.button("Close", size="3"),
                                ),
                            ),
                        ),
                        background_color="#d5d9de",
                        color="#0A72CC",
                        width="100%",
                        height="20%",
                        margin="auto",
                        padding="4px",
                    ),
                    rx.box(
                        rx.scroll_area(
                            rx.text(
                                "Graphical abstract:",
                                font_size="1em",
                                color="#8f5a50",
                                text_align="start",
                                justify="start",
                                align_items="top",
                            ),
                            rx.image(
                                src="/abstract_1.jpg",
                                width="100%",
                                height="auto",
                                style={
                                    "display": "block",
                                    "margin": "auto",
                                },
                            ),
                            type="hover",
                            scrollbars="vertical",
                            style={"overflow": "auto"},
                            width="100%",
                            height="100%",
                        ),
                        background_color="#d5d9de",
                        color="#ffffff",
                        width="100%",
                        height="80%",
                        padding="1em",
                    ),
                    spacing="2",
                    flex_direction="column",
                    height="100%",
                    width="70%",
                ),
                spacing="2",
                padding="1em",
                flex_direction="row",
                height="50vh",
                width="100%",
            ),
            width="100%",
            height="auto",
            spacing="4",
            padding="1em",
            flex_direction="column",
            font_family="MyFont",
        )
    )
