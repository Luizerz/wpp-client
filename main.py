import flet as ft
from flet_route import Routing,path
from SignUpView import SignUpView
from ContactListView import ContactListView


id = None
def main(page: ft.Page):
    app_routes = [
        path("/", clear=True, view=SignUpView().view),
        path("/signup/:foo", clear=True, view=ContactListView().view),
    ]
    
    Routing(page=page, app_routes=app_routes)
    page.go(page.route)

ft.app(main, view=ft.AppView.WEB_BROWSER)
