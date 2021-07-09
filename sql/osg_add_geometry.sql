UPDATE blpus_21 SET geom = ST_GeomFromText('POINT(' || x_coordinate || ' ' || y_coordinate || ')', 27700 );
UPDATE esus_13 SET geom = ST_GeomFromText(geometry,27700);