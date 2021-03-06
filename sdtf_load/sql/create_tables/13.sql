DROP TABLE IF EXISTS esus_13 CASCADE; 

CREATE TABLE esus_13(
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1),
    pro_order BIGINT,
    esu_id BIGINT NOT NULL,
    "state" SMALLINT,
    state_date DATE,
    classification SMALLINT,
    classification_date DATE,
    entry_date DATE,
    start_date DATE,
    last_update_date DATE,
    end_date DATE,
    geometry geometry(Geometry),
CONSTRAINT esus_pk PRIMARY KEY(esu_id)
);