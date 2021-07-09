CREATE TABLE organisations_31 (
    record_identifier SMALLINT,
    change_type CHARACTER VARYING(1) NOT NULL,
    pro_order BIGINT NOT NULL,
    uprn BIGINT NOT NULL,
    org_key CHARACTER VARYING(14) NOT NULL,
    organisation CHARACTER VARYING(100),
    legal_name CHARACTER VARYING(60),
    start_date DATE NOT NULL,
    end_date DATE,
    entry_date DATE,
    last_update_date DATE NOT NULL,
CONSTRAINT orgs_pk PRIMARY KEY(org_key),
CONSTRAINT org_fk_uprn FOREIGN KEY(uprn) REFERENCES blpus_21(UPRN)
);