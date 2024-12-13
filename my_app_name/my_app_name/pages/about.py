import reflex as rx
from rxconfig import config
from my_app_name.template.template import base_page


@rx.page(route="/about")
def about() -> rx.Component:
    return base_page(
        rx.flex(
            rx.flex(
                rx.box(
                    rx.text("Digital Drawing"),
                    background_color="#d5d9de",
                    color="#ffffff",
                    text_align="center",
                    font_size="1.6em",
                    width="100%",
                    height="10%",
                    padding="4px",
                ),
                rx.box(
                    rx.scroll_area(
                        rx.image(
                            src="/1.jpg",
                            width="370px",
                            height="auto",
                            style={
                                "display": "block",  # 将图片作为块元素
                                "margin": "auto",  # 自动设置左右外边距
                            },
                        ),
                        rx.image(
                            src="/2.jpg",
                            width="370px",
                            height="auto",
                            style={
                                "display": "block",
                                "margin": "auto",
                            },
                        ),
                        rx.image(
                            src="/3.jpg",
                            width="370px",
                            height="auto",
                            style={
                                "display": "block",
                                "margin": "auto",
                            },
                        ),
                        rx.image(
                            src="/4.jpg",
                            width="370px",
                            height="auto",
                            style={
                                "display": "block",
                                "margin": "auto",
                            },
                        ),
                        rx.image(
                            src="/5.jpg",
                            width="370px",
                            height="auto",
                            style={
                                "display": "block",
                                "margin": "auto",
                            },
                        ),
                        rx.image(
                            src="/6.jpg",
                            width="370px",
                            height="auto",
                            style={
                                "display": "block",
                                "margin": "auto",
                            },
                        ),
                        rx.image(
                            src="/7.jpg",
                            width="370px",
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
                    font_size="1.5em",
                    width="100%",
                    height="90%",
                    padding="4px",
                ),
                spacing="2",
                padding="1em",
                flex_direction="column",
                height="100%",
                width="45%",
            ),
            rx.flex(
                rx.box(
                    rx.text("Education"),
                    background_color="#d5d9de",
                    color="#ffffff",
                    text_align="center",
                    font_size="1.6em",
                    width="100%",
                    height="10%",
                    padding="4px",
                ),
                rx.box(
                    rx.scroll_area(
                        rx.flex(
                            rx.box(
                                rx.link(
                                    rx.button(
                                        "Northeast Forestry University",
                                        style={
                                            "width": "100%",  # 设置按钮宽度
                                            "height": "100%",  # 设置按钮高度
                                            "padding": "0px 0px",  # 内边距，调整按钮内部文字与边框的距离
                                            "font-size": "18px",
                                            "color": "#ffffff",  # 设置文字颜色
                                            "background-color": "#4b4641",  # 设置按钮背景颜色
                                            "border": "transparent",  # 设置边框颜色
                                        },
                                    ),
                                    href="https://www.nefu.edu.cn/",target="_blank",
                                ),
                                width="100%",
                                height="5%",
                            ),
                            rx.image(
                                src="/time_1.png",
                                width="100%",
                                height="45%",
                                style={
                                    "display": "block",
                                    "margin": "auto",
                                },
                            ),
                            rx.box(
                                rx.link(
                                    rx.button(
                                        "University of Tsukuba-NIMS Joint Graduate",
                                        style={
                                            "width": "100%",  # 设置按钮宽度
                                            "height": "100%",  # 设置按钮高度
                                            "padding": "0px 0px",  # 内边距，调整按钮内部文字与边框的距离
                                            "font-size": "18px",
                                            "color": "#ffffff",  # 设置文字颜色
                                            "background-color": "#4b4641",  # 设置按钮背景颜色
                                            "border": "transparent",  # 设置边框颜色
                                        },
                                    ),
                                    href="https://www.nims.go.jp/tsukuba/en/",target="_blank",
                                ),
                                width="100%",
                                height="5%",
                            ),
                            rx.image(
                                src="/time_2.png",
                                width="100%",
                                height="45%",
                                style={
                                    "display": "block",
                                    "margin": "auto",
                                },
                            ),
                            width="100%",
                            height="100%",
                            flex_direction="column",
                        ),
                        type="hover",
                        scrollbars="vertical",
                        style={"overflow": "auto"},
                        width="100%",
                        height="100%",
                    ),
                    background_color="#d5d9de",
                    color="#ffffff",
                    font_size="1.5em",
                    width="100%",
                    height="90%",
                    padding="4px",
                    on_mouse_enter=rx.toast("Click on the university name to go to the university's website"),
                ),
                spacing="2",
                padding="1em",
                flex_direction="column",
                height="100%",
                width="45%",
            ),
            rx.flex(
                rx.box(
                    rx.text("Data analysis"),
                    background_color="#d5d9de",
                    color="#ffffff",
                    text_align="center",
                    font_size="1.6em",
                    width="100%",
                    height="10%",
                    padding="4px",
                ),
                rx.box(
                    rx.scroll_area(
                        # on_mouse_enter=rx.toast("Mouse entered"),
                        type="hover",
                        scrollbars="vertical",
                        style={"overflow": "auto"},
                        width="100%",
                        height="100%",
                    ),
                    background_color="#d5d9de",
                    color="#ffffff",
                    font_size="1.5em",
                    width="100%",
                    height="90%",
                    padding="4px",
                ),
                spacing="2",
                padding="1em",
                flex_direction="column",
                height="100%",
                width="45%",
            ),
            width="100%",
            height="85vh",
            spacing="3",
            padding="1em",
            flex_direction="row",
            font_family="MyFont",
        )
    )
