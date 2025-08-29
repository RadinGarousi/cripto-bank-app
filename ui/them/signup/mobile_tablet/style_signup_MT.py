import  flet as ft
# from ui.pages.signup.global_signup import GlobalSignupWidgets

STYLE_SIGNUP_MT = {
    "main_container": {"padding": {"vertical": 20, "horizontal": 20}},

    "change_them_button": {
        "container": {
            "width": 30,
            "height": 30,
            "border_radius": 1
        }
    },

    "signup_container": {"height": 100, "padding": 0, "offset": ft.Offset(0, 1.5)},

    "appbar": {
        "height": 100,
        "opacity": 0,
        "scale": ft.Scale(scale=0.5),
        "offset": ft.Offset(0, -1),
        "bgcolor": ft.Colors.PURPLE
    }
}