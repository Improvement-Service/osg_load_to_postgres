/*SET THE CLIENT ENCODING*/
\encoding UTF8

/*LOAD THE DATA TO PostgreSQL USING "\COPY" META-COMMANDS*/
\copy header_10 FROM :data_in/:data_in/11.csv WITH (FORMAT csv, HEADER false);
\copy streets_11 FROM :data_in/11.csv WITH (FORMAT csv, HEADER false);
\copy esus_13 FROM :data_in/13.csv WITH (FORMAT csv, HEADER false);
\copy street_descriptions_15 FROM :data_in/15.csv WITH (FORMAT csv, HEADER false);
\copy street_xrefs_12 from :data_in/12.csv WITH (FORMAT csv, HEADER false);
\copy metadata_29 FROM :data_in/29.csv WITH (FORMAT csv, HEADER false);
\copy maintenance_responsibilities_51 FROM :data_in/51.csv WITH (FORMAT csv, HEADER false);
\copy reinstatement_categories_52 FROM :data_in/52.csv WITH (FORMAT csv, HEADER false);
\copy special_designations_53 FROM :data_in/53.csv WITH (FORMAT csv, HEADER false);
\copy trailer_99 FROM :data_in/99.csv WITH (FORMAT csv, HEADER false);