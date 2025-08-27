import flet as ft
import math

class StyleSignupDesktop:

    @staticmethod
    def change_them_button_container_hover(colors: dict, page, e):
        if e.data == "true":
            e.control.rotate = math.pi / 5
            e.control.scale = 1.1
            e.control.bgcolor = colors["change_them_button"]["container"]["hover"]
        else:
            e.control.rotate = 0
            e.control.scale = 1
            e.control.bgcolor = colors["change_them_button"]["container"]["bgcolor"]
        page.update()


STYLE_SIGNUP_D = {
    "main_container": {
        "padding": {"vertical": 100, "horizontal": 75}
    },

    "signup_container": {"height": 700, "padding": 30, "offset": ft.Offset(2, 0)},

    "change_them_button": {
        "container": {
            "width": 50,
            "height": 50,
            "border_radius": 60
        }
    }

}