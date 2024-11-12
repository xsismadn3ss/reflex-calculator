import reflex as rx
from .container import calc_container

def calculator():
    return calc_container(
        rx.hstack(
            rx.button('1'),
            rx.button('2'),
            rx.button('3'),
        ),
    )
