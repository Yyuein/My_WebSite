import reflex as rx
from yue_in.template.template import base_page

HARMONIOUS_PALETTE = {
    "card_background": "#FFFFFF",   
    "primary_text": "#2C3E50",      
    "secondary_text": "#7F8C8D",   
    "accent_primary": "#D5D9DE",    
    "accent_light": "#E2E6E9",      
    "accent_dark": "#BCC2C7",      
    "border_subtle": "#CFD8DC",   
    "button_primary_bg": "#4b4641",
    "button_primary_text": "#FFFFFF",
}

COMMON_CARD_STYLE = {
    "border_radius": "12px",
    "box_shadow": "0 8px 20px rgba(0, 0, 0, 0.15)",
    "padding": "0",
    "color": HARMONIOUS_PALETTE["primary_text"], 
    "transition": "all 0.3s ease-in-out",
    "_hover": {
        "box_shadow": f"0 12px 25px rgba(0, 0, 0, 0.2), 0 0 15px {HARMONIOUS_PALETTE['accent_light']}", 
        "transform": "translateY(-5px)",
    }
}

SECTION_TITLE_STYLE = {
    "background_color": HARMONIOUS_PALETTE["accent_primary"],
    "color": HARMONIOUS_PALETTE["button_primary_text"],
    "text_align": "center",
    "font_size": "2.2em",
    "font_weight": "bold",
    "width": "100%",
    "height": "70px",
    "padding": "0.6em 0",
    "border_radius": "8px 8px 0 0",
    "letter_spacing": "0.1em",
    "flex_shrink": "0",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
}

SCROLL_AREA_INNER_STYLE = {
    "overflow": "auto",
    "padding_right": "10px",
    "border_radius": "8px",
}

def titled_scroll_content(title: str, content_component: rx.Component) -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text(title),
            **SECTION_TITLE_STYLE,
        ),
        rx.box(
            content_component,
            width="100%",
            height="calc(100% - 70px)",
            background_color=HARMONIOUS_PALETTE["card_background"],
            border_radius="0 0 12px 12px",
            padding="1.8em",
            padding_top="0",
        ),
        spacing="0",
        flex_direction="column",
        height="100%",
        width="100%",
        **COMMON_CARD_STYLE,
    )

def image_gallery_scroll_area() -> rx.Component:
    image_paths = ["/1.jpg", "/2.jpg", "/3.jpg", "/4.jpg", "/5.jpg", "/6.jpg", "/7.jpg"]
    images = [
        rx.image(
            src=path,
            width="100%",
            height="auto",
            border_radius="8px",
            object_fit="contain",
            margin_bottom="1em",
            _hover={"transform": "scale(1.02)"},
            transition="transform 0.2s ease-in-out",
        ) for path in image_paths
    ]
    return rx.scroll_area(
        rx.vstack(*images, spacing="4"),
        type="hover",
        scrollbars="vertical",
        style={**SCROLL_AREA_INNER_STYLE, "height": "100%"},
    )

def education_content_scroll_area() -> rx.Component:
    return rx.scroll_area(
        rx.flex(
            rx.link(
                rx.button(
                    "Northeast Forestry University",
                    style={
                        "width": "100%",
                        "padding": "15px 0px",
                        "font_size": "1.2em",
                        "color": HARMONIOUS_PALETTE["button_primary_text"],
                        "background_color": HARMONIOUS_PALETTE["button_primary_bg"],
                        "border": "transparent",
                        "border_radius": "8px",
                        "box_shadow": "0 4px 10px rgba(0, 0, 0, 0.2)",
                        "cursor": "pointer",
                        "transition": "all 0.3s ease",
                        "_hover": {
                            "background_color": HARMONIOUS_PALETTE["accent_light"], 
                            "box_shadow": "0 6px 15px rgba(0, 0, 0, 0.3)",
                            "transform": "translateY(-2px)",
                        },
                    },
                ),
                href="https://www.nefu.edu.cn/",
                target="_blank",
                text_decoration="none",
                width="100%",
                margin_bottom="1.5em",
            ),
            rx.image(
                src="/time_1.png",
                width="100%",
                height="auto",
                border_radius="8px",
                object_fit="contain",
                margin_bottom="1.5em",
            ),
            rx.link(
                rx.button(
                    "University of Tsukuba-NIMS Joint Graduate",
                    style={
                        "width": "100%",
                        "padding": "15px 0px",
                        "font_size": "1.2em",
                        "color": HARMONIOUS_PALETTE["button_primary_text"],
                        "background_color": HARMONIOUS_PALETTE["button_primary_bg"],
                        "border": "transparent",
                        "border_radius": "8px",
                        "box_shadow": "0 4px 10px rgba(0, 0, 0, 0.2)",
                        "cursor": "pointer",
                        "transition": "all 0.3s ease",
                        "_hover": {
                            "background_color": HARMONIOUS_PALETTE["accent_light"],
                            "box_shadow": "0 6px 15px rgba(0, 0, 0, 0.3)",
                            "transform": "translateY(-2px)",
                        },
                    },
                ),
                href="https://www.nims.go.jp/tsukuba/en/",
                target="_blank",
                text_decoration="none",
                width="100%",
                margin_bottom="1.5em",
            ),
            rx.image(
                src="/time_2.png",
                width="100%",
                height="auto",
                border_radius="8px",
                object_fit="contain",
                margin_bottom="1.5em",
            ),
            width="100%",
            height="100%",
            flex_direction="column",
            align_items="center",
            justify="start",
        ),
        type="hover",
        scrollbars="vertical",
        style={**SCROLL_AREA_INNER_STYLE, "height": "100%"},
    )

def projects_content_scroll_area() -> rx.Component:
    return rx.scroll_area(
        rx.flex(
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(
                            "file-code-2",
                            size=50, 
                            color=HARMONIOUS_PALETTE["primary_text"],
                            flex_shrink="0", 
                        ),
                        rx.link(
                            rx.button(
                                "Data-Analysis",
                                size="3",
                                style={
                                    "width": "100%",
                                    "padding": "10px 15px", 
                                    "font_size": "1.2em",
                                    "color": HARMONIOUS_PALETTE["button_primary_text"],
                                    "background_color": HARMONIOUS_PALETTE["button_primary_bg"],
                                    "border": "transparent",
                                    "border_radius": "8px",
                                    "box_shadow": "0 4px 10px rgba(0, 0, 0, 0.2)",
                                    "cursor": "pointer",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "background_color": HARMONIOUS_PALETTE["accent_dark"],
                                        "box_shadow": "0 6px 15px rgba(0, 0, 0, 0.3)",
                                        "transform": "translateY(-2px)",
                                    },
                                },
                                align_items="center",
                                justify="center",
                            ),
                            href="https://github.com/Yyuein/Data-Analysis",
                            target="_blank",
                            text_decoration="none",
                            flex_grow="1", 
                            min_width="0",
                        ),
                        align_items="center",
                        justify_content="start",
                        spacing="4", 
                        width="100%",
                        flex_wrap="wrap", 
                    ),
                    rx.hstack(
                        rx.markdown(
                            "![Jupyter](https://img.shields.io/badge/Jupyter-F37726?style=for-the-badge&logo=jupyter&logoColor=white)"
                            "![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)",
                            align="center",
                            font_size="1em", 
                            style={
                                "display": "flex",
                                "gap": "5px",   
                                "flex_wrap": "wrap",
                                "justify_content": "center",
                                "width": "100%",
                            }
                        ),
                        align_items="center",
                        justify_content="center",
                        spacing="0", 
                        width="100%",
                    ),
                    spacing="4", 
                    width="100%",
                ),
                width="100%", 
                style={
                    "background_color": HARMONIOUS_PALETTE["card_background"],
                    "border_radius": "10px",
                    "box_shadow": "0 4px 10px rgba(0, 0, 0, 0.1)",
                    "padding": "1.5em",
                    "margin_bottom": "1.5em",
                    "overflow": "hidden", 
                }
            ),
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.icon(
                            "file-code-2",
                            size=50, 
                            color=HARMONIOUS_PALETTE["primary_text"], 
                            flex_shrink="0", 
                        ),
                        rx.link(
                            rx.button(
                                "expense_log",
                                size="3", 
                                style={
                                    "width": "100%",
                                    "padding": "10px 15px",
                                    "font_size": "1.2em",
                                    "color": HARMONIOUS_PALETTE["button_primary_text"],
                                    "background_color": HARMONIOUS_PALETTE["button_primary_bg"],
                                    "border": "transparent",
                                    "border_radius": "8px",
                                    "box_shadow": "0 4px 10px rgba(0, 0, 0, 0.2)",
                                    "cursor": "pointer",
                                    "transition": "all 0.3s ease",
                                    "_hover": {
                                        "background_color": HARMONIOUS_PALETTE["accent_dark"],
                                        "box_shadow": "0 6px 15px rgba(0, 0, 0, 0.3)",
                                        "transform": "translateY(-2px)",
                                    },
                                },
                                align_items="center",
                                justify="center",
                            ),
                            href="https://github.com/Yyuein/expense_log",
                            target="_blank",
                            text_decoration="none",
                            flex_grow="1",
                            min_width="0", 
                        ),
                        align_items="center",
                        justify_content="start",
                        spacing="4",
                        width="100%",
                        flex_wrap="wrap",
                    ),
                    rx.hstack(
                        rx.markdown(
                            "![Dart](https://img.shields.io/badge/Dart-00579C?style=for-the-badge&logo=dart&logoColor=white)"
                            "![flutter](https://img.shields.io/badge/Flutter-54C5F8?style=for-the-badge&logo=flutter&logoColor=white)",
                            font_size="1em",
                            style={
                                "display": "flex",
                                "gap": "5px",   
                                "flex_wrap": "wrap",
                                "justify_content": "center",
                                "width": "100%",
                            }
                        ),
                        align_items="center",
                        justify_content="center",
                        spacing="0",
                        width="100%",
                    ),
                    spacing="4",
                    width="100%",
                ),
                width="100%", 
                style={
                    "background_color": HARMONIOUS_PALETTE["card_background"],
                    "border_radius": "10px",
                    "box_shadow": "0 4px 10px rgba(0, 0, 0, 0.1)",
                    "padding": "1.5em",
                    "margin_bottom": "1.5em",
                    "overflow": "hidden", 
                }
            ),
            rx.card(
                rx.hstack(
                    rx.icon(
                        "loader",
                        size=60, 
                        color=HARMONIOUS_PALETTE["primary_text"], 
                        animation="spin 2s linear infinite",
                        flex_shrink="0", 
                    ),
                    rx.text(
                        "More content coming soon~",
                        font_size="1.4em", 
                        text_align="center",
                        color=HARMONIOUS_PALETTE["secondary_text"],
                        letter_spacing="0.05em",
                        white_space="normal", 
                        line_height="1.4",
                        flex_grow="1", 
                        min_width="0",
                    ),
                    align_items="center",
                    justify_content="center",
                    spacing="4", 
                    width="100%",
                    flex_wrap="wrap",
                ),
                align_items="center",
                justify_content="center",
                width="100%",
                style={
                    "background_color": HARMONIOUS_PALETTE["card_background"],
                    "border_radius": "10px",
                    "box_shadow": "0 4px 10px rgba(0, 0, 0, 0.1)",
                    "padding": "1.5em",
                    "display": "flex", 
                    "flex_direction": "column", 
                    "overflow": "hidden", 
                }
            ),
            width="100%",
            height="100%",
            flex_direction="column",
            align_items="center",
            justify="start",
        ),
        type="hover",
        scrollbars="vertical",
        style={**SCROLL_AREA_INNER_STYLE, "height": "100%"},
    )


@rx.page(route="/about")
def about() -> rx.Component:
    return base_page(
        rx.flex(
            rx.box(
                titled_scroll_content(
                    title="Digital Drawing",
                    content_component=image_gallery_scroll_area()
                ),
                width="30%",
                height="100%",
                style=COMMON_CARD_STYLE
            ),
            rx.box(
                titled_scroll_content(
                    title="Education",
                    content_component=education_content_scroll_area()
                ),
                width="32%",
                height="100%",
                style=COMMON_CARD_STYLE,
                on_mouse_enter=rx.toast(
                    "Click on the university name to visit the university's official website.",
                    duration=3000,
                    position="bottom-left",
                ),
            ),
            rx.box(
                titled_scroll_content(
                    title="Projects",
                    content_component=projects_content_scroll_area()
                ),
                width="30%",
                height="100%",
                style=COMMON_CARD_STYLE
            ),
            width="100%",
            height="80vh", 
            spacing="8",
            padding="3em",
            flex_direction="row",
            justify="between",
            align_items="stretch", 
            font_family="MyFont",
            wrap="nowrap",
        )
    )