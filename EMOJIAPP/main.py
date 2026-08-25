import flet as ft

EMOJIS = ['😀','😃','😄','😁','😆','😅','🤣']

IDX = 0 


def main(page: ft.Page):
    page.title = 'EmojiApp'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    input = ft.Text(value=EMOJIS[0])
    
    # refreshes the app
    def refresh_click(e):
        global IDX
        icon = e.control.icon
        if icon == ft.Icons.ARROW_RIGHT_SHARP:
            print('right')
            IDX = (IDX + 1) 
        else:
            print('left')
            IDX = (IDX - 1)
        IDX = IDX % len(EMOJIS)
        input.value = EMOJIS[IDX]
        
    # different buttons for moving the index left and right
    btn_left = ft.IconButton(ft.Icons.ARROW_LEFT_SHARP, on_click=refresh_click)
    btn_right = ft.IconButton(ft.Icons.ARROW_RIGHT_SHARP, on_click=refresh_click)
    
    # the singular row of the app
    row = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER, 
        controls=[
            btn_left,
            input,
            btn_right
        ]
    )
    page.add(row)
    
if __name__ == '__main__' :
    ft.run(main)
    