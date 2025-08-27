import flet as ft
from ui.them.signup.mobile_tablet import style_signup_MT
class MobileSignupWidgets:
    def __init__(self, global_widgets, global_styles):

        self.global_widgets = global_widgets
        self.styles = style_signup_MT.STYLE_SIGNUP_MT
        self.global_styles = global_styles
        self.mobile_widget()

    def mobile_widget(self):

        self.appbar = ft.Container(
            height=self.styles["appbar"]["height"],
            opacity=self.styles["appbar"]["opacity"],
            scale=self.styles["appbar"]["scale"],
            offset=self.styles["appbar"]["offset"],
            animate_opacity=self.global_styles["animate"],
            animate_scale=self.global_styles["animate"],
            animate_offset=self.global_styles["animate"],
            bgcolor=self.styles["appbar"]["bgcolor"],
            expand=True
        )

        self.appbar_column = ft.Column(controls=[self.appbar], alignment=ft.MainAxisAlignment.START)