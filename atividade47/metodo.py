import flet as ft

def main(page: ft.Page):
    def acao(e):
        # Usando uma expressão ternária para verificar se a idade é um número
        verificacao = (
            'é maior de idade' if idade.value.isdigit() and int(idade.value) >= 18 
            else 'é menor de idade' if idade.value.isdigit() 
            else "Por favor, insira uma idade válida."
        )
        # Atualiza o resultado, considerando a verificação
        result.value = f'{nome.value} {verificacao}' if idade.value.isdigit() else "Por favor, insira uma idade válida."
        nome.value = ''
        idade.value = ''
        page.update()

    def ir_para_idade(e):
        idade.focus()  

    page.title = 'Maioridade'
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme_mode = ft.ThemeMode.LIGHT

    nome = ft.TextField(label='Nome', on_submit=ir_para_idade)
    idade = ft.TextField(label='Idade', suffix_text='anos', on_submit=acao)
    result = ft.Text(size=30)
    
    page.add(
        ft.Row(
            [ft.Text('Maioridade', size=40, weight=ft.FontWeight.BOLD)],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [nome],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [idade],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [ft.ElevatedButton('Calcular maioridade', on_click=acao)],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [result],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    
    page.update()

ft.app(main)
