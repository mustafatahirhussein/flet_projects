import flet
from flet import Row, icons, IconButton, TextField, Page;

def main(page: Page) :
    page.title = "Counter App"
    page.vertical_alignment = "center"

    tf =TextField(text_align="center",value="0", width=100)

    def minus(e) :
        tf.value = int(tf.value) -1
        page.update()

    def plus(e) :
        tf.value = int(tf.value) + 1
        page.update()

    page.add(
        Row([

            IconButton(icons.REMOVE, on_click=minus),
            tf,
            IconButton(icons.ADD, on_click=plus)
        ],
        alignment="center")
    )


flet.app(target=main,view=flet.WEB_BROWSER)