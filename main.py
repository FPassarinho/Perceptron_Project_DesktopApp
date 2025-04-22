import eel

eel.init('view')  # 'web' is the folder with your HTML files

@eel.expose
def say_hello_py(x):
  print(f"Hello from JS: {x}")

eel.start('index.html')
