import reflex as rx
from ..components.calculator.calculator import calculator


@rx.page(route="/", title="Home", description="My first app using reflex")
def index() -> rx.Component:
    return rx.center(
        calculator(),
        direction="column",
        margin_top='2rem'
    )
