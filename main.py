from kivy.app import App
from kivy.lang import Builder
from telas import *
import webbrowser
from botoes import *
import requests
import os
import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()

GUI = Builder.load_file('main.kv')

class PerfilEnergia(App):
    def build(self):
        return GUI

    def mudar_tela(self, id_site):
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_site
        site = "https://perfil-energia.modelovencedor.com/login"
        webbrowser.open_new(site)
        botao = Button(on_release=abrir_site)



PerfilEnergia().run()