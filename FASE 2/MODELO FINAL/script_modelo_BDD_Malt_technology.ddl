CREATE TABLE analista (
    id_analista     INTEGER NOT NULL,
    nombre_analista VARCHAR2(50)
);

ALTER TABLE analista ADD CONSTRAINT analista_pk PRIMARY KEY ( id_analista );

CREATE TABLE cliente (
    id_cliente     INTEGER NOT NULL,
    nombre_cliente VARCHAR2(60)
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( id_cliente );

CREATE TABLE estado (
    id_estado   INTEGER NOT NULL,
    tipo_estado VARCHAR2(60)
);

ALTER TABLE estado ADD CONSTRAINT estado_pkv2 PRIMARY KEY ( id_estado );

CREATE TABLE estado_tina (
    id_estado_tina INTEGER NOT NULL,
    descripcion    VARCHAR2(60)
);

ALTER TABLE estado_tina ADD CONSTRAINT estado_pk PRIMARY KEY ( id_estado_tina );

CREATE TABLE info_analisis (
    batch               INTEGER NOT NULL,
    id_estado           INTEGER NOT NULL,
    id_tipo_malta       INTEGER NOT NULL,
    fecha_produccion    DATE,
    fecha_analisis      DATE,
    id_cliente          INTEGER NOT NULL,
    id_tipo_horno       INTEGER NOT NULL,
    proceso_tag         CHAR(2),
    id_variedad         INTEGER NOT NULL,
    silo_origen         VARCHAR2(80),
    silo_destino_1      VARCHAR2(40),
    malta_limpia        INTEGER,
    humedad             FLOAT(8),
    tipo_sacarificacion FLOAT(8),
    ext_fino_ss         FLOAT(8),
    ext_gru_ss          FLOAT(8),
    fan                 FLOAT(8),
    id_analista         INTEGER NOT NULL
);

CREATE UNIQUE INDEX info_analisis__idx ON
    info_analisis (
        batch
    ASC );

ALTER TABLE info_analisis ADD CONSTRAINT info_analisis_pk PRIMARY KEY ( batch );

CREATE TABLE info_germinacion (
    cod_germinacion INTEGER NOT NULL,
    batch           INTEGER NOT NULL,
    tbhorno         VARCHAR2(50),
    hora            INTEGER,
    tshorno         INTEGER,
    presionbhorno   INTEGER,
    abertura        INTEGER,
    tcontrol        INTEGER,
    tretorno        INTEGER
);

ALTER TABLE info_germinacion ADD CONSTRAINT info_germinacion_pk PRIMARY KEY ( cod_germinacion,
                                                                              batch );

CREATE TABLE info_horno (
    batch               INTEGER NOT NULL,
    fecha               DATE NOT NULL,
    variedad            VARCHAR2(40),
    temp_sobre_grano    FLOAT(5),
    temp_bajo_tela      FLOAT(5),
    temp_ambiente       FLOAT(5),
    hr_sobre_tela       FLOAT(5),
    p_apertura_damper   FLOAT(5),
    presion_diferencial INTEGER,
    gas_total           INTEGER,
    gas_et_1            INTEGER,
    gas_et_2            INTEGER,
    gas_et_3            INTEGER,
    gas_et_4            INTEGER,
    gas_et_5            INTEGER,
    gas_et_6            INTEGER,
    tiempo_total        INTEGER,
    tiempo_barra_e1     INTEGER,
    tiempo_barra_e2     INTEGER,
    tiempo_barra_e3     INTEGER,
    tiempo_barra_e4     INTEGER,
    tiempo_barra_e5     INTEGER,
    tiempo_barra_e6     INTEGER,
    sp_temp_1           INTEGER,
    sp_temp_2           INTEGER,
    sp_temp_3           INTEGER,
    sp_temp_4           INTEGER,
    sp_temp_5           INTEGER,
    sp_temp_6           INTEGER
);

ALTER TABLE info_horno ADD CONSTRAINT info_horno_pk PRIMARY KEY ( fecha,
                                                                  batch );

CREATE TABLE info_produccion (
    batch                            INTEGER NOT NULL,
    id_tipo_malta                    INTEGER NOT NULL,
    id_tipo_horno                    INTEGER NOT NULL,
    fecha_horneo                     DATE NOT NULL,
    tipo_variedad                    VARCHAR2(60) NOT NULL,
    cebada_limpia                    FLOAT(8),
    cebada_sucia                     FLOAT(8),
    falla                            INTEGER,
    impureza                         INTEGER,
    polvo                            INTEGER,
    malta_sucia                      INTEGER,
    brote                            INTEGER,
    pijilla_malta                    INTEGER,
    malta_limpia                     INTEGER,
    malta_verde                      INTEGER,
    materiaseca                      INTEGER,
    fecha_volteo                     DATE,
    fecha_pulido                     DATE,
    silo_destino_1                   VARCHAR2(60),
    kg_destino_1                     INTEGER,
    silo_destino_2                   VARCHAR2(60),
    kg_destino_2                     INTEGER,
    electricidad                     INTEGER,
    agua                             INTEGER,
    gas                              INTEGER,
    cs_ci                            FLOAT(6),
    ci_mi                            FLOAT(6),
    "cs/ml"                          FLOAT(6),
    "ms/ml"                          FLOAT(6),
    "brote/ml"                       FLOAT(6),
    factor_perdida_humedad           FLOAT(8),
    factor_perdida_conversion        FLOAT(8),
    kg_perdida_humedad               INTEGER,
    kg_perdida_conversion            INTEGER,
    factor_carbon                    FLOAT(8),
    factor_electricidad              FLOAT(8),
    factor_agua                      FLOAT(8), 
    info_germinacion_cod_germinacion INTEGER,
    info_horno_fecha                 DATE,
    info_tina_cod_tina               INTEGER
);

CREATE UNIQUE INDEX info_produccion__idx ON
    info_produccion (
        batch
    ASC );

ALTER TABLE info_produccion ADD CONSTRAINT info_produccion_pk PRIMARY KEY ( batch );

CREATE TABLE info_tina (
    cod_tina       INTEGER NOT NULL,
    batch          INTEGER NOT NULL,
    fecha          DATE,
    hora           VARCHAR2(8),
    temptina1      INTEGER,
    temptina2      INTEGER,
    id_estado_tina INTEGER NOT NULL
);

ALTER TABLE info_tina ADD CONSTRAINT info_tina_pk PRIMARY KEY ( cod_tina,
                                                                batch );

CREATE TABLE tipo_horno (
    id_tipo_horno INTEGER NOT NULL,
    nombre_horno  VARCHAR2(20)
);

ALTER TABLE tipo_horno ADD CONSTRAINT tipo_horno_pk PRIMARY KEY ( id_tipo_horno );

CREATE TABLE tipo_malta (
    id_tipo_malta INTEGER NOT NULL,
    nombre_malta  VARCHAR2(60)
);

ALTER TABLE tipo_malta ADD CONSTRAINT tipo_malta_pk PRIMARY KEY ( id_tipo_malta );

CREATE TABLE variedad (
    id_variedad INTEGER NOT NULL,
    descripcion VARCHAR2(60)
);

ALTER TABLE variedad ADD CONSTRAINT variedad_pk PRIMARY KEY ( id_variedad );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_analista_fk FOREIGN KEY ( id_analista )
        REFERENCES analista ( id_analista );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_cliente_fk FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado ( id_estado );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_info_produccion_fk FOREIGN KEY ( batch )
        REFERENCES info_produccion ( batch );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_tipo_horno_fk FOREIGN KEY ( id_tipo_horno )
        REFERENCES tipo_horno ( id_tipo_horno );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_tipo_malta_fk FOREIGN KEY ( id_tipo_malta )
        REFERENCES tipo_malta ( id_tipo_malta );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_variedad_fk FOREIGN KEY ( id_variedad )
        REFERENCES variedad ( id_variedad );


ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_info_germinacion_fk FOREIGN KEY ( info_germinacion_cod_germinacion,
                                                                     batch )
        REFERENCES info_germinacion ( cod_germinacion,
                                      batch );

ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_info_horno_fk FOREIGN KEY ( info_horno_fecha,
                                                               batch )
        REFERENCES info_horno ( fecha,
                                batch );

ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_info_tina_fk FOREIGN KEY ( info_tina_cod_tina,
                                                              batch )
        REFERENCES info_tina ( cod_tina,
                               batch );

ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_tipo_horno_fk FOREIGN KEY ( id_tipo_horno )
        REFERENCES tipo_horno ( id_tipo_horno );

ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_tipo_malta_fk FOREIGN KEY ( id_tipo_malta )
        REFERENCES tipo_malta ( id_tipo_malta );

ALTER TABLE info_tina
    ADD CONSTRAINT info_tina_estadov1_fk FOREIGN KEY ( id_estado_tina )
        REFERENCES estado_tina ( id_estado_tina );