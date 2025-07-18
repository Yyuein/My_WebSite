import reflex as rx
from yue_in.ui.navbar import navbar
from yue_in.ui.footer import footer

def base_page(child:rx.Component, hide_navbar=False,*args,**kwargs)-> rx.Component:
    if not isinstance(child,rx.Component):
        child=rx.heading('no content') 

    return rx.vstack(
        # 导航栏 (如果显示)
        navbar() if not hide_navbar else rx.fragment(), 

        # 主内容区域
        rx.box(
            child, 
            width="100%",
            flex_grow="1",
            overflow_y="auto",
            padding_x="1em", 
            padding_y="1em",
        ),

        # 页脚
        footer(),

        height="100vh", 
        width="100%",
        spacing="0", 
        align_items="stretch", 
    )