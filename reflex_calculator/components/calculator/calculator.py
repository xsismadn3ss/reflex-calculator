import reflex as rx
from .container import calc_container
from .buttons import number_button, operation_button, action_icon_button, action_button


def calculator():
    return calc_container(
        rx.hstack(
            action_button("C"),
            action_icon_button("delete"),
            action_button("%"),
            operation_button("divide"),
            justify="end",
            width='100%'
        ),
        rx.hstack(
            number_button("7"),
            number_button("8"),
            number_button("9"),
            operation_button("x"),
            justify="end",
            width='100%'
        ),
        rx.hstack(
            number_button("4"),
            number_button("5"),
            number_button("6"),
            operation_button("minus"),
            justify="end",
            width='100%'
        ),
        rx.hstack(
            number_button("1"),
            number_button("2"),
            number_button("3"),
            operation_button("plus"),
            justify="end",
            width='100%'
        ),
        rx.hstack(
            number_button("."),
            number_button("0"),
            operation_button("equal"),
            justify="end",
            width='100%'
        ),
    )
