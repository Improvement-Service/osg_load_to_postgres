DROP TABLE IF EXISTS lpis_24; 

CREATE TABLE lpis_24 (
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1) NOT NULL,
    pro_order BIGINT NOT NULL,
    uprn BIGINT NOT NULL,
    lpi_key CHARACTER VARYING(14) NOT NULL,
    language CHARACTER VARYING(3),
    logical_status SMALLINT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    entry_date DATE,
    last_update_date DATE NOT NULL,
    sao_start_number SMALLINT,
    sao_start_suffix CHARACTER VARYING(2),
    sao_end_number SMALLINT,
    sao_end_suffix CHARACTER VARYING(2),
    sao_text CHARACTER VARYING(90),
    pao_start_number SMALLINT,
    pao_start_suffix CHARACTER VARYING(2),
    pao_end_number SMALLINT,
    pao_end_suffix CHARACTER VARYING(2),
    pao_text CHARACTER VARYING(90),
    usrn BIGINT NOT NULL,
    sub_locality CHARACTER VARYING(35),
    postally_addressable CHARACTER VARYING(1),
    postcode CHARACTER VARYING(8),
    post_town CHARACTER VARYING(30),
    official_flag CHARACTER VARYING(1),
CONSTRAINT lpis_pk PRIMARY KEY(lpi_key),
CONSTRAINT lpis_fk_uprn FOREIGN KEY(uprn) REFERENCES blpus_21(uprn),
CONSTRAINT lpis_fk_ursn FOREIGN KEY(usrn) REFERENCES streets_11(usrn)
);