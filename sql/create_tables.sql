-- pensar en los on delete cascade, los not null 
-------------------- Armado del database ------------------------------
-- opciones limitadas predefinidas 


CREATE TABLE Persona (
  dni INT PRIMARY KEY,
  nombre TEXT,
  apellido TEXT,
  genero genero_enum,
  nacimiento DATE,
  educacion educacion_enum,
  -- constraint
  constraint nacimiento_valido CHECK(nacimiento < CURRENT_DATE)
);


create table Frecuencia (
	id_frecuencia int primary key, 
	valor text not null 
);


create table Religion (
	nombre_religion text primary key, 
	teismo teismo, 
	tiene_clero boolean, 
	clasificacion_temporal clasi_temporal
);


create table Encuesta (
	id_encuesta INT,  
	dni_encuestado INT NOT NULL,
	fecha DATE NOT NULL,
    tel_operador BIGINT NOT NULL,
  	tel_encuestado BIGINT NOT NULL,
  	tipo_creencia tipo_creencia_enum NOT NULL,
  	tipo_creyente tipo_creyente_enum NOT NULL,
  	se_siente_parte_de_religion si_no_no_estoy_seguro NOT NULL,
  	se_identifica_con_religion si_no_no_estoy_seguro NOT NULL,
  	grado_espiritualidad INT NOT NULL,
  	grado_religiosidad INT NOT NULL,
	cambio_religion BOOLEAN NOT NULL,
	dejo_de_creer BOOLEAN NOT NULL,
	familia_comparte_religion BOOLEAN NOT NULL,
	sufrio_discriminacion BOOLEAN NOT NULL,
	importancia_seres_supremos TEXT NOT NULL,
	importancia_poder_espiritual_personal TEXT NOT NULL,
	importancia_santos TEXT NOT NULL,
	importancia_energia TEXT NOT NULL,
	opinion_relaciones_genero TEXT NOT NULL,
	opinion_estado_religion TEXT NOT NULL,
	opinion_familia TEXT NOT NULL,
	impacto_pandemia TEXT NOT NULL,
	frecuencia_asistencia_lugares_religiosos int NOT NULL,
	frecuencia_expericencias_religiosas int NOT NULL,
	frecuencia_tv_religiosa int NOT NULL,
	frecuencia_lectura_sagrada int NOT NULL,
	nombre_religion_actual TEXT NOT NULL,
	
	-- primary key 
	primary key (id_encuesta),
	
	-- Restricciones
	constraint fecha_encuesta_valida CHECK(fecha <= CURRENT_DATE),
	constraint grado_e_valido CHECK (grado_espiritualidad BETWEEN 0 AND 10),
	constraint grado_r_valido CHECK (grado_religiosidad BETWEEN 0 AND 10),
	
	-- Foreign Keys
	constraint fk_encuesta_a_persona foreign key (dni_encuestado) references Persona(dni) on delete cascade,
	constraint fk_encuesta_asistencia foreign key (frecuencia_asistencia_lugares_religiosos) references Frecuencia(id_frecuencia),
	constraint fk_encuesta_experiencia foreign key (frecuencia_expericencias_religiosas) references Frecuencia(id_frecuencia),
	constraint fk_encuesta_tv foreign key (frecuencia_tv_religiosa) references Frecuencia(id_frecuencia),
	constraint fk_encuesta_lectura foreign key (frecuencia_lectura_sagrada) references Frecuencia(id_frecuencia),
	constraint fk_nombre_religion_actual foreign key (nombre_religion_actual) references Religion(nombre_religion) 
);

