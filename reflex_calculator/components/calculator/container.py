import reflex as rx


def calc_container(*args):
    return rx.card(
        rx.inset(
            rx.heading(
                "Hello world",
                padding_x="1rem",
                padding_top="1rem",
                color_scheme="gray",
                bg="gray",
            ),
            side="top",
            pb="current",
        ),
        rx.vstack(args),
        size="3",
    )
