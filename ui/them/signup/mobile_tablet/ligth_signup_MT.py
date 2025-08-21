import flet as ft

LIGHT_SIGNUP_MT = {
    "change_them_button": {
        "button": {
            "icon": ft.Icons.LIGHT_MODE_OUTLINED,
            "icon_color": "#4b5563"
        },
        "container": {
            "bgcolor": "#f3faff"
        }
    },

    "appbar": {
        "change_them_button": {
            "button": {
                "icon": ft.Icons.DARK_MODE_OUTLINED,
                "icon_color": "#4b5563"
            },
            "container": {
                "bgcolor": "#f2f9fe",
                "border": ft.border.all(1.5, "#eff6fe")
            }
        }
    }
}