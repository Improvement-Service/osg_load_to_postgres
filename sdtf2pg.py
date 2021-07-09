import psycopg2

class OsgPsqlDbLoad(object):
    """
    Class to load previously split SDTF CSV file into a Postgresql datbase using psql COPY command.
    Host machine must have PSQL installed
    
    #GoogleStyle 
    Args:
        db_name (str):  Name of postgres db
        live_schema (str):  Name of the live schema within the db  Final tables will output here.
        tmp_schema (str): Name of the live schema within the db. Temp tables will be processed and dropped from here.
        user (str):  DB username .
        passwd (str):  DB password for user.
        osg_split_csvs (lst):  CSV files, split from original SDTF by record_identifier. Will be loaded to db directly.
        host (str):  Host of postgres db
        port (str):  Port of postgres db
        
    Attributes:
        osg_table_ids (lst): List of table numbers in OSG spec. Used to validate CSV files.
        
        
    #NumPy Style
    Parameters
    ---------
    db_name : str
        Name of postgres db
    live_schema : str
        Name of the live schema within the db.  Final tables will output here
    tmp_schema : str
        Name of the live schema within the db. Temp tables will be processed and dropped from here
    user : str  
        DB username
    passwd : str
        DB password for user
    osg_split_csvs : list
        CSV files, split from original SDTF by record_identifier. Will be loaded to db directly.
    host : str
        Host for postgres db
    port : int 
        Port for postgres db
            
    Attributes
    ----------
    osg_table_ids : list 
        List of table numbers in OSG spec. Used to validate CSV files.
    
    """
    osg_table_ids = [
                10,
                11,
                12,
                13,
                14,
                15,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                29,
                30,
                31,
                32,
                51,
                52,
                53,
                93,
                99
                ]    
    
    def __init__(self, db_name, live_schema, tmp_schema, user, passwd, 
                 osg_split_csvs, host='localhost', port=5432):
        self.db_name = db_name
        self.live_schema = live_schema
        self.tmp_schema = tmp_schema
        self.user = user
        self.passwd = passwd
        self.osg_split_csvs = osg_split_csvs
        self.host = host
        self.port = port
        
        #Validation of arguments.
        if  self.live_schema not in ['osg', 'osg_v4', 'sg', 'sg_v4']:
            print(type(self.live_schema))
            raise ValueError(
                'Live schema name {} is unexpected.  Not completing SQL operation.'.format(self.live_schema)
            )
        if self.tmp_schema not in ['temp', 'tmp']:
            print(self.tmp_schema)
            raise ValueError(
                'Temp schema name {} is unexpected.  Not completing SQL operation.'.format(self.tmp_schema)
            )
        if any(char.isspace() for char in self.db_name):
            raise ValueError('db_name cannot contain whitespace')
        if any(char.isspace() for char in self.user):
            raise ValueError('user cannot contain whitespace')
        if any(char.isspace() for char in self.live_schema):
            raise ValueError('live_schema cannot contain whitespace')
        if any(char.isspace() for char in self.tmp_schema):
            raise ValueError('tmp_schema cannot contain whitespace')

    def create_psql_command(self, sql_file: str):
        cmd_str = 'psql -h {} -U {} -d {} -c \'set search_path = {}\' -af {}'.format(
                shlex.quote(self.host), 
                shlex.quote(self.user), 
                shlex.quote(self.db_name), 
                shlex.quote(self.tmp_schema), 
                shlex.quote(sql_file)
                )
        cmd_lst = shlex.split(cmd_str)
        #cmd = subprocess.run(cmd_lst, capture_output=True, text=True, shell=True)
        return cmd_lst
    
    def run_psql_command(self, cmd: list):
        cmd = subprocess.run(cmd_list, capture_output=True, text=True, shell=True)
        # Send output to logger
        return cmd
            
    def psql_copy_data(self, osg_split_csvs:list):
        """
        Use PSQL COPY command to load split SDTF files to Postgres database.  
        Check to make sure split table name matches expected name structure.
        """
        for file in osg_split_csvs:
            if file.split('/')[-1].split('\\')[-1].split('.')[0] not in osg_table_ids:
                raise ValueError(
                    'Unexpected SDTF split file name.  It should be in list of OSG table IDs.'
            )

        command = ''
        command_list = shlex.split(shlex.quote(command))
        return command_list
        pass
    
    def build_constraints(self, sql_constraint_file:str):
        """
        Use SQL file to build constraints on tables after load.
        """
        pass
    
    
    def create_tmp_schema(self):
        """
        Create temporary schema if it doesn't exist.
        """     
        conn = psycopg2.connect(f"dbname={self.db_name} user={self.user}")
        cur = conn.cursor()
        cur.execute(f'CREATE SCHEMA IF NOT EXISTS {self.tmp_schema} AUTHORIZATION "SISedit";')
        conn.commit()
        cur.close()
        conn.close()
        return None

    def tmp_schema_to_live(self):
        """
        Move temp tables to live by renaming the schema and all tables within.
        """
        if  self.live_schema not in ['osg', 'osg_v4', 'sg', 'sg_v4']:
            print(type(self.live_schema))
            raise ValueError(
                'Live schema name {} is unexpected.  Not completing SQL operation.'.format(self.live_schema)
            )
        if self.tmp_schema not in ['temp', 'tmp']:
            print(self.tmp_schema)
            raise ValueError(
                'Temp schema name {} is unexpected.  Not completing SQL operation.'.format(self.tmp_schema)
            )
        
        #sql = f'ALTER SCHEMA {self.temp_schema} RENAME TO {self.live_schema}'
        conn = psycopg2.connect(f"dbname={self.db_name} user={self.user}")
        cur = conn.cursor()
        cur.execute(f'DROP SCHEMA {self.live_schema} CASCADE;')
        cur.execute(f'ALTER SCHEMA {self.tmp_schema} RENAME TO {self.live_schema};')
        conn.commit()
        cur.close()
        conn.close()
        return None