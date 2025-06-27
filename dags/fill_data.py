from airflow import DAG
from airflow.operators.python import PythonOperator
import pendulum
from td7.data_generator import DataGenerator
from td7.schema import Schema

ENCUESTAS_POR_DIA = 100

def task_insertar_personas():
    generator = DataGenerator()
    schema = Schema()
    personas = generator.generate_people(100)
    schema.insert(personas, "persona")

def task_insertar_religiones():
    generator = DataGenerator()
    schema = Schema()
    religiones = generator.generate_religiones()
    schema.insert(religiones, "religion")
    
    #if len(religiones) == 0:
    #    religiones = generator.generate_religiones()
    #    schema.insert(religiones, "religion")
    #else:
    #    print("Ya existen religiones, no se inserta nada.")
    
def task_insertar_frecuencia():
    generator = DataGenerator()
    schema = Schema()
    frecuencia = generator.generate_frecuencia()
    schema.insert(frecuencia, "frecuencia")
    #if len(frecuencia) == 0:
    #    frecuencia = generator.generate_frecuencia()
    #    schema.insert(frecuencia, "frecuencia")
    #else:
    #    print("Ya existen religiones, no se inserta nada.")


def task_insertar_encuestas(base_time: str, n: int):
    generator = DataGenerator()
    schema = Schema()
    
    personas = schema.get_people(n)
    religiones = schema.get_religiones()
    frecuencia = schema.get_frecuencia()
    #religiones = generator.generate_religiones()
    #frecuencia = generator.generate_frecuencia()
    
    encuestas = generator.generate_encuestas(personas, religiones, frecuencia, n)
    schema.insert(encuestas, "encuesta")



with DAG(
    "fill_data",
    start_date=pendulum.datetime(2024, 6, 1, tz="UTC"),
    schedule_interval="@daily",
    catchup=True,
) as dag:

    insertar_personas = PythonOperator(
        task_id="insertar_personas",
        python_callable=task_insertar_personas
    )

    insertar_religiones = PythonOperator(
        task_id="insertar_religiones",
        python_callable=task_insertar_religiones
    )
    
    insertar_frecuencia = PythonOperator(
        task_id="insertar_frecuencia",
        python_callable=task_insertar_frecuencia
    )

    insertar_encuestas = PythonOperator(
        task_id="insertar_encuestas",
        python_callable=task_insertar_encuestas,
        op_kwargs=dict(n=ENCUESTAS_POR_DIA, base_time="{{ ds }}"),
    )
    
  

    [insertar_personas, insertar_religiones, insertar_frecuencia] >> insertar_encuestas
