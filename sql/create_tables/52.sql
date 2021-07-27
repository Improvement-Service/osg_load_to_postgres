DROP TABLE IF EXISTS reinstatement_categories_52; 

CREATE TABLE reinstatement_categories_52 (
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1),
    pro_order BIGINT,
    usrn BIGINT NOT NULL,
    custodian_code INTEGER NOT NULL,
    category_seq_num INTEGER,
    reinstatement_authority_code INTEGER,
    reinstatement_category SMALLINT,
    whole_road SMALLINT,
    specific_location CHARACTER VARYING(250),
    "state" SMALLINT,
    entry_date DATE,
    start_date DATE,
    last_update_date DATE,
    end_date DATE,
    geometry GEOMETRY(Geometry),
CONSTRAINT rein_fk_usrn FOREIGN KEY(usrn) REFERENCES streets_11(usrn)
);