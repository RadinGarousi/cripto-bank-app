import flet as ft

DARK_SIGNUP_D = {
    "main_container": {
        "gradient_color": ["#020202", "#101829", "#1E2837", "#313D4F"]
    },

    "change_them_button": {
        "button": {
            "icon": ft.Icons.LIGHT_MODE_OUTLINED,
            "icon_color": "#f4f5f7"
        },
        "container": {
            "bgcolor": "#525860",
            # "hover": "#686c74"
        }
    },

    "signup_container": {
        "bgcolor": ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
        "border": ft.border.all(2, ft.Colors.with_opacity(0.4, ft.Colors.WHITE)),
        "change_them_button": {
            "icon": ft.Icons.LIGHT_MODE_OUTLINED,
            "icon_color": ft.Colors.WHITE70,
            "bgcolor": "#525860"
        }
    },

    "mobile_tablet_appbar": {
        "leading": {
            "icon_button": {
                "icon": ft.Icons.DARK_MODE,
                "icon_color": "#4b5563"
            }
        }
    }
}