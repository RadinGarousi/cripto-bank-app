import flet as ft

DARK_SIGNUP_G = {
    "main_container": {
        "gradient_color": ["#020202", "#101829", "#1E2837", "#313D4F"]
    },

    "change_them_button": {
        "button": {
            "icon": ft.Icons.LIGHT_MODE_OUTLINED,
            "icon_color": ft.Colors.with_opacity(0.8, ft.Colors.WHITE)
        }
    },

    "signup_container": {
        "bgcolor": ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        "border": ft.border.all(2, ft.Colors.with_opacity(0.4, ft.Colors.WHITE))
    },

}