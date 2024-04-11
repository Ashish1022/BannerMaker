import flet
from flet import *
from header import AppHeader
from form import AppForm
from data_table import AppDataTable
from btn import banner_without_offset



def main(page :Page):
    page.bgcolor = "#dfdfdf"
    page.padding = 20
    page.window_full_screen = True
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                
                Divider(height=2,color='transparent'),
                AppForm(),
                Divider(height=2,color='transparent'),
                Column(
                    scroll='hidden',
                    expand=True,
                    controls=[
                        AppDataTable(),
                    ]
                ),
                Divider(height=2,color='transparent'),
                ElevatedButton(
                    on_click=lambda e: banner_without_offset(),
                    bgcolor='#081d33',
                    color='white',
                    content=Row(
                        controls=[
                            Icon(
                                name=icons.ADD_ROUNDED,
                                size=12,
                            ),
                            Text(
                                "Make Banner",
                                size=11,
                                weight='bold'
                            ),
                        ],
                    ),
                    style=ButtonStyle(
                        shape={
                            "":RoundedRectangleBorder(radius=6),
                        },
                        color={
                            "":'white',
                        },
                    ),
                    height=42,
                    width=220,
                ),

            ],
        )
    )
    page.update()
    pass

if __name__ == "__main__":
    flet.app(target=main)