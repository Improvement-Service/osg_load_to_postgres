DROP TABLE IF EXISTS streets_11 CASCADE; 

CREATE TABLE streets_11 (
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1) NOT NULL,
    PRO_ORDER BIGINT NOT NULL,
    usrn BIGINT NOT NULL,
    record_type SMALLINT,
    custodian_code SMALLINT NOT NULL,
    entry_date DATE,
    start_date DATE,
    last_update_date DATE,
    end_date DATE,
CONSTRAINT streets_pk PRIMARY KEY(usrn)
);