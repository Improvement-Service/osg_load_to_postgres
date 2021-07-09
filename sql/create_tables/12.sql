CREATE TABLE street_xrefs_12(
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1),
    pro_order BIGINT ,
    usrn INTEGER NOT NULL,
    esu_id BIGINT NOT NULL,
    entry_date DATE,
    start_date DATE,
    last_update_date DATE,
    end_date DATE,
CONSTRAINT streetxrefs_fk_usrn FOREIGN KEY(usrn) REFERENCES streets_11(usrn)
CONSTRAINT streetxrefs_fk_esuid FOREIGN KEY(esu_id) REFERENCES esus_13(esu_id)
);