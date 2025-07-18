import reflex as rx

def navbar_icons_item(
    text: str, icon: str, url: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4", weight="medium"),
        ),
        href=url,
    )

def navbar_images_item(
    text: str, icon_path: str, url: str
) -> rx.Component:
    return rx.link(
        rx.vstack(
            rx.image(icon_path, width="3em", height="auto"),
            rx.text(
                text, 
                size="3", 
                weight="medium",
                font_family="MyFont",
                font_size="1em",
                color="#8f5a50",
            ),
        ),
        href=url,
    )

def navbar_logo() ->rx.Component:
    return  rx.hstack(
                    rx.image(
                        src="/icon_2.png",
                        width="2.5em",
                        height="auto",
                    ),
                    rx.text("La vie est ailleurs",
                    weight="medium",
                    font_family="MyFont",
                    font_size="1.5em",
                    color="#8f5a50",),
                    
                align_items="center",
                )

def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                navbar_logo(),
                rx.hstack(
                    rx.image(
                        src="/icon_3.png",
                        width="20em",
                        height="auto",
                    ),
                ),
                rx.hstack(
                    navbar_images_item(
                        "HOME", "/home.png", "/#"
                    ),
                    navbar_images_item(
                        "ABOUT", "/about.png", "/about"
                    ),
                    navbar_images_item(
                        "WORKS", "/works.png", "/works"
                    ),
                    spacing="6",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                navbar_logo(),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        navbar_images_item(
                            "HOME", "/home.png", "/#"
                        ),
                        navbar_images_item(
                            "ABOUT", "/about.png", "/ABOUT"
                        ),
                        navbar_images_item(
                            "works", "/works.png", "/works"
                        ),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg="#d5d9de",
        padding="0.2em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )