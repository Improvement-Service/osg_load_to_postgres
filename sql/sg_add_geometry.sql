SELECT UpdateGeometrySRID('esus_13','geometry',27700); 
SELECT UpdateGeometrySRID('maintenance_responsibilities_51','geometry',27700); 
SELECT UpdateGeometrySRID('reinstatement_categories_52','geometry',27700); 
SELECT UpdateGeometrySRID('special_designations_53','geometry',27700); 
/*
ALTER TABLE esus_13 ALTER COLUMN geometry type geometry(LineString, 27700);
ALTER TABLE maintenance_responsibilities_51 ALTER COLUMN geometry type geometry(MultiLineString, 27700) using ST_Multi(geometry);
ALTER TABLE reinstatement_categories_52 ALTER COLUMN geometry type geometry(MultiLineString, 27700) using ST_Multi(geometry);
ALTER TABLE special_designations_53 ALTER COLUMN geometry type geometry(MultiLineString, 27700) using ST_Multi(geometry);
*/