import reflex as rx
from yue_in.template.template import base_page

# --- 样式常量和工具函数 (保持不变) ---
ACCENT_COLOR = "#8f5a50"
ACCENT_COLOR_LIGHT= "#E2E6E9",  
BG_COLOR_LIGHT = "#e0e5ec"
BG_COLOR_DARK = "#d5d9de"
TEXT_COLOR_PRIMARY = "#2c3e50"
TEXT_COLOR_SECONDARY = "#4b4641"
TEXT_COLOR_LIGHT = "#ffffff"
TEXT_STYLE = {
    "font_family": "MyFont",
}

LINK_STYLE = {
    "text_decoration": "none",
    "color": "inherit",
}

def image_button_overlay(image_src: str, button_text: str, href: str) -> rx.Component:
    """创建一个带有图片背景和居中按钮的链接盒。"""
    return rx.box(
        rx.link(
            rx.button(
                button_text,
                style={
                    "width": "120px",
                    "height": "60px",
                    "padding": "0px",
                    "font_size": "24px",
                    "color": TEXT_COLOR_LIGHT,
                    "background_color": "rgba(0, 0, 0, 0.5)",
                    "border": "none",
                    "border_radius": "8px",
                    "position": "absolute",
                    "top": "50%",
                    "left": "50%",
                    "transform": "translate(-50%, -50%)",
                    "z_index": "2",
                    "opacity": "0",
                    "transition": "opacity 0.3s ease-in-out",
                    ":hover": {
                        "opacity": "1",
                        "background_color": "rgba(0, 0, 0, 0.7)",
                    },
                },
            ),
            href=href,
            style={
                "position": "absolute",
                "width": "100%",
                "height": "100%",
                "display": "flex",
                "justify_content": "center",
                "align_items": "center",
                "z_index": "2",
            },
        ),
        rx.image(
            src=image_src,
            style={
                "width": "100%",
                "height": "100%",
                "object_fit": "cover",
                "position": "relative",
                "transition": "opacity 0.3s ease-in-out",
                "opacity": "1",
                ":hover": {
                    "opacity": "0.7",
                },
            },
        ),
        style={
            "width": "100%",
            "height": "100%",
            "position": "relative",
            "display": "flex",
            "justify_content": "center",
            "align_items": "center",
            "border_radius": "10px",
            "overflow": "hidden",
            "box_shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
            "cursor": "pointer",
        },
    )

def paper_card(title: str, href: str) -> rx.Component:
    """创建一个包含图标、标题和链接的论文卡片。"""
    return rx.card(
        rx.hstack(
            rx.icon("notebook-pen", size=25, color=ACCENT_COLOR),
            rx.scroll_area(
                rx.link(
                    rx.heading(
                        title,
                        font_size={"base": "1em", "md": "1.2em", "lg": "1.5em"},
                        **TEXT_STYLE,
                        color=TEXT_COLOR_PRIMARY,
                    ),
                    href=href,
                    **LINK_STYLE,
                ),
                type="hover",
                scrollbars="vertical",
                style={"overflow": "auto", "width": "100%"},
            ),
            align_items="top",
            spacing="3",
            width="100%",
        ),
        background_color=BG_COLOR_LIGHT,
        border_radius="10px",
        box_shadow="0 2px 4px rgba(0, 0, 0, 0.08)",
        padding="1em",
        height="100%",
        style={
            "_hover": {
                "background_color": ACCENT_COLOR_LIGHT, 
                "box_shadow": "0 6px 15px rgba(0, 0, 0, 0.3)",
                "transform": "translateY(-2px)",
            },
        },
    )


@rx.page(route="/")
def home() -> rx.Component:
    return base_page(
        rx.flex(
            # 左侧个人信息区域 - 40% 宽度，内容顶部对齐
            rx.flex(
                rx.flex( # 包含头像和 "Yue in"
                    rx.image(
                        src="/icon.jpg",
                        width="100px",
                        height="auto",
                        border_radius="50%",
                        border="3px solid #ffffff",
                        object_fit="cover",
                    ),
                    rx.heading(
                        "Yue in",
                        font_family="MyFont",
                        font_size="6em",
                        color=ACCENT_COLOR,
                        letter_spacing="-2px",
                        weight="bold", # !!! 加粗 "Yue in" !!!
                    ),
                    width="100%",
                    align_items="center",
                    justify_content="center",
                    spacing="4",
                ),
                rx.vstack(
                    rx.text("“Just some bits and bobs”", **TEXT_STYLE, font_size="1.5em", color=TEXT_COLOR_LIGHT, weight="bold"), # !!! 加粗 !!!
                    rx.text("“Hope you have fun ~”", **TEXT_STYLE, font_size="1.5em", color=TEXT_COLOR_LIGHT, weight="bold"), # !!! 加粗 !!!
                    background_color=BG_COLOR_DARK,
                    border_radius="15px",
                    padding="2em",
                    text_align="center",
                    justify="center",
                    align_items="center",
                    width="80%",
                    height="auto",
                    margin_x="auto",
                    box_shadow="inset 0 2px 4px rgba(0, 0, 0, 0.1)",
                ),
                rx.hstack( # 邮箱信息
                    rx.icon("mail", size=25, color=ACCENT_COLOR),
                    rx.text("e-mail:", **TEXT_STYLE, font_size={"base": "0.8em", "md": "1em"}, color=TEXT_COLOR_SECONDARY),
                    rx.text("s2320387@u.tsukuba.ac.jp", **TEXT_STYLE, font_size={"base": "0.8em", "md": "1em"}, color=TEXT_COLOR_SECONDARY),
                    rx.text("/ YU.Yueying@nims.go.jp", **TEXT_STYLE, font_size={"base": "0.8em", "md": "1em"}, color=TEXT_COLOR_SECONDARY),
                    background_color="transparent",
                    width="100%",
                    height="auto",
                    align_items="center",
                    justify_content="center",
                    spacing="2",
                    flex_wrap="wrap",
                ),
                spacing="2",
                padding="1em",
                height="100%",
                width="40%",
                align_items="center",
                justify_content="center",
                direction = "column",
            ),
            # 右侧内容区域 - 60% 宽度
            rx.flex(
                rx.box(
                    rx.text("About me", **TEXT_STYLE, color=TEXT_COLOR_LIGHT, weight="bold"), # !!! 加粗 "About me" !!!
                    background_color=BG_COLOR_DARK,
                    font_size={"base": "1.2em", "md": "1.5em"},
                    width="100%",
                    height={"base": "8%", "md": "10%"},
                    padding="8px",
                    border_radius="8px 8px 0 0",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                rx.flex(
                    image_button_overlay("dd.png", "Digital Drawing", "/about"),
                    image_button_overlay("ed.png", "Education", "/about"),
                    image_button_overlay("pj.png", "Projects", "/about"),
                    height={"base": "30%", "md": "40%"},
                    width="100%",
                    spacing="4",
                    flex_direction={"base": "column", "md": "row"},
                    align_items="center",
                    justify_content="center",
                    padding_y={"base": "1em", "md": "0"},
                ),
                rx.box(
                    rx.text("My Works", **TEXT_STYLE, color=TEXT_COLOR_LIGHT, weight="bold"), # !!! 加粗 "My Works" !!!
                    background_color=BG_COLOR_DARK,
                    font_size={"base": "1.2em", "md": "1.5em"},
                    width="100%",
                    height={"base": "8%", "md": "10%"},
                    padding="8px",
                    border_radius="0 0 8px 8px",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                rx.flex(
                    paper_card(
                        """Exploration of antifouling zwitterionic polyimide ultrafiltration membrane
                        based on novel aromatic diamine monomer""",
                        "/works",
                    ),
                    paper_card(
                        """Antifreeze-infused superhydrophobic surface with superb anti-icing and anti-frosting performance""",
                        "/works",
                    ),
                    height={"base": "54%", "md": "40%"},
                    width="100%",
                    spacing="3",
                    flex_direction="column",
                    align_items="center",
                    justify_content="center",
                ),
                spacing="2",
                padding="1em",
                flex_direction="column",
                width="60%",
                height="100%",
                justify_content="center",
            ),
            width="100%",
            height="100%",
            flex_direction={"base": "column", "md": "row"},
            font_family="MyFont",
            align_items="center",
            justify_content="center",
        ),
        background_color=BG_COLOR_LIGHT,
    )