import flet as ft
import asyncio
from ui.them import light, dark

class Signin:
    def __init__(self, page: ft.Page):
        self.page = page

        # set window settings
        self.page.title = "کریپتو بانک"
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.padding = 0
        # self.page.on_resized = self.resize
        self.page.theme_mode = ft.ThemeMode.SYSTEM
        self.colors = dark.DARK_THEM if self.page.platform_brightness.value == "dark" else light.LIGHT_THEM
        self.page.on_platform_brightness_change = self.change_them
        self.page.window.maximized = True
        self.page.update()

        # place item
        self.widgets()

    def widgets(self):
        # create background
        self.background_gradient = ft.RadialGradient(
            colors=self.colors["main_background"]["background_colors"],
            center=ft.alignment.top_left,
            radius=self.colors["main_background"]["radius"]
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

        )

        self.signup_column = ft.Column(
            controls=[self.signup_container]
        )

        self.main_container = ft.Container(
            padding=ft.padding.symmetric(vertical=30),
            gradient=self.background_gradient,
            alignment=ft.alignment.center,
            content=self.signup_column,
            expand=True
        )

        self.build_signup_form()

    def build_signup_form(self):

        self.change_them_button = ft.IconButton(
            icon=ft.Icons.NIGHTLIFE
        )

        self.signup_widgrts = ft.Column(
            controls=[]
        )

        self.place_item()

    def place_item(self):
        if self.page.width > 1200 and self.page.height > 650:
            self.page.add(self.main_container)
            self.page.run_task(self.animations)

    async def animations(self):
        await asyncio.sleep(0.05)
        self.signup_container.opacity = 1
        self.signup_container.scale = 1
        self.page.update()

    def change_them(self, e):
        if self.colors != self.page.theme_mode.SYSTEM:
            self.colors = dark.DARK_THEM if self.page.platform_brightness.value == "dark" else light.LIGHT_THEM
            self.background_gradient.colors = self.colors["main_background"]["background_colors"]
            self.background_gradient.radius = self.colors["main_background"]["radius"]

            self.signup_container.bgcolor = self.colors["signup_container"]["bgcolor"]
            self.signup_container.border = self.colors["signup_container"]["border"]
            self.page.update()

