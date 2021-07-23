/*SET THE CLIENT ENCODING*/
\encoding UTF8

/* :data_in variable is the folder where the split SDTF CSVs sit 
e.g. data_in = in/9080_20210720_A_01         */

/*LOAD THE DATA TO PostgreSQL USING "\COPY" META-COMMANDS*/
\copy  header_10 FROM '10.csv' WITH (FORMAT csv, HEADER false);
\copy streets_11 FROM '11.csv' WITH (FORMAT csv, HEADER false);
\copy esus_13 FROM '13.csv' WITH (FORMAT csv, HEADER false);
\copy street_descriptions_15 FROM '15.csv' WITH (FORMAT csv, HEADER false);
\copy street_xrefs_12 from '12.csv' WITH (FORMAT csv, HEADER false);
\copy blpus_21 FROM '21.csv' WITH (FORMAT csv, HEADER false);
\copy provenance_22 FROM '22.csv' WITH (FORMAT csv, HEADER false);
\copy application_xrefs_23 FROM '23.csv' WITH (FORMAT csv, HEADER false);
\copy lpis_24 FROM '24.csv' WITH (FORMAT csv, HEADER false);
\copy metadata_29 FROM '29.csv' WITH (FORMAT csv, HEADER false);
\copy successor_xrefs_30 FROM '30.csv' WITH (FORMAT csv, HEADER false);
\copy organisations_31 FROM '31.csv' WITH (FORMAT csv, HEADER false);
\copy blpu_classifications_32 FROM '32.csv' WITH (FORMAT csv, HEADER false);
\copy trailer_99 FROM '99.csv' WITH (FORMAT csv, HEADER false);