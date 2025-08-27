import flet as ft

STYLE_SIGNUP_G = {
    "main_container_elements_repository": {"alignment": ft.CrossAxisAlignment.CENTER, "scroll": ft.ScrollMode.AUTO},

    "background": {"begin": ft.alignment.top_left, "end": ft.alignment.bottom_right},

    "signup_container": {
        "width": 440,
        "border_radius": 35,
        "opacity": 0,
        "blur": ft.Blur(40, 40, ft.BlurTileMode.MIRROR)
    },

    "change_them_button": {
        "button": {"icon_size": 22},
        "container": {"scale": 1, "animate_scale_rotate": ft.Animation(200, ft.AnimationCurve.BOUNCE_OUT)}
    },

    "animate": ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT),
    "offset_animate": ft.Animation(3000, ft.AnimationCurve.FAST_OUT_SLOWIN)
}