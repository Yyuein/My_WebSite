import reflex as rx

# 创建 Reflex 页面
def writing_animation_page():
    # 使用 rx.raw 插入全局 CSS
    global_styles = rx.raw("""
        <style>
        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }
        
        @keyframes blink {
            50% { border-color: transparent; }
        }
        
        .typing-effect {
            font-family: monospace;
            font-size: 2.5em;
            white-space: nowrap;
            overflow: hidden;
            border-right: 3px solid #ffffff; /* 模拟光标 */
            width: 0; /* 初始宽度为0 */
            animation: typing 4s steps(40, end), blink 0.7s step-end infinite;
        }
        
        .typing-effect-delay {
            animation-delay: 4s;
            animation-fill-mode: forwards;
        }
        </style>
    """)

    # 页面内容
    return rx.fragment(
        global_styles,  # 添加全局样式
        rx.vstack(
            rx.text(
                '"Just some bits and bobs',
                class_name="typing-effect",  # 应用动画样式
            ),
            rx.text(
                'Hope you have fun ~"',
                class_name="typing-effect typing-effect-delay",  # 应用延迟动画样式
            ),
            background_color="#d5d9de",
            font_size="2.5em",
            text_align="center",
            justify="center",
            align_items="center",
            color="#ffffff",
            width="100%",
            height="40%",
        ),
    )

# 创建 Reflex 应用
app = rx.App()
app.add_page(writing_animation_page, route="/")
app.compile()

