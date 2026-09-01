import flet as ft



def main(page: ft.Page):
  page.title = 'ParOuImpar'
  page.vertical_alignment = ft.MainAxisAlignment.CENTER
  input = ft.TextField(label='value' ,hint_text="digite um numero inteiro", autofocus= True)
  result = ft.Column(alignment=ft.MainAxisAlignment.CENTER, spacing=10, height=200, width=200,scroll=ft.ScrollMode.ALWAYS,scroll_interval=0)
  
  
  def addHistory(e):
    if input.value:
      num = int(input.value.strip())
      input.value = ''
      input.update()
      if num % 2 == 0:
        res = f'{num} é par'
        result.controls.append(ft.Text(res))
        result.update()
      else:
        res = f'{num} é impar'
        result.controls.append(ft.Text(res))
        result.update()
  
              
  btn = ft.IconButton(ft.Icons.ADD, on_click=(addHistory))          
  
  inputRow = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[input, btn])
  resultRow = ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[result])
  
  page.add( 
  inputRow,
  resultRow
)
  
  
  
if __name__ == '__main__' :
  ft.run(main)
  