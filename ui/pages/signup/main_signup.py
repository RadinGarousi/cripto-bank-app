import flet as ft
import asyncio
from ui.them.signup.desktop import styles_signup_D
from ui.them.signup.mobile_tablet import style_signup_MT
from ui.them.signup.global_ import style_signup_G
from ui.pages.signup import mobile_tablet_signup, global_signup
import database.json.signup_base_data as signup_base_data
from utiles.detect_device import detect_device

class MainSignup:
    """
    This class is responsible for configuring window settings, placing signup page widgets responsively,
    applying animations to them and managing their color them
    """
    def __init__(self, page: ft.Page):
        """This method is responsible for configuring window settings and
        calling (place_item) method to place the signup page widgets"""
        # create state variables
        self.page = page
        self.last_device = ""
        self.animations_method_permission = False

        # set window settings
        # self.page.window.favicon = r"E:\python\cripto-bank-app\assets\loading-animation.png"
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.theme_mode = ft.ThemeMode.SYSTEM
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.window.maximized = True
        self.page.window.min_width = 520
        self.page.title = "Crypto Bank"
        self.page.padding = 0

        # Detecting the user's device by monitor resolution
        signup_base_data.insert("system", self.page.platform_brightness.value, detect_device(self.page), self.last_device, "ltr")
        self.last_device = signup_base_data.reade()["user_device"]

        self.styles = styles_signup_D.STYLE_SIGNUP_D if signup_base_data.reade()["user_device"] == "desktop" else style_signup_MT.STYLE_SIGNUP_MT
        self.global_styles = style_signup_G.STYLE_SIGNUP_G

        self.global_widgets = global_signup.GlobalSignupWidgets(self.page)
        self.mobile_tablet_widgets = mobile_tablet_signup.MobileSignupWidgets(self.page, self.global_styles)
        self.page.on_platform_brightness_change = self.global_widgets.change_them
        self.page.on_resized = self.resize
        self.place_item()

    def place_item(self):
        """This method for place the signup page elements"""

        self.page.add(self.global_widgets.background_container)

        if signup_base_data.reade()["user_device"] == "desktop":
            self.global_widgets.signup_widgets_repository.controls.append(
                self.global_widgets.change_them_button_container
            )
            if self.global_widgets.signup_container.height + self.styles["main_container"]["padding"]["vertical"] * 2 < self.page.height:
                self.global_widgets.main_container.height = self.page.height
        elif signup_base_data.reade()["user_device"] != "desktop":
            self.global_widgets.background_container_elements_repository.controls.append(self.mobile_tablet_widgets.appbar_column)
            self.global_widgets.main_container.height = self.page.height

        self.page.update()
        self.page.run_task(self.animations, "place_item")

    async def animations(self, e):
        """This method is responsible for apply animations to active widgets"""
        await asyncio.sleep(0.5)
        if e in ["place_item", "resized"]:
            self.global_widgets.signup_container.opacity = 1
            self.global_widgets.signup_container.scale = 1
            self.global_widgets.signup_container.offset = ft.Offset(0, 0)

            if signup_base_data.reade()["user_device"] != "desktop":
                self.mobile_tablet_widgets.appbar.opacity = 1
                self.mobile_tablet_widgets.appbar.scale = 1
                self.mobile_tablet_widgets.appbar.offset = ft.Offset(0, 0)
            self.animations_method_permission = False
            self.page.update()

    def resize(self, e):
        """this method is responsible for handling window responsiveness"""
        # Detect user device for best responsiveness
        signup_base_data.insert(
            them_mode="system" if signup_base_data.reade()["them_mode"] == "system"
            else "dark" if signup_base_data.reade()["them_mode"] == "dark" else "light",

            color_mode=self.page.platform_brightness.value if signup_base_data.reade()["them_mode"] == "system"
            else "dark" if signup_base_data.reade()["them_mode"] == "dark" else "light",

            user_device=detect_device(self.page),
            last_device=self.last_device
        )

        # update window widgets style
        #==================================UPDATE STYLES DICTIONARY=================================
        self.styles = styles_signup_D.STYLE_SIGNUP_D if signup_base_data.reade()["user_device"] == "desktop" else style_signup_MT.STYLE_SIGNUP_MT
        #===============================FINISH UPDATE STYLES DICTIONARY=============================
        #===============SET UP WIDGETS FOR SMALL AND LARGE DISPLAY(MOBILE AND TABLET)===============
        if signup_base_data.reade()["user_device"] == "desktop":
            if self.last_device != "desktop":
               self.global_widgets.background_container_elements_repository.controls.remove(self.mobile_tablet_widgets.appbar_column)
               self.global_widgets.signup_widgets_repository.controls.append(self.global_widgets.change_them_button_container)

        elif signup_base_data.reade()["user_device"] != "desktop":
            if self.last_device == "desktop":
                for _ in self.global_widgets.signup_widgets_repository.controls:
                    if _ in [self.global_widgets.change_them_button_container]:
                        self.global_widgets.signup_widgets_repository.controls.remove(self.global_widgets.change_them_button_container)
                self.global_widgets.background_container_elements_repository.controls.append(self.mobile_tablet_widgets.appbar_column)
        # update widgets style
        if self.last_device != signup_base_data.reade()["user_device"]:
            self.global_widgets.change_them_button_container.width = self.styles["change_them_button"]["container"]["width"]
            self.global_widgets.change_them_button_container.height = self.styles["change_them_button"]["container"]["height"]
            self.global_widgets.change_them_button_container.border_radius = self.styles["change_them_button"]["container"]["border_radius"]

            self.global_widgets.signup_container.height = self.styles["signup_container"]["height"]
            self.global_widgets.signup_container.padding = self.styles["signup_container"]["padding"]

            self.global_widgets.main_container.padding = ft.padding.symmetric(
                    self.styles["main_container"]["padding"]["vertical"],
                    self.styles["main_container"]["padding"]["horizontal"]
            )
            self.animations_method_permission = True
            self.global_widgets.change_them(e)
            # finish update widget style
        # ==============UPDATE MAIN_CONTAINER HEIGHT TO CROSS FULL GRADIENT BACKGROUND==============
        if signup_base_data.reade()["user_device"] == "desktop":
            if self.global_widgets.signup_container.height + self.styles["main_container"]["padding"]["vertical"] * 2 < self.page.height:
                self.global_widgets.main_container.height = self.page.height
            elif self.global_widgets.signup_container.height + self.styles["main_container"]["padding"]["vertical"] * 2 > self.page.height:
                self.global_widgets.main_container.height = self.global_widgets.signup_container.height + self.styles["main_container"]["padding"]["vertical"] * 2

        elif signup_base_data.reade()["user_device"] != "desktop":
            self.global_widgets.main_container.height = self.page.height
        # ============================FINISH UPDATE MAIN_CONTAINER HEIGHT============================
        #=====================FINISH SET UP WIDGETS FOR SMALL AND LARGE DISPLAY======================
        self.last_device = signup_base_data.reade()["user_device"]
        signup_base_data.insert(
            them_mode=signup_base_data.reade()["them_mode"],
            color_mode=signup_base_data.reade()["color_mode"],
            user_device=signup_base_data.reade()["user_device"],
            last_device=self.last_device
        )
        self.page.update()

        if self.animations_method_permission:
            self.page.run_task(self.animations, "resized")