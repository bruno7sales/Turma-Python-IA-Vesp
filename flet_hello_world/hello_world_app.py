import flet as ft 

def main(page: ft.Page):
    page.title = "Olá, mundo!"
    page.scroll = "adaptive"

# Declaração de Variaveis
    nome = ft.TextField(label= "Nome")

    page.add(
        ft.Text("Olá, Mundo (De novo)!", size= 16, font_family= "Times New Roman", color= "blue"),
        nome,
        ft.TextButton("Clique aqui!")
    )

    page.update()

ft.app(main)