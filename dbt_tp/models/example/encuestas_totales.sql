{{ config(materialized='table') }}

select
    e.id_encuesta,
    e.fecha,
    p.dni,
    p.nombre,
    p.apellido,
    p.genero,
    r.nombre_religion,
    r.teismo,
    r.clasificacion_temporal,
    f1.valor as asistencia_lugares,
    f2.valor as experiencia_religiosa,
    f3.valor as tv_religiosa,
    f4.valor as lectura_sagrada,
    e.grado_espiritualidad,
    e.grado_religiosidad
from {{ source('data_encuesta', 'encuesta') }} e
join {{ source('data_encuesta', 'persona') }} p on e.dni_encuestado = p.dni
join {{ source('data_encuesta', 'religion') }} r on e.nombre_religion_actual = r.nombre_religion
join {{ source('data_encuesta', 'frecuencia') }} f1 on e.frecuencia_asistencia_lugares_religiosos = f1.id_frecuencia
join {{ source('data_encuesta', 'frecuencia') }} f2 on e.frecuencia_expericencias_religiosas = f2.id_frecuencia
join {{ source('data_encuesta', 'frecuencia') }} f3 on e.frecuencia_tv_religiosa = f3.id_frecuencia
join {{ source('data_encuesta', 'frecuencia') }} f4 on e.frecuencia_lectura_sagrada = f4.id_frecuencia
