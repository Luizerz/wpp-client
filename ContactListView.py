import flet as ft
from flet_route import Params, Basket

class ContactListView():
    def __init__(self) -> None:
        pass
    def view(self, page: ft.Page, params: Params, basket: Basket):
        print(params)
        foo = params.get("foo")

        return ft.View("/signup/:foo", controls=[
            ft.Text(f"ContactList {foo}"),
            ft.ElevatedButton("Go Back", on_click=lambda _ :page.go(f"/")),
        ])
        