import flet as ft
from ui.them.signup.desktop import dark_signup_D, light_signup_D
from ui.them.signup.mobile_tablet import dark_signup_MT, ligth_signup_MT
from ui.them.signup.global_ import dark_signup_G, light_signup_G

class GlobalSignupWidgets:
    def __init__(self, color_mode: str, page: ft.Page, device: str):
        """Initializes global signup widgets based on the system color mode (dark or light)"""

        self.page = page
        self.color_mode = color_mode
        self.device = device
        self.colors = ""

        if self.device == "desktop":
            self.colors = dark_signup_D.DARK_SIGNUP_D if self.color_mode == "dark" else light_signup_D.LIGHT_SIGNUP_D
        else: self.colors = dark_signup_MT.DARK_SIGNUP_MT if self.color_mode == "dark" else ligth_signup_MT.LIGHT_SIGNUP_MT

        self.global_colors = dark_signup_G.DARK_SIGNUP_G if self.color_mode == "dark" else light_signup_G.LIGHT_SIGNUP_G

        self.base_widgets()

    def signup_widgets(self):
        """In this method create the all signup page"""

        self.change_them_button = ft.IconButton(
            icon=self.colors["change_them_button"]["button"]["icon"],
            icon_color=self.colors["change_them_button"]["button"]["icon_color"],
            icon_size=22
        )

        self.change_them_button_container = ft.Container(
            width=50,
            height=50,
            scale=1,
            bgcolor=self.colors["change_them_button"]["container"]["bgcolor"],
            border=ft.border.all(1.5, ft.Colors.WHITE54),
            border_radius=60,
            content=self.change_them_button,
            animate=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
            animate_scale=200,
            on_hover=lambda e:

            setattr(self.change_them_button_container, "scale", 1.1 if e.data == "true" else 1)
            or setattr(self.change_them_button_container, "bgcolor", "" if e.data == "true" else "#525860")
            or self.page.update()
        )

    def base_widgets(self):
        """
        This method builds the base and global UI widgets for the signup page
        This method builds the background and layout containers for the signup page
        """
        self.signup_widgets_repository = ft.Column(controls=[])

        self.background = ft.LinearGradient(
            colors=self.global_colors["main_container"]["gradient_color"],
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right
        )

        self.signup_container = ft.Container(
            width=440,
            height=700,
            border_radius=35,
            padding=30,
            opacity=0,
            scale=ft.Scale(scale=0.5),
            bgcolor=self.colors["signup_container"]["bgcolor"],
            border=self.colors["signup_container"]["border"],
            blur=ft.Blur(40, 40, ft.BlurTileMode.MIRROR),
            animate_opacity=1000,
            animate_scale=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT_CIRC),
            content=self.signup_widgets_repository
        )

        self.signup_column = ft.Column(
            controls=[self.signup_container],
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.main_container = ft.Container(
            padding=35,
            gradient=self.background,
            alignment=ft.alignment.center,
            content=self.signup_column,
            expand=True
        )

        self.signup_widgets()

    def change_them(self, e):
        """This method is responsible for change app them(light, dark)"""

        # update colors variable
        self.color_mode = self.page.platform_brightness.value
        self.global_colors = dark_signup_G.DARK_SIGNUP_G if self.color_mode == "dark" else light_signup_G.LIGHT_SIGNUP_G

        # update active widgets color
        self.background.colors = self.global_colors["main_container"]["gradient_color"]
        self.signup_container.bgcolor = self.global_colors["signup_container"]["bgcolor"]
        self.signup_container.border = self.global_colors["signup_container"]["border"]

        # update modular widgets color
        if self.page.width >= 1200:
            self.device = "desktop"
        elif self.page.width >= 650:
            self.device = "tablet"
        else:
            self.device = "mobile"

        if self.device == "desktop":
            self.colors = dark_signup_D.DARK_SIGNUP_D if self.color_mode == "dark" else light_signup_D.LIGHT_SIGNUP_D
        else: self.colors = dark_signup_MT.DARK_SIGNUP_MT if self.color_mode == "dark" else ligth_signup_MT.LIGHT_SIGNUP_MT

        self.change_them_button.icon = self.colors["change_them_button"]["button"]["icon"]
        self.change_them_button.icon_colo = self.colors["change_them_button"]["button"]["icon_color"]
        self.change_them_button_container.bgcolor = self.colors["change_them_button"]["container"]["bgcolor"]

        self.page.update()