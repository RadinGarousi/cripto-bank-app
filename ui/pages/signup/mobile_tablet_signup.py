import flet as ft
from ui.them.signup.mobile_tablet import style_signup_MT

class MobileSignupWidgets:
    def __init__(self, global_widgets):

        self.global_widgets = global_widgets
        self.styles = style_signup_MT.STYLE_SIGNUP_MT
        self.mobile_widget()

    def mobile_widget(self):

        self.appbar = ft.Container(
            bgcolor=ft.Colors.BLACK38,
            height=100,
            expand=True
        )

        self.appbar_column = ft.Column(controls=[self.appbar], alignment=ft.MainAxisAlignment.START)