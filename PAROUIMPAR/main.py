import flet as ft

HISTORY = []


def main(page: ft.Page):
    page.title = 'ParOuImpar'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    input = ft.TextField(label='value' ,hint_text="digite um numero inteiro")
    result = ft.Column(alignment=ft.MainAxisAlignment.CENTER)
    
    
    def addHistory(e):
        HISTORY.append(input.value)
    
                
    btn = ft.IconButton(ft.Icons.ADD, on_click=(addHistory))          
    
    page.add(
        ft.Row(ft.MainAxisAlignment.CENTER, controls=[input,btn]),
        ft.Row(alignment=ft.MainAxisAlignment.CENTER,controls=[result])

        
    )
    
    
    
if __name__ == '__main__' :
    ft.run(main)
    