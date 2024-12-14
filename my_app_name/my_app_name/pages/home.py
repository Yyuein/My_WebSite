import reflex as rx
from rxconfig import config
from my_app_name.template.template import base_page


@rx.page(route="/")
def home() -> rx.Component:
    return base_page(
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
                        font_family="MyFont",
                        font_size="6em",
                        color="black",
                    ),
                    width="100%",
                    height="30%",
                    align_items="center",
                ),
                rx.vstack(
                    rx.text('"Just some bits and bobs'),
                    rx.text('Hope you have fun ~"'),
                    background_color="#d5d9de",
                    font_size="2.5em",
                    text_align="center",
                    justify="center",
                    align_items="center",
                    color="#ffffff",
                    width="100%",
                    height="40%",
                ),
                rx.hstack(
                    rx.icon("mail", size=25),
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
                    color="#4b4641",
                    width="100%",
                    height="10%",
                    align_items="center",
                    justify="center",
                ),
                spacing="2",
                padding="1em",
                flex_direction="column",
                height="100%",
                width="45%",
            ),
            rx.flex(
                rx.box(
                    rx.text("About me"),
                    background_color="#d5d9de",
                    color="#ffffff",
                    font_size="1.5em",
                    width="100%",
                    height="10%",
                    padding="4px",
                ),
                rx.flex(
                    rx.box(
                        rx.link(
                            rx.button(
                                "Digital Drawing",
                                style={
                                    "width": "100px",  # 设置按钮宽度
                                    "height": "50px",  # 设置按钮高度
                                    "padding": "0px 0px",  # 内边距，调整按钮内部文字与边框的距离
                                    "font-size": "25px",
                                    "color": "white",  # 设置文字颜色
                                    "background-color": "transparent",  # 设置按钮背景颜色
                                    "border": "transparent",  # 设置边框颜色
                                    "position": "absolute",
                                    "transform": "translate(-50%, -50%)",
                                    "z-index": "2",
                                },
                            ),
                            href="/about",
                            style={
                                "position": "absolute",
                                "transform": "translate(-50%, -50%)",
                                "border": "1px solid #ccc",
                                "z-index": "2",
                            },
                        ),
                        rx.box(
                            rx.image(
                                src="dd.png",
                                style={
                                    "position": "absolute",
                                    "transform": "translate(0%, 0%)",
                                    "transition": "opacity 0s",
                                    "opacity": "1",
                                    "z-index": "1",
                                    "width": "100%",
                                    "height": "100%",
                                    ":hover": {
                                        "opacity": "0",  # 悬停时透明度变为 0
                                        # "pointer-events": "none",
                                    },
                                },
                            ),
                            style={
                                "width": "100%",
                                "height": "100%",
                                "position": "relative",
                            },
                        ),
                        style={
                            "width": "33%",
                            "height": "100%",
                            "position": "relative",
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "background_color": "#d5d9de",
                        },
                    ),
                    rx.box(
                        rx.link(
                            rx.button(
                                "Education",
                                style={
                                    "width": "100px",  # 设置按钮宽度
                                    "height": "50px",  # 设置按钮高度
                                    "padding": "0px 0px",  # 内边距，调整按钮内部文字与边框的距离
                                    "font-size": "24px",
                                    "color": "white",  # 设置文字颜色
                                    "background-color": "transparent",  # 设置按钮背景颜色
                                    "border": "transparent",  # 设置边框颜色
                                    "position": "absolute",
                                    "transform": "translate(-50%, -50%)",
                                    "z-index": "2",
                                },
                            ),
                            href="/about",
                            style={
                                "position": "absolute",
                                "transform": "translate(-50%, -50%)",
                                "border": "1px solid #ccc",
                                "z-index": "2",
                            },
                        ),
                        rx.box(
                            rx.image(
                                src="ed.png",
                                style={
                                    "position": "absolute",
                                    "transform": "translate(0%, 0%)",
                                    "transition": "opacity 0s",
                                    "opacity": "1",
                                    "z-index": "1",
                                    "width": "100%",
                                    "height": "100%",
                                    ":hover": {
                                        "opacity": "0",  # 悬停时透明度变为 0
                                        # "pointer-events": "none",
                                    },
                                },
                            ),
                            style={
                                "width": "100%",
                                "height": "100%",
                                "position": "relative",
                            },
                        ),
                        style={
                            "width": "33%",
                            "height": "100%",
                            "position": "relative",
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "background_color": "#d5d9de",
                        },
                    ),
                    rx.box(
                        rx.link(
                            rx.button(
                                "Projects",
                                style={
                                    "width": "100px",  # 设置按钮宽度
                                    "height": "50px",  # 设置按钮高度
                                    "padding": "0px 0px",  # 内边距，调整按钮内部文字与边框的距离
                                    "font-size": "25px",
                                    "color": "white",  # 设置文字颜色
                                    "background-color": "transparent",  # 设置按钮背景颜色
                                    "border": "transparent",  # 设置边框颜色
                                    "position": "absolute",
                                    "transform": "translate(-50%, -50%)",
                                    "z-index": "1",
                                },
                            ),
                            href="/about",
                            style={
                                "position": "absolute",
                                "transform": "translate(-50%, -50%)",
                                "border": "1px solid #ccc",
                                "z-index": "2",
                            },
                        ),
                        rx.box(
                            rx.image(
                                src="pj.png",
                                style={
                                    "position": "absolute",
                                    "transform": "translate(0%, 0%)",
                                    "transition": "opacity 0s",
                                    "opacity": "1",
                                    "z-index": "1",
                                    "width": "100%",
                                    "height": "100%",
                                    ":hover": {
                                        "opacity": "0",  # 悬停时透明度变为 0
                                        # "pointer-events": "none",
                                    },
                                },
                            ),
                            style={
                                "width": "100%",
                                "height": "100%",
                                "position": "relative",
                            },
                        ),
                        style={
                            "width": "33%",
                            "height": "100%",
                            "position": "relative",
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "background_color": "#d5d9de",
                        },
                    ),
                    height="40%",
                    width="100%",
                    spacing="4",
                    flex_direction="row",
                ),
                rx.box(
                    rx.text("My workes"),
                    background_color="#d5d9de",
                    font_size="1.5em",
                    color="#ffffff",
                    width="100%",
                    height="10%",
                    padding="4px",
                    align_items="center",
                ),
                rx.flex(
                    rx.card(
                        rx.flex(
                            rx.icon(
                                "notebook-pen",
                                size=25,
                            ),
                            rx.scroll_area(
                                rx.link(
                                    rx.heading(
                                        """Exploration of antifouling 
                                        zwitterionic polyimide ultrafiltration membrane 
                                        based on novel aromatic diamine monomer""",
                                        font_size="1.5em",
                                    ),
                                    href="/workes",
                                ),
                                type="hover",
                                scrollbars="vertical",
                                style={"overflow": "auto"},
                            ),
                            align_items="top",
                            spacing="2",
                        ),
                        flex_direction="row",
                        background_color="#d5d9de",
                        width="100%",
                        height="50%",
                    ),
                    rx.card(
                        rx.hstack(
                            rx.icon(
                                "notebook-pen",
                                size=25,
                            ),
                            rx.scroll_area(
                                rx.link(
                                    rx.heading(
                                        """Superb anti-icing surface by 
                                        infusing PG into a superhydrophobic skeleton 
                                        composed of ZnO and PDMS""",
                                        font_size="1.5em",
                                    ),
                                    href="/workes",
                                ),
                                type="hover",
                                scrollbars="vertical",
                                style={"overflow": "auto"},
                            ),
                            align_items="top",
                            spacing="2",
                        ),
                        width="100%",
                        height="50%",
                        background_color="#d5d9de",
                    ),
                    height="40%",
                    width="100%",
                    spacing="2",
                    flex_direction="column",
                ),
                spacing="2",
                padding="1em",
                flex_direction="column",
                height="100%",
                width="55%",
            ),
            width="100%",
            height="85vh",
            spacing="3",
            padding="1em",
            flex_direction="row",
            font_family="MyFont",
        ),
    )
