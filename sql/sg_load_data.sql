/*SET THE CLIENT ENCODING*/
\encoding UTF8

/*LOAD THE DATA TO PostgreSQL USING "\COPY" META-COMMANDS*/
\copy header_10 FROM '10.csv' WITH (FORMAT csv, HEADER false);
\copy streets_11 FROM '11.csv' WITH (FORMAT csv, HEADER false);
\copy esus_13 FROM '13.csv' WITH (FORMAT csv, HEADER false);
\copy street_descriptions_15 FROM '15.csv' WITH (FORMAT csv, HEADER false);
\copy street_xrefs_12 from '12.csv' WITH (FORMAT csv, HEADER false);
\copy metadata_29 FROM '29.csv' WITH (FORMAT csv, HEADER false);
\copy maintenance_responsibilities_51 FROM '51.csv' WITH (FORMAT csv, HEADER false);
\copy reinstatement_categories_52 FROM '52.csv' WITH (FORMAT csv, HEADER false);
\copy special_designations_53 FROM '53.csv' WITH (FORMAT csv, HEADER false);
\copy trailer_99 FROM '99.csv' WITH (FORMAT csv, HEADER false);