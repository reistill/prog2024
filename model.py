from config import *

class Animal(db.Entity):
    nome = Required(str)
    alimentacao = Required(str)
    sexo = Required(str)
    idade = Required(str)
    especie = Required(str)
    def __str__(self):
        return f'{self.nome}, {self.alimentacao}, {self.sexo}, {self.idade}, {self.especie}'

db.bind(provider='sqlite', filename='animal.db', create_db=True)
db.generate_mapping(create_tables=True)