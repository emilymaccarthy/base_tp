import random
from faker import Faker
from td7.custom_types import Records

class DataGenerator:
    def __init__(self):
        self.fake = Faker("es_AR")

    def generate_people(self, n: int) -> Records:
        people = []
        for _ in range(n):
            people.append({
                "first_name": self.fake.unique.first_name(),
                "last_name": self.fake.unique.last_name(),
                "date_of_birth": self.fake.unique.date_of_birth(),
                "passport_number": self.fake.unique.passport_number(),
                "dni": self.fake.unique.random_int(min=10_000_000, max=55_000_000),
                "genero": random.choice(["M", "F", "O"]),
                "educacion": random.choice(["sin estudios","primaria","secundaria","universitaria","posgrado"]),
            })
        return people

    def generate_religiones(self) -> Records:
        return [
            {
                "nombre_religion": "Cristianismo",
                "teismo": "monoteista",
                "tiene_clero": True,
                "tiene_lugares_sagrados": True,
                "tiene_libros": True,
                "clasificacion_temporal": "antigua"
            },
            {
                "nombre_religion": "Islam",
                "teismo": "monoteista",
                "tiene_clero": True,
                "tiene_lugares_sagrados": True,
                "tiene_libros": True,
                "clasificacion_temporal": "medieval"
            },
            {
                "nombre_religion": "Judaísmo",
                "teismo": "monoteista",
                "tiene_clero": True,
                "tiene_lugares_sagrados": True,
                "tiene_libros": True,
                "clasificacion_temporal": "antigua"
            },
            {
                "nombre_religion": "Hinduismo",
                "teismo": "politeista",
                "tiene_clero": True,
                "tiene_lugares_sagrados": True,
                "tiene_libros": True,
                "clasificacion_temporal": "antigua"
            },
            {
                "nombre_religion": "New Age",
                "teismo": "no tiene",
                "tiene_clero": False,
                "tiene_lugares_sagrados": False,
                "tiene_libros": False,
                "clasificacion_temporal": "contemporánea"
            }
        ]
        
    def generate_frecuencia(self) -> Records:
        return [
            {
                "id_frecuencia": "1",
                "valor": "Nunca"
            },
            {
                "id_frecuencia": "2",
                "valor": "Menos de una vez al año"
            },
            {
                "id_frecuencia": "3",
                "valor": "Una vez al año"
            },
            {
                "id_frecuencia": "4",
                "valor": "Dos o más veces al año"
            },
            {
                "id_frecuencia": "5",
                "valor": "Una vez al mes"
            },
            {
                "id_frecuencia": "6",
                "valor": "Dos o más veces al mes"
            },
            {
                "id_frecuencia": "7",
                "valor": "Una vez a la semana"
            },
            {
                "id_frecuencia": "8",
                "valor": "Dos o más veces a la semana"
            },
            {
                "id_frecuencia": "9",
                "valor": "Una vez al día"
            },
            {
                "id_frecuencia": "10",
                "valor": "Dos o más veces por día"
            }
        ]
    
    def generate_encuestas(self, people: list, religiones: list, frecuencia: list, n: int) -> Records:
        encuestas = []
        for i in range(n):
            person = random.choice(people)
            religion = random.choice(religiones)["nombre_religion"]
            frecuencia_elegida = random.choice(frecuencia)
            encuestas.append({
                "dni_encuestado": person["dni"],
                "id_encuesta": i + 1,
                "telefono_operador": self.fake.random_int(min=1100000000, max=1199999999),
                "telefono_encuestado": self.fake.random_int(min=1100000000, max=1199999999),
                "fecha": self.fake.date_between(start_date='-5y', end_date='today'),
                "tipo_creencia": random.choice(['religioso', 'espiritual', 'religioso y espiritual', 'ninguna']),
                "tipo_creyente": random.choice(['por tradición', 'por convicción', 'no practicante', 'no creyente']),
                "se_siente_parte_de_religion": random.choice(['si', 'no', 'no estoy seguro']),
                "se_identifica_con_religion": random.choice(['si', 'no', 'no estoy seguro']),
                "grado_espiritualidad": self.fake.random_int(min=0, max=10),
                "grado_religiosidad": self.fake.random_int(min=0, max=10),
                "cambio_de_religion": self.fake.boolean(),
                "dejo_de_creer": self.fake.boolean(),
                "familia_comparte_religion": self.fake.boolean(),
                "sufrio_discriminacion": self.fake.boolean(),
                "razon_abandono": self.fake.sentence(),
                "importancia_seres_supremos": self.fake.text(max_nb_chars=100),
                "importancia_poder_espiritual_personal": self.fake.text(max_nb_chars=100),
                "importancia_santos": self.fake.text(max_nb_chars=100),
                "importancia_energia": self.fake.text(max_nb_chars=100),
                "opinion_relaciones_genero": self.fake.text(max_nb_chars=100),
                "opinion_familia": self.fake.text(max_nb_chars=100),
                "impacto_pandemia": self.fake.text(max_nb_chars=100),
                "frecuencia_asistencia_lugares_religiosos": frecuencia_elegida["id_frecuencia"],
                "frecuencia_experiencias_religiosas": frecuencia_elegida["id_frecuencia"],
                "frecuencia_tv_religiosa": frecuencia_elegida["id_frecuencia"],
                "frecuencia_lectura_sagrada": frecuencia_elegida["id_frecuencia"],
                "nombre_religion_actual": religion
            })
        return encuestas
    
    
 
