import webview
import time
import os
from PySide6.QtWidgets import QApplication

class API:
    def run_model(self):
        # Replace this with your perceptron logic
        return "Perceptron model executed successfully!"

def maximize_window(window):
    time.sleep(0.5)

    app = QApplication([])
    screen = app.primaryScreen()
    size = screen.size()
    width = size.width()
    height = size.height()

    window.resize(width, height)
    window.move(0, 0)


if __name__ == '__main__':
    icon_path = os.path.abspath("client/img/favicon.ico")
    api = API()
    window = webview.create_window(
        title="MIND OF A PERCEPTRON",
        url="client/index.html",
        js_api=api,
        width=800,    
        height=600,   
        resizable=True, 
        fullscreen=False, 
        frameless=False   
    )
    webview.start(maximize_window, window, icon=icon_path, gui='qt')