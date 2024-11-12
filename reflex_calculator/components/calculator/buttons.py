import reflex as rx

def number_button(number:str, on_click=None):
    return rx.button(
        number,
        color_scheme='gray',
        on_click=on_click
    )

def operation_button(icon_name:str, on_click=None):
    return rx.icon_button(
        icon_name,
        color_scheme='orange',
        on_click=on_click
    )

def action_icon_button(icon_name:str, on_click=None):
    return rx.icon_button(
        icon_name,
        color='orange',
        color_scheme='gray',
        on_click=on_click
    )

def action_button(text:str= ' ', on_click=None):
    return rx.button(
        rx.text(text, color_scheme='orange'),
        color_scheme='gray',
        on_click=on_click
    )