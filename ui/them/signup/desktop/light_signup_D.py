import flet as ft

LIGHT_SIGNUP_D = {
    "main_container": {
        "gradient_colors": [ "#f0f9ff", "#f0f9ff", "#dbeafe", "#93c5fd", "#73a6fa"]
    },

    "change_them_button": {
        "button":{
            "icon": ft.Icons.DARK_MODE_OUTLINED,
            "icon_color": "#5b6470"
        },
        "container": {
            "bgcolor": "#cee4fe",
            "hover": "#d6e9fe"
        }

    },

    "signup_container": {
        "bgcolor": ft.Colors.with_opacity(0.25, ft.Colors.WHITE),
        "border": ft.border.all(2.5, ft.Colors.with_opacity(0.65, ft.Colors.WHITE))
    }
}