DROP TABLE IF EXISTS maintenance_responsibilities_51; 

CREATE TABLE maintenance_responsibilities_51 (
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1),
    pro_order BIGINT,
    usrn BIGINT NOT NULL,
    custodian_code INTEGER,
    maintenance_seq_num INTEGER NOT NULL,
    maintaining_authority_code INTEGER,
    whole_road SMALLINT,
    specific_location CHARACTER VARYING(250),
    street_status SMALLINT,
    "state" SMALLINT,
    entry_date DATE,
    start_date DATE,
    last_update_date DATE,
    end_date DATE,
    geometry GEOMETRY(Geometry),
CONSTRAINT main_fk_usrn FOREIGN KEY(usrn) REFERENCES streets_11(usrn)
);