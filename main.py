import eel

eel.init('static_web_folder')  

@eel.expose
def say_hello_py(x):
  print(f"Hello from JS: {x}")

###Ver se ínicio como aplicação de Desktop ou web
eel.start('html/main_page.html', mode='chrome-app', port=8080, cmdline_args=['--start-fullscreen'])