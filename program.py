import os
import json

class Program():
    def __init__(self, filename):
        self.filename = filename
        self.running: bool = True
        self.menues: dict = {}
        self.in_submenu: bool = False
        self.submenu_id = 1

    def init(self):
        self.clear()
        self.load_menues()
        while self.running:
            self.display()
            self.events()
            self.clear()

    def events(self):
        command = input('> ').lower()
        if command == 's':
            self.running = False
        
    def clear(self):
        os.system('cls')

    def display(self):
        if not self.in_submenu:
            for key, value in enumerate(self.menues):
                print(f"""
                {self.menues[value]['name']}
                {key} - {self.menues[value]['description']}
                """)
        else:
            for key, value in enumerate(self.menues):
                print(f"""
                {self.menues[value]['submenu']['name']}
                {key} - {self.menues[value]['submenu']['description']}
                """)

    def load_menues(self):
        with open(self.filename, 'r') as file:
            data = json.load(file)
            self.menues = data['menu']