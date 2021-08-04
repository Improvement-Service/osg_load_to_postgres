DROP TABLE IF EXISTS blpu_classifications_32; 

CREATE TABLE blpu_classifications_32 (
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1) NOT NULL,
    pro_order BIGINT NOT NULL,
    uprn BIGINT NOT NULL,
    class_key CHARACTER VARYING(14),
    class_scheme CHARACTER VARYING(40),
    blpu_class CHARACTER VARYING(4),
    start_date DATE,
    end_date DATE,
    entry_date DATE,
    last_update_date DATE
/*, CONSTRAINT class_fk_uprn FOREIGN KEY(UPRN) REFERENCES blpus_21(uprn)*/
);