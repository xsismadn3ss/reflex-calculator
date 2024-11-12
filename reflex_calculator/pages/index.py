import reflex as rx


@rx.page(route="/", title="Home", description="My first app using reflex")
def index() -> rx.Component:
    return rx.center(  # rx.center is a div with justify center property
        rx.heading("Hello world"),
        direction="column",  # direction is like flex direction on CSS
    )
