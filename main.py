import flet as ft
from ui.pages.signin.main_signin import Signin

def main(page: ft.Page):
    Signin(page)

if __name__=="__main__":
    ft.app(target=main)