import ctypes
from typing import Container
import flet
from flet import TextField, icons, FloatingActionButton, Page, Checkbox, Column, Row

def main(page: Page) :
    page.title = "Todo Practice App"
    page.vertical_alignment = "center"


    def clicked(e) :

        ctypes.windll.user32.MessageBoxW(0, "Value is empty", "Message", 0) #just for test
        task_view.controls.append(Checkbox(label=task_field.value))
        task_field.value = ""
        task_view.update()

    task_field = TextField(hint_text="New Task...",expand=True)

    # to align the contents
    task_view = Column(
        controls=[
            Row(
                controls=[
                    task_field,
                    FloatingActionButton(text="Add",icon=icons.ADD, on_click=clicked),
                ]
            )
        ]
    )

    page.add(task_view)


flet.app(target=main)