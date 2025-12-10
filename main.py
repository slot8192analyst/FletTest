import os
import flet as ft

def main(page: ft.Page):
    page.title = "My Flet App"
    page.add(ft.Text("Hello, Flet on Web!"))

if __name__ == "__main__":
    # Render や Railway では PORT 環境変数にポート番号が入ることが多い
    port = int(os.environ.get("PORT", 8080))

    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,  # ブラウザで開く
        port=port,
        host="0.0.0.0"                # 外部からアクセスできるように
    )
