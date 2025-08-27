import flet as ft

LIGHT_SIGNUP_G = {
    "main_container": {
        "gradient_color": ["#fafbfc", "#3884f5"]
    },

    "change_them_button": {
        "button": {
            "icon": ft.Icons.DARK_MODE_OUTLINED,
            "icon_color": "#737986"
        }
    },

    "signup_container": {
        "bgcolor": ft.Colors.with_opacity(0.25, ft.Colors.WHITE),
        "border": ft.border.all(2.5, ft.Colors.with_opacity(0.65, ft.Colors.WHITE))
    }

}