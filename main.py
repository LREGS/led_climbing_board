import home_page


from nicegui import app, ui 

@ui.page("/")
def index_page() -> None:
    home_page.content()

()
ui.run()