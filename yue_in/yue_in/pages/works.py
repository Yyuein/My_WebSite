import reflex as rx
from yue_in.template.template import base_page

COLOR_PALETTE = {
    "background_light": "#F0F2F5",  
    "card_background": "#FFFFFF",   
    "primary_text": "#333333",      
    "secondary_text": "#666666",    
    "accent_color_1": "#8f5a50",    
    "accent_color_2": "#0A72CC",    
    "border_color": "#E0E0E0",      
}

COMMON_BOX_STYLE = {
    "background_color": COLOR_PALETTE["card_background"],
    "border_radius": "8px",         
    "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)", 
    "padding": "1.5em",             
}

IMAGE_BOX_STYLE = {
    **COMMON_BOX_STYLE,
    "width": "30%",
    "height": "100%",
    "display": "flex",
    "align_items": "center",
    "justify_content": "center",
    "padding": "10px", 
}

HEADING_BOX_STYLE = {
    "background_color": COLOR_PALETTE["card_background"],
    "border_radius": "8px",
    "box_shadow": "none", 
    "width": "100%",
    "height": "20%",
    "margin_bottom": "1em",
    "padding": "1em",
    "display": "flex",
    "align_items": "center",
    "justify_content": "flex-start",
}

TEXT_CONTENT_BOX_STYLE = {
    "background_color": COLOR_PALETTE["card_background"],
    "border_radius": "8px",
    "box_shadow": "none", 
    "width": "100%",
    "height": "80%",
    "overflow": "hidden",
}


ABSTRACT_TEXT_STYLE = {
    "font_size": "0.95em",
    "color": COLOR_PALETTE["secondary_text"],
    "text_align": "start",
}

def work_image_card(src: str) -> rx.Component:
    """A reusable component for displaying a work image with card styling."""
    return rx.box(
        rx.image(
            src=src,
            width="90%",
            height="auto",
            max_height="100%",
            style={
                "object_fit": "contain",
            },
        ),
        **IMAGE_BOX_STYLE,
    )

def work_text_content_card(title: str, abstract_image_src: str, link_href: str = None, is_dialog: bool = False) -> rx.Component:
    """A reusable component for displaying work text content (title, abstract) with card styling."""
    title_heading = rx.heading(
        title,
        font_size="1.4em",
        color=COLOR_PALETTE["primary_text"],
        line_height="1.3",
    )

    if link_href:
        heading_area = rx.link(
            title_heading,
            href=link_href,
            target="_blank",
            text_decoration="none",
            _hover={"color": COLOR_PALETTE["accent_color_2"]},
        )
    elif is_dialog:
        heading_area = rx.dialog.root(
            rx.dialog.trigger(
                rx.button(
                    title_heading,
                    variant="ghost",
                    color_scheme="blue",
                    text_align="left",
                    white_space="normal",
                    height="auto",
                    width="100%",
                    padding="0",
                    justify_content="flex-start",
                )
            ),
            rx.dialog.content(
                rx.dialog.title("This work is still under research!"),
                rx.dialog.close(
                    rx.button("Close", size="3"),
                ),
                style={
                    "background_color": COLOR_PALETTE["card_background"],
                    "border_radius": "8px",
                }
            ),
        )
    else:
        heading_area = title_heading

    return rx.flex(
        rx.box(heading_area, **HEADING_BOX_STYLE),
        rx.box(
            rx.text("Graphical abstract:", **ABSTRACT_TEXT_STYLE, margin_bottom="0.5em"), 
            rx.scroll_area(
                rx.image(
                    src=abstract_image_src,
                    width="100%",
                    height="auto",
                    style={
                        "display": "block",
                        "margin": "auto",
                        "border_radius": "4px",
                    },
                ),
                type="hover",
                scrollbars="vertical",
                style={"overflow": "auto", "padding_right": "10px"},
                width="100%",
                height="100%",
            ),
            **TEXT_CONTENT_BOX_STYLE,
            padding_top="0",
        ),
        spacing="3",
        flex_direction="column",
        height="100%",
        width="70%",
    )

def work_item_row(image_src: str, title: str, abstract_image_src: str, link_href: str = None, is_dialog: bool = False) -> rx.Component:
    """Combines image and text content into a single well-styled work item row."""
    return rx.flex(
        work_image_card(image_src),
        work_text_content_card(title, abstract_image_src, link_href, is_dialog),
        spacing="7",
        padding="2em",
        flex_direction="row",
        align_items="stretch",
        height="50vh",
        width="100%",
        border_bottom=f"1px solid {COLOR_PALETTE['border_color']}",
    )

@rx.page(route="/works")
def works() -> rx.Component:
    return base_page(
        rx.flex(
            work_item_row(
                image_src="/works_1.png",
                title="""Exploration of antifouling
                        zwitterionic polyimide ultrafiltration membrane
                        based on novel aromatic diamine monomer""",
                abstract_image_src="/abstract_1.jpg",
                link_href="https://www.sciencedirect.com/science/article/abs/pii/S1383586620322127",
            ),
            rx.flex(
                rx.box(
                    rx.vstack(
                        rx.icon(
                            "coffee",
                            size=100,
                            color=COLOR_PALETTE["accent_color_1"],
                        ),
                        rx.text(
                            "Still working on it.",
                            font_size="2em",
                            color=COLOR_PALETTE["accent_color_1"],
                            text_align="center",
                        ),
                        align_items="center",
                        justify="center",
                        spacing="3",
                    ),
                    **IMAGE_BOX_STYLE,
                ),
                work_text_content_card(
                    title="Superb anti-icing surface by infusing PG into a superhydrophobic skeleton composed of ZnO and PDMS",
                    abstract_image_src="/abstract_2.png",
                    is_dialog=True,
                ),
                spacing="7",
                padding="2em",
                flex_direction="row",
                align_items="stretch",
                height="50vh",
                width="100%",
            ),
            width="100%",
            height="auto",
            spacing="0",
            padding="2em",
            flex_direction="column",
            font_family="MyFont",
            background_color=COLOR_PALETTE["background_light"],
        )
    )