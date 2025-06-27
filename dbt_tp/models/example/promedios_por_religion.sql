{{ config(materialized='view') }}

select
    nombre_religion,
    avg(grado_espiritualidad) as promedio_espiritualidad,
    avg(grado_religiosidad) as promedio_religiosidad,
    count(*) as cantidad_encuestas
from {{ ref('encuestas_totales') }}
group by nombre_religion
order by cantidad_encuestas desc
