DROP TABLE IF EXISTS street_descriptions_15; 

CREATE TABLE street_descriptions_15(
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1) NOT NULL,
    pro_order BIGINT NOT NULL,
    usrn BIGINT NOT NULL,
    descriptor CHARACTER VARYING(110) NOT NULL,
    locality CHARACTER VARYING(35),
    town CHARACTER VARYING(30),
    island CHARACTER VARYING(30),
    administrative_area CHARACTER VARYING(30),
    language CHARACTER VARYING(3),
CONSTRAINT streetdescs_fk FOREIGN KEY(usrn) REFERENCES streets_11(usrn)
);