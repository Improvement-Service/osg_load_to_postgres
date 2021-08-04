DROP TABLE IF EXISTS special_designations_53; 

CREATE TABLE special_designations_53 (
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1),
    pro_order BIGINT,
    usrn BIGINT NOT NULL,
    custodian_code INTEGER NOT NULL,
    designation_seq_num INTEGER,
    authority_code INTEGER,
    special_designation SMALLINT,
    whole_road SMALLINT,
    specific_location CHARACTER VARYING(250),
    description CHARACTER VARYING(255),
    "state" SMALLINT,
    entry_date DATE,
    start_date DATE,
    last_update_date DATE,
    end_date DATE,
    geometry GEOMETRY(Geometry),
CONSTRAINT desig_fk_usrn FOREIGN KEY(usrn) REFERENCES streets_11(usrn)
);