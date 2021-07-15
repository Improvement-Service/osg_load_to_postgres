DROP TABLE IF EXISTS header_10; 


CREATE TABLE header_10(
    record_identifier SMALLINT,
    custodian_name TEXT,
    custodian_code INTEGER,
    process_date DATE,
    volume_number INTEGER,
    entry_date DATE,
    time_stamp TIME WITHOUT TIME ZONE,
    dtf_version NUMERIC(3,2),
    file_type TEXT 
);