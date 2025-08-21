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
        self.page.scroll = ft.ScrollMode.AUTO
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
        self.page.on_resized = self.resize

        self.place_item()


    def place_item(self):

        """This method for place the signup page elements"""

        if self.device == "desktop":
            self.global_widgets.signup_widgets_repository.controls.append(
                self.global_widgets.change_them_button_container
            )

            self.page.add(self.global_widgets.main_container)
            self.page.update()
            self.page.run_task(self.animations)

    async def animations(self):
        """This method is responsible for apply animations to active widgets"""

        await asyncio.sleep(0.05)
        self.global_widgets.signup_container.opacity = 1
        self.global_widgets.signup_container.scale = 1
        self.page.update()

    def resize(self, e):
        self.global_widgets.main_container.height = self.page.height if (
            self.page.height > self.global_widgets.signup_container.height + self.global_widgets.main_container.padding) \
            else (self.global_widgets.signup_container.height + self.global_widgets.main_container.padding)

        self.page.update()
