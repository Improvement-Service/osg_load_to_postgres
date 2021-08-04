DROP TABLE IF EXISTS application_xrefs_23; 

CREATE TABLE application_xrefs_23 (
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1) NOT NULL,
    pro_order BIGINT NOT NULL,
    uprn BIGINT NOT NULL,
    xref_key CHARACTER VARYING(14) NOT NULL,
    start_date DATE,
    last_update_date DATE,
    entry_date DATE,
    end_date DATE,
    cross_reference CHARACTER VARYING(50) NOT NULL,
    source CHARACTER VARYING(6),
CONSTRAINT appxrefs_pk PRIMARY KEY(XREF_KEY,UPRN)
--,
--CONSTRAINT appxrefs_fk_uprn FOREIGN KEY(UPRN) REFERENCES blpus_21(uprn)
);