-- BLPU geometry
ALTER TABLE blpus_21 ADD COLUMN geom geometry(Point,27700)
UPDATE blpus_21 SET geom = ST_SetSRID(ST_MakePoint(x_coordinate, y_coordinate), 27700 );

-- ESU geometry
SELECT UpdateGeometrySRID('esus_13','geometry',27700); 
-- ALTER TABLE esus_13 ALTER COLUMN geometry type geometry(LineString, 27700);