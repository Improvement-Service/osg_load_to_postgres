DROP TABLE IF EXISTS successor_xrefs_30; 

CREATE TABLE successor_xrefs_30(
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1) NOT NULL,
    pro_order BIGINT NOT NULL,
    predecessor BIGINT,
    succ_key CHARACTER VARYING(14) NOT NULL,
    start_date DATE NOT NULL,
    last_update_date DATE NOT NULL,
    entry_date DATE,
    end_date DATE,
    successor_type BIGINT NOT NULL,
    successor BIGINT NOT NULL
);