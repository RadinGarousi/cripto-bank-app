import flet as ft

DARK = {
    "main_container": {
        "gradient_color": ["#020202", "#101829", "#1E2837", "#313D4F"]
    },

    "signup_container": {
        "bgcolor": ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        "border": ft.border.all(2, ft.Colors.with_opacity(0.4, ft.Colors.WHITE))
    },

    "change_them_button": {
        "button": {
            "icon": ft.Icons.LIGHT_MODE_OUTLINED,
            "icon_color": ft.Colors.WHITE70
        },
        "container": {
            "bgcolor": "#525860"
        }
    }
}