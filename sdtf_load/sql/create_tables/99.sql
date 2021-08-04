DROP TABLE IF EXISTS trailer_99; 

CREATE TABLE trailer_99(
    record_identifier SMALLINT,
    next_volume_number SMALLINT,
    record_count BIGINT,
    entry_date DATE,
    time_stamp TIME WITHOUT TIME ZONE
);