import flet as ft
from ui.them.signup.desktop import dark_signup_D, light_signup_D, styles_signup_D
from ui.them.signup.mobile_tablet import dark_signup_MT, light_signup_MT, style_signup_MT
from ui.them.signup.global_ import dark_signup_G, light_signup_G, style_signup_G
import database.json.code.signup.signup_base_data as signup_base_data

class GlobalSignupWidgets:
    def __init__(self, page: ft.Page, styles, global_styles):
        """Initializes global signup widgets based on the system color mode (dark or light)"""

        self.page = page
        if signup_base_data.reade()["user_device"] == "desktop":
            self.colors = dark_signup_D.DARK_SIGNUP_D if signup_base_data.reade()["color_mode"] == "dark" else light_signup_D.LIGHT_SIGNUP_D
        else:
            self.colors = dark_signup_MT.DARK_SIGNUP_MT if signup_base_data.reade()["color_mode"] == "dark" else light_signup_MT.LIGHT_SIGNUP_MT
        self.global_colors = dark_signup_G.DARK_SIGNUP_G if signup_base_data.reade()["color_mode"] == "dark" else light_signup_G.LIGHT_SIGNUP_G
        self.styles = styles
        self.global_styles = global_styles


        self.base_widgets()

    def signup_widgets(self):
        """In this method create the all signup page"""

        self.change_them_button = ft.Icon(
            name=self.global_colors["change_them_button"]["button"]["icon"],
            color=self.global_colors["change_them_button"]["button"]["icon_color"],
            size=self.global_styles["change_them_button"]["button"]["icon_size"]
        )

        self.change_them_button_container = ft.Container(
            width=self.styles["change_them_button"]["container"]["width"],
            height=self.styles["change_them_button"]["container"]["height"],
            scale=self.global_styles["change_them_button"]["container"]["scale"],
            bgcolor=self.colors["change_them_button"]["container"]["bgcolor"],
            border=self.colors["change_them_button"]["container"]["border"],
            border_radius=self.styles["change_them_button"]["container"]["border_radius"],
            content=self.change_them_button,
            animate_scale=self.global_styles["change_them_button"]["container"]["animate_scale_rotate"],
            animate_rotation=self.global_styles["change_them_button"]["container"]["animate_scale_rotate"],

            on_hover=lambda e:
            styles_signup_D.StyleSignupDesktop.change_them_button_container_hover(self.colors, self.page, e)
            if signup_base_data.reade()["user_device"] == "desktop" else None,
            on_click=self.change_them
        )

    def base_widgets(self):
        """
        This method builds the base and global UI widgets for the signup page
        This method builds the background and layout containers for the signup page
        """
        self.signup_widgets_repository = ft.Column(controls=[])

        self.background = ft.LinearGradient(
            colors=self.global_colors["main_container"]["gradient_color"],
            begin=self.global_styles["background"]["begin"],
            end=self.global_styles["background"]["end"]
        )

        self.signup_container = ft.Container(
            width=self.global_styles["signup_container"]["width"],
            height=self.styles["signup_container"]["height"],
            border_radius=self.global_styles["signup_container"]["border_radius"],
            padding=self.styles["signup_container"]["padding"],
            opacity=self.global_styles["signup_container"]["opacity"],
            scale=self.global_styles["signup_container"]["scale"],
            bgcolor=self.global_colors["signup_container"]["bgcolor"],
            border=self.global_colors["signup_container"]["border"],
            blur=self.global_styles["signup_container"]["blur"],
            animate_opacity=self.global_styles["signup_container"]["animate"],
            animate_scale=self.global_styles["signup_container"]["animate"],
            content=self.signup_widgets_repository
        )

        self.main_container_elements_repository = ft.Column(
            controls=[self.signup_container],
            alignment=self.global_styles["main_container_elements_repository"]["alignment"],
            scroll=self.global_styles["main_container_elements_repository"]["scroll"]
        )

        self.main_container = ft.Container(
            padding=ft.padding.symmetric(
                self.styles["main_container"]["padding"]["vertical"],
                self.styles["main_container"]["padding"]["horizontal"]
            ),
            content=self.main_container_elements_repository,
            expand=True
        )

        self.background_container_elements_repository = ft.Stack(controls=[self.main_container])

        self.background_container = ft.Container(
            gradient=self.background,
            alignment=ft.alignment.center_right,
            content=self.background_container_elements_repository,
            expand=True,
            animate=500
        )

        self.signup_widgets()

    def change_them(self, e):
        """This method is responsible for change app them(light, dark)"""
        def update_global_widgets_colors():
            self.background.colors = self.global_colors["main_container"]["gradient_color"]

            self.signup_container.bgcolor = self.global_colors["signup_container"]["bgcolor"]
            self.signup_container.border = self.global_colors["signup_container"]["border"]

            self.change_them_button.name = self.global_colors["change_them_button"]["button"]["icon"]
            self.change_them_button.color = self.global_colors["change_them_button"]["button"]["icon_color"]
            self.update_widgets_colors_by_user_device(e)
        #=====UPDATE (color_mode) KEY FROM JSON FILE TO UPDATE COLORS DICTIONARY=====
        if e.name == "platformBrightnessChange":
            signup_base_data.insert(e.data, e.data, signup_base_data.reade()["user_device"], signup_base_data.reade()["last_device"])
        elif e.name == "click":
            signup_base_data.insert(
                them_mode="dark" if signup_base_data.reade()["color_mode"] == "light" else "light",
                color_mode="dark" if signup_base_data.reade()["color_mode"] == "light" else "light",
                user_device=signup_base_data.reade()["user_device"],
                last_device=signup_base_data.reade()["last_device"]
            )
        #============== FINISH UPDATE (color_mode) KEY FROM JSON FILE ===============
        #====================== UPDATE COLORS DICTIONARY =======================
        self.global_colors = dark_signup_G.DARK_SIGNUP_G if signup_base_data.reade()["color_mode"] == "dark" else light_signup_G.LIGHT_SIGNUP_G
        if signup_base_data.reade()["user_device"] == "desktop":
            self.colors = dark_signup_D.DARK_SIGNUP_D if signup_base_data.reade()["color_mode"] == "dark" else light_signup_D.LIGHT_SIGNUP_D
        else:
            self.colors = dark_signup_MT.DARK_SIGNUP_MT if signup_base_data.reade()["color_mode"] == "dark" else light_signup_MT.LIGHT_SIGNUP_MT
       #=====================FINISH UPDATE COLORS DICTIONARY=====================
        #======================UPDATE ACTIVE WIDGETS COLORS======================
        if e.name == "resized":
            self.update_widgets_colors_by_user_device(e)
        update_global_widgets_colors()
        # ===================FINISH UPDATE ACTIVE WIDGETS COLORS==================

    def update_widgets_colors_by_user_device(self, e):
        # if signup_base_data.reade()["user_device"] == "desktop":
        self.change_them_button_container.bgcolor = self.colors["change_them_button"]["container"]["bgcolor"]
        self.change_them_button_container.border = self.colors["change_them_button"]["container"]["border"]
        if e.name != "resized":
            self.page.update()