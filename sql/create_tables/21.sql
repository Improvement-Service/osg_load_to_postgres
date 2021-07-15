DROP TABLE IF EXISTS blpus_21 CASCADE; 

CREATE TABLE blpus_21 (
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1) NOT NULL,
    pro_order BIGINT NOT NULL,
    uprn BIGINT NOT NULL,
    logical_status SMALLINT NOT NULL,
    blpu_state SMALLINT,
    blpu_state_date DATE,
    parent_uprn BIGINT,
    x_coordinate NUMERIC(9,2) NOT NULL,
    y_coordinate NUMERIC(9,2) NOT NULL,
    rpc SMALLINT NOT NULL,
    custodian_code SMALLINT,
    start_date DATE NOT NULL,
    end_date DATE,
    last_update_date DATE NOT NULL,
    entry_date DATE,
    level NUMERIC(3,2),
CONSTRAINT blpus_pk PRIMARY KEY(uprn)
);