DROP TABLE IF EXISTS metadata_29; 

CREATE TABLE metadata_29(
    record_identifier SMALLINT,
    gaz_name CHARACTER VARYING(75),
    gaz_scope CHARACTER VARYING(60),
    ter_of_use CHARACTER VARYING(60),
    gaz_owner CHARACTER VARYING(60),
    custodian_name CHARACTER VARYING(40),
    custodian_code SMALLINT,
    co_ord_system CHARACTER VARYING(10),
    co_ord_unit CHARACTER VARYING(10),
    meta_date DATE,
    class_scheme CHARACTER VARYING(40),
    state_code_scheme CHARACTER VARYING(40),
    gaz_date DATE,
    "language" CHARACTER VARYING(3),
    character_set TEXT
);