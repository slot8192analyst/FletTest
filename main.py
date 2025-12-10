import os
import flet as ft

def main(page: ft.Page):
    page.title = "My Flet App"
    page.add(
        ft.Text("Hello, Flet on Web!"),
        ft.Image(src="70291.jpg", width=300, height=300)
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    ft.app(
        target=main,
        host="0.0.0.0",
        port=port,
        assets_dir="assets"
    )
