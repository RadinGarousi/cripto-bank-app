import flet as ft
from ui.pages.signup.main_signup import MainSignup

def main(page: ft.Page):
    MainSignup(page)

if __name__=="__main__":
    ft.app(target=main, assets_dir="assets")