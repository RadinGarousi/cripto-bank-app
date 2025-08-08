import flet as ft
import asyncio
# from ui.them.signup.desktop import signup_dark_D, signup_light_D
from ui.pages.signin import mobile, tablet, desktop, global_

class Signin:
    """
    This class is responsible for configuring window settings, placing signup page widgets responsively,
    applying animations to them and managing their color them
    """
    def __init__(self, page: ft.Page):
        """This method is responsible for configuring window settings and
        calling (place_item) method to place the signup page widgets"""

        # create state variables
        self.page = page
        self.device = ""

        # set window settings
        self.color_mode = self.page.platform_brightness.value
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.SYSTEM
        self.page.scroll = ft.ScrollMode.ALWAYS
        self.page.window.maximized = True
        self.page.window.min_width = 520
        self.page.title = "کریپتو بانک"
        self.page.padding = 0

        # Detecting the user's device by monitor resolution
        if self.page.width >= 1200:
            self.device = "desktop"
        elif self.page.width >= 650:
            self.device = "tablet"
        else:
            self.device = "mobile"

        self.global_widgets = global_.GlobalSignupWidgets(self.color_mode, self.page, self.device)
        self.mobile_widgets = mobile.MobileSignupWidgets(self.global_widgets)
        self.page.on_platform_brightness_change = self.global_widgets.change_them

        #
        # self.responsive = {
        #     "mobile": mobile.MOBILE_SIGNIN,
        #     "tablet": tablet.TABLET_SIGNIN,
        #     "desktop": desktop.DESKTOP_SIGNIN
        # }[self.device]

        self.page.update()
        self.place_item()

        # self.build_signup_form() if self.device == "desktop" else self.mobile_and_tablet_widgets()

    # def build_signup_form(self):
    #     # desktop
    #     print("desktop")
    #
    #     self.change_them_button_for_desktop = ft.IconButton(
    #         icon=self.colors["signup_container"]["change_them_button"]["icon"],
    #         icon_color=self.colors["signup_container"]["change_them_button"]["icon_color"],
    #         icon_size=22
    #     )
    #
    #     self.change_them_button_for_desktop_container = ft.Container(
    #         width=50,
    #         height=50,
    #         scale=1,
    #         bgcolor="#525860",
    #         border=ft.border.all(1.5, ft.Colors.WHITE54),
    #         border_radius=60,
    #         content=self.change_them_button_for_desktop,
    #         animate=ft.Animation(200, ft.AnimationCurve.EASE_IN_OUT),
    #         animate_scale=200,
    #         on_hover=lambda e:
    #         setattr(self.change_them_button_for_desktop_container, "scale", 1.1 if e.data == "true" else 1)
    #         or setattr(self.change_them_button_for_desktop_container, "bgcolor", "#686c74" if e.data == "true" else "#525860")
    #         or self.page.update()
    #     )
    #
    #     self.global_widgets()
    #
    # def global_widgets(self):
    #
    #
    #
    # def mobile_and_tablet_widgets(self):
    #     if self.device == "mobile" or self.device == "tablet":
    #
    #         mobile.MobileWidgetsSignin(self.color_mode)
    #         self.global_widgets()

    def place_item(self):

        """This method for place the signup page elements"""

        if self.device == "desktop":
            self.global_widgets.signup_widgets_repository.controls.append(
                self.global_widgets.change_them_button_container
            )

            self.page.add(self.global_widgets.main_container)
            self.page.run_task(self.animations)

        # elif self.device == "mobile":
        #     print("a")
        #     # self.signup_widgets.controls = [self.change_them_button_for_desktop_container]
        #     self.main_container.gradient = mobile.MobileWidgetsSignin(self.color_mode)
        #     self.page.add(self.main_container)
        #     self.page.run_task(self.animations)

    async def animations(self):
        """This method is responsible for apply animations to active widgets"""

        await asyncio.sleep(0.05)
        self.global_widgets.signup_container.opacity = 1
        self.global_widgets.signup_container.scale = 1
        self.page.update()

    # def change_them(self, e):
    #     if self.colors != self.page.theme_mode.SYSTEM:
    #         self.color_mode = self.page.platform_brightness.value
    #         self.colors = signup_dark_D.DARK_THEM if self.color_mode == "dark" else signup_light_D.LIGHT_THEM
    #         self.background_gradient.colors = self.colors["main_background"]["background_colors"]
    #         self.background_gradient.radius = self.colors["main_background"]["radius"]
    #
    #         self.signup_container.bgcolor = self.colors["signup_container"]["bgcolor"]
    #         self.signup_container.border = self.colors["signup_container"]["border"]
    #         self.page.update()

    # def resize(self, e):
    #     print("resized")
    #     if self.page.width >= 1200:
    #         self.device = "desktop"
    #     elif self.page.width >= 650:
    #         self.device = "tablet"
    #     else:
    #         self.device = "mobile"
    #
    #     if self.device == "mobile":
    #         print("mobile")
    #         # mobile_ui = mobile.MobileWidgetsSignin(self.color_mode)
    #         self.b = ft.LinearGradient(
    #             begin=ft.alignment.top_left,
    #             end=ft.alignment.bottom_left,
    #             colors=[
    #     "#000000,"
    #     "#0f172a",
    #     "#1e293b",
    #     "#334155",
    #     "#0f172a"
    #                                ],
    #             # stops=[0.0, 0.25, 0.75, 1.0]
    #         )
    #         self.page.g = self.b
    #         self.page.update()
