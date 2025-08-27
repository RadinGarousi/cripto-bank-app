import flet as ft

STYLE_SIGNUP_G = {
    "main_container_elements_repository": {"alignment": ft.MainAxisAlignment.CENTER, "scroll": ft.ScrollMode.AUTO},

    "background": {"begin": ft.alignment.top_left, "end": ft.alignment.bottom_right},

    "signup_container": {
        "width": 440,
        "border_radius": 35,
        "opacity": 0,
        "scale": ft.Scale(scale=0.5),
        "blur": ft.Blur(40, 40, ft.BlurTileMode.MIRROR),
        "animate": ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
    },

    "change_them_button": {
        "button": {"icon_size": 22},
        "container": {"scale": 1, "animate_scale_rotate": ft.Animation(200, ft.AnimationCurve.BOUNCE_OUT)}
    }
}