ALTER TABLE blpus_21 ADD COLUMN geom geometry(Point,27700)
UPDATE blpus_21 SET geom = ST_SetSRID(ST_MakePoint(x_coordinate, y_coordinate), 27700 );
ALTER TABLE esus_13 ADD COLUMN geom geometry(Geometry,27700);
UPDATE esus_13 SET geom = ST_GeomFromText(geometry,27700);