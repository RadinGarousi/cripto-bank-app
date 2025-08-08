import flet as ft
from ui.them.signup.mobile_tablet import dark_signup_MT, ligth_signup_MT

class MobileSignupWidgets:
    def __init__(self, global_widgets):

        self.global_widgets = global_widgets
        self.mobile_widget()

    def mobile_widget(self):
        pass
        # self.appbar = ft.AppBar(
        #     leading=self.global_widgets.change_them_button_container
        # )



MOBILE_SIGNIN = {
    "signup_container": {
        "width": 440,
        "padding": 0
    }
}