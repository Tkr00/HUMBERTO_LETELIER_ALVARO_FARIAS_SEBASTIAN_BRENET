CREATE TABLE analista (
    id_analista     INTEGER NOT NULL,
    nombre_analista VARCHAR2(60) NOT NULL
);

ALTER TABLE analista ADD CONSTRAINT analista_pk PRIMARY KEY ( id_analista );

CREATE TABLE cliente (
    id_cliente     INTEGER NOT NULL,
    nombre_cliente VARCHAR2(60) NOT NULL
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( id_cliente );

CREATE TABLE estado (
    id_estado   INTEGER NOT NULL,
    tipo_estado  VARCHAR2(60) NOT NULL
);

ALTER TABLE estado ADD CONSTRAINT estado_pk PRIMARY KEY ( id_estado );

CREATE TABLE info_analisis (
    batch                    INTEGER NOT NULL,
    estado                   INTEGER NOT NULL,
    tipo_malta               INTEGER NOT NULL,
    fecha_produccion         DATE NOT NULL,
    fecha_analisis           DATE NOT NULL,
    cod_cliente              INTEGER NOT NULL,
    tipo_horno               INTEGER NOT NULL,
    proceso_tag              INTEGER NOT NULL,
    tipo_variedad            INTEGER NOT NULL,
    silo_origen               VARCHAR2(60) NOT NULL,
    silo_destino_1           VARCHAR2(40) NOT NULL,
    malta_limpia             INTEGER NOT NULL,
    humedad                  FLOAT(8) NOT NULL,
    tipo_sacarificacion      FLOAT(8) NOT NULL,
    ext_fino_ss              FLOAT(8) NOT NULL,
    ext_gru_ss               FLOAT(8) NOT NULL,
    fan                      FLOAT NOT NULL,
    estado_id_estado         INTEGER NOT NULL,
    cliente_id_cliente       INTEGER NOT NULL,
    analista_id_analista     INTEGER NOT NULL,
    tipo_malta_id_tipo_malta INTEGER NOT NULL,
    info_produccion_batch    INTEGER NOT NULL,
    variedad_id_variedad     INTEGER NOT NULL
);

CREATE UNIQUE INDEX info_analisis__idx ON
    info_analisis (
        info_produccion_batch
    ASC );

ALTER TABLE info_analisis ADD CONSTRAINT info_analisis_pk PRIMARY KEY ( batch );

CREATE TABLE info_germinacion (
    cod_germinacion INTEGER NOT NULL,
    descripcion      VARCHAR2(60) NOT NULL
);

ALTER TABLE info_germinacion ADD CONSTRAINT info_germinacion_pk PRIMARY KEY ( cod_germinacion );

CREATE TABLE info_horno (
    batch               INTEGER NOT NULL,
    fecha               DATE NOT NULL,
    variedad            VARCHAR2(40) NOT NULL,
    temp_sobre_grano    FLOAT(5) NOT NULL,
    temp_bajo_tela      FLOAT(5) NOT NULL,
    temp_ambiente       FLOAT(5) NOT NULL,
    hr_sobre_tela       FLOAT(5) NOT NULL,
    p_apertura_damper   FLOAT(5) NOT NULL,
    presion_diferencial INTEGER NOT NULL,
    gas_total           INTEGER NOT NULL,
    gas_et_1            INTEGER NOT NULL,
    gas_et_2            INTEGER NOT NULL,
    gas_et_3            INTEGER NOT NULL,
    gas_et_4            INTEGER NOT NULL,
    gas_et_5            INTEGER NOT NULL,
    gas_et_6            INTEGER NOT NULL,
    tiempo_total        INTEGER NOT NULL,
    tiempo_barra_e1     INTEGER NOT NULL,
    tiempo_barra_e2     INTEGER NOT NULL,
    tiempo_barra_e3     INTEGER NOT NULL,
    tiempo_barra_e4     INTEGER NOT NULL,
    tiempo_barra_e5     INTEGER NOT NULL,
    tiempo_barra_e6     INTEGER NOT NULL,
    sp_temp_1           INTEGER NOT NULL,
    sp_temp_2           INTEGER NOT NULL,
    sp_temp_3           INTEGER NOT NULL,
    sp_temp_4           INTEGER NOT NULL,
    sp_temp_5           INTEGER NOT NULL,
    sp_temp_6           INTEGER NOT NULL
);

ALTER TABLE info_horno ADD CONSTRAINT info_horno_pk PRIMARY KEY ( fecha,
                                                                  batch );

CREATE TABLE info_produccion (
    batch                            INTEGER NOT NULL,
    tipo_malta                       INTEGER NOT NULL,
    tipo_horno                       INTEGER NOT NULL,
    fecha_horneo                     DATE NOT NULL,
    tipo_variedad                    INTEGER NOT NULL,
    cebada_limpia                    FLOAT NOT NULL,
    cebada_sucia                     FLOAT NOT NULL,
    falla                            INTEGER NOT NULL,
    impureza                         INTEGER NOT NULL,
    polvo                            INTEGER NOT NULL,
    malta_sucia                      INTEGER NOT NULL,
    brote                            INTEGER NOT NULL,
    pijilla_malta                    INTEGER NOT NULL,
    malta_limpia                     INTEGER NOT NULL,
    malta_verde                      INTEGER NOT NULL,
    materiaseca                      INTEGER NOT NULL,
    fecha_volteo                     DATE NOT NULL,
    fecha_pulido                     DATE NOT NULL,
    silo_destino_1                   VARCHAR2(60) NOT NULL,
    kg_destino_1                     INTEGER NOT NULL,
    silo_destino_2                   VARCHAR2(60) NOT NULL,
    kg_destino_2                     INTEGER NOT NULL,
    electricidad                     INTEGER NOT NULL,
    agua                             INTEGER NOT NULL,
    gas                              INTEGER NOT NULL,
    cs_ci                            FLOAT(6) NOT NULL,
    ci_mi                            FLOAT(6) NOT NULL,
    "cs/ml"                          FLOAT(6) NOT NULL,
    "ms/ml"                          FLOAT(6) NOT NULL,
    "brote/ml"                       FLOAT(6) NOT NULL,
    factor_perdida_humedad           FLOAT(8) NOT NULL,
    factor_perdida_conversion        FLOAT(8) NOT NULL,
    kg_perdida_humedad               INTEGER NOT NULL,
    kg_perdida_conversion            INTEGER NOT NULL,
    factor_carbon                    FLOAT(8) NOT NULL,
    factor_electricidad              FLOAT(8) NOT NULL,
    factor_agua                      FLOAT(8) NOT NULL,
    tipo_malta_id_tipo_malta         INTEGER NOT NULL,
    info_analisis_batch              INTEGER NOT NULL,
    cod_germinacion                  INTEGER NOT NULL,
    cod_tina                         INTEGER NOT NULL,
    tipo_horno_id_tipo_horno         INTEGER NOT NULL, 
    info_germinacion_cod_germinacion INTEGER NOT NULL,
    info_horno_fecha                 DATE NOT NULL,
    info_horno_batch                 INTEGER NOT NULL,
    info_tina_cod_tina               INTEGER NOT NULL,
    id_usuario                       INTEGER NOT NULL,
    usuarios_id_usuario              INTEGER NOT NULL
);

CREATE UNIQUE INDEX info_produccion__idx ON
    info_produccion (
        info_analisis_batch
    ASC );

ALTER TABLE info_produccion ADD CONSTRAINT info_produccion_pk PRIMARY KEY ( batch );

CREATE TABLE info_tina (
    cod_tina   INTEGER NOT NULL,
     VARCHAR2(60) NOT NULL
);

ALTER TABLE info_tina ADD CONSTRAINT info_tina_pk PRIMARY KEY ( cod_tina );

CREATE TABLE tipo_horno (
    id_tipo_horno INTEGER NOT NULL,
    nombre_horno  VARCHAR2(20) NOT NULL
);

ALTER TABLE tipo_horno ADD CONSTRAINT tipo_horno_pk PRIMARY KEY ( id_tipo_horno );

CREATE TABLE tipo_malta (
    id_tipo_malta INTEGER NOT NULL,
    nombre_malta  VARCHAR2(60) NOT NULL
);

ALTER TABLE tipo_malta ADD CONSTRAINT tipo_malta_pk PRIMARY KEY ( id_tipo_malta );

CREATE TABLE usuarios (
    id_usuario  INTEGER NOT NULL,
    rut         VARCHAR2(13) NOT NULL,
    nom_usuario VARCHAR2(250) NOT NULL,
    contraseña  VARCHAR2(250) NOT NULL,
    mail        VARCHAR2(250) NOT NULL,
    rol         VARCHAR2(250) NOT NULL
);

ALTER TABLE usuarios ADD CONSTRAINT usuarios_pk PRIMARY KEY ( id_usuario );

CREATE TABLE variedad (
    id_variedad INTEGER NOT NULL,
    descripcion  VARCHAR2(60) NOT NULL
);

ALTER TABLE variedad ADD CONSTRAINT variedad_pk PRIMARY KEY ( id_variedad );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_analista_fk FOREIGN KEY ( analista_id_analista )
        REFERENCES analista ( id_analista );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_cliente_fk FOREIGN KEY ( cliente_id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_estado_fk FOREIGN KEY ( estado_id_estado )
        REFERENCES estado ( id_estado );


ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_info_produccion_fk FOREIGN KEY ( info_produccion_batch )
        REFERENCES info_produccion ( batch );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_tipo_malta_fk FOREIGN KEY ( tipo_malta_id_tipo_malta )
        REFERENCES tipo_malta ( id_tipo_malta );

ALTER TABLE info_analisis
    ADD CONSTRAINT info_analisis_variedad_fk FOREIGN KEY ( variedad_id_variedad )
        REFERENCES variedad ( id_variedad );


ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_info_analisis_fk FOREIGN KEY ( info_analisis_batch )
        REFERENCES info_analisis ( batch );


ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_info_germinacion_fk FOREIGN KEY ( info_germinacion_cod_germinacion )
        REFERENCES info_germinacion ( cod_germinacion );

ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_info_horno_fk FOREIGN KEY ( info_horno_fecha,
                                                               info_horno_batch )
        REFERENCES info_horno ( fecha,
                                batch );

ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_info_tina_fk FOREIGN KEY ( info_tina_cod_tina )
        REFERENCES info_tina ( cod_tina );

ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_tipo_horno_fk FOREIGN KEY ( tipo_horno_id_tipo_horno )
        REFERENCES tipo_horno ( id_tipo_horno );

ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_tipo_malta_fk FOREIGN KEY ( tipo_malta_id_tipo_malta )
        REFERENCES tipo_malta ( id_tipo_malta );

ALTER TABLE info_produccion
    ADD CONSTRAINT info_produccion_usuarios_fk FOREIGN KEY ( usuarios_id_usuario )
        REFERENCES usuarios ( id_usuario );




