import os

class Delete:
    def __init__(self, weapons_data):
        self.weapons_data = weapons_data

    def delete(self, index):
        if 0 <= index < len(self.weapons_data):
            del self.weapons_data[index]
            self.update_file()

    def update_file(self):
        file_path = os.path.join(os.path.dirname(__file__), 'list_data.txt')
        with open(file_path, 'w') as file:
            for weapon in self.weapons_data:
                file.write(';'.join(weapon) + '\n')
