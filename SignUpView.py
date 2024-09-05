import flet as ft
from flet_route import Params, Basket

class SignUpView():
    def __init__(self) -> None:
        pass
    def view(self, page: ft.Page, params: Params, basket: Basket):
        print(params)
        send_your_params = "teste"
        return ft.View("/", controls=[
            ft.Text("HomeScreen"),
            ft.ElevatedButton("Sign Up", on_click=lambda _ :page.go(f"/signup/{send_your_params}")),
        ])
        