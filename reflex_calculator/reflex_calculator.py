import reflex as rx
from rxconfig import config
from .pages.index import index

app = rx.App(
    app=rx.App(
        theme=rx.theme(
            appearance="light",
            accent_color="orange",
        )
    )
)
