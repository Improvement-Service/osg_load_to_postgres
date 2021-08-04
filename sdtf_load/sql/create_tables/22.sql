DROP TABLE IF EXISTS provenance_22; 

CREATE TABLE provenance_22(
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1) NOT NULL,
    pro_order BIGINT NOT NULL,
    uprn BIGINT,
    prov_key CHARACTER VARYING(14),
    extent_key CHARACTER VARYING(14),
    provenance_code CHARACTER VARYING(1) NOT NULL,
    annotation CHARACTER VARYING(30) NOT NULL,
    entry_date DATE,
    start_date DATE,
    end_date DATE,
    last_update_date DATE
--,
--CONSTRAINT prov_fk_uprn FOREIGN KEY(uprn) REFERENCES blpus_21(uprn)
);