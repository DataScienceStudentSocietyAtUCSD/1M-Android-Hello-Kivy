import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder

kv = '''
Label:
    text: "Hello World"
'''

class TestApp(App):
   def build(self):
          return Builder.load_string(kv)
if __name__ == '__main__':
   TestApp().run()
