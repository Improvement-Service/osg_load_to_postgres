import psycopg2
import os
import shlex
import subprocess
    
class OsgPsqlDbLoad(object):
    """
    Class to load previously split SDTF CSV file into a Postgresql datbase using psql COPY command.
    Host machine must have PSQL installed.
    
    #GoogleStyle 
    Args:
        db_name (str):  Name of postgres db
        live_schema (str):  Name of the live schema within the db  Final tables will output here.
        tmp_schema (str): Name of the live schema within the db. Temp tables will be processed and dropped from here.
        user (str):  DB username .
        passwd (str):  DB password for user.
        sdtf_type (str):  Type of SDTF file.  Will be used to determine what SQL files to run
        host (str):  Host of postgres db
        port (int):  Port of postgres db
        
    Attributes:
        sql_files (dict):  Dict of SQL files used in PSQL commands within class.  SQL files part of repo.    
    """
        
    sql_files = {
        'create': {
            'osg': 'sql/osg_create_tables.sql', 
            'sg': 'sql/sg_create_tables.sql'
        },
        'load': {
            'osg': 'sql/osg_load_data.sql', 
            'sg': 'sql/sg_load_data.sql'
        },
        'add_geom': {
            'osg': 'sql/osg_add_geometry.sql', 
            'sg': 'sql/sg_add_geometry.sql'
        }
    }
    
    def __init__(self, db_name, live_schema, tmp_schema, user, sdtf_type, read_user,
                 host='localhost', port=5432):
        self.db_name = db_name
        self.live_schema = live_schema
        self.tmp_schema = tmp_schema
        self.user = user
        self.read_user = read_user
        self.host = host
        self.port = port
        self.sdtf_type = sdtf_type
        if sdtf_type.upper() == 'E':
            self.gaz_type = 'sg'
            self.create_sql = OsgPsqlDbLoad.sql_files['create']['sg']
            self.load_sql = OsgPsqlDbLoad.sql_files['load']['sg']
            self.add_geom_sql = OsgPsqlDbLoad.sql_files['add_geom']['sg']
        else:
            self.gaz_type = 'osg'
            self.create_sql = OsgPsqlDbLoad.sql_files['create']['osg']
            self.load_sql = OsgPsqlDbLoad.sql_files['load']['osg']
            self.add_geom_sql = OsgPsqlDbLoad.sql_files['add_geom']['osg']
        
        #Validation of arguments.
        if sdtf_type.upper() not in ['A', 'E']:
            raise ValueError('sdtf_type was not expected, should be "A" or "E".  Vale provided was:{sdtf_type})')
        if  self.live_schema not in ['osg', 'osg_v4', 'sg', 'sg_v4']:
            raise ValueError(
                'Live schema name {} is unexpected.  Not completing SQL operation.'.format(self.live_schema)
            )
        if self.tmp_schema not in ['temp', 'tmp']:
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

    def create_psql_command(self, sql_file: str, var_assign:dict = None):
        cmd_str = 'psql -h {} -U {} -d {} -c \'set search_path = {}, public;\' -af {}'.format(
                shlex.quote(self.host), 
                shlex.quote(self.user), 
                shlex.quote(self.db_name), 
                shlex.quote(self.tmp_schema), 
                shlex.quote(sql_file)
                )
        # Add variable assignment if this is added
        if var_assign is not None:
            for k, v in var_assign.items():
                if  len(k.split(' ')) > 1 or len(v.split(' ')) > 1:
                    raise ValueError('Variable assignment dict has whitespace. Not allowed for security')
                cmd_str = cmd_str + ' -v ' + shlex.quote(f'{k}={v}')
                
        cmd_list = shlex.split(cmd_str)
        #cmd = subprocess.run(cmd_list, capture_output=True, text=True, shell=True)
        return cmd_list

    def run_psql_command(self, cmd_list: list):
        cmd = subprocess.run(cmd_list, capture_output=True, text=True, shell=True)
        if cmd.returncode != 0:
            try:
                cmd.check_returncode()
            except subprocess.CalledProcessError as exc:
                print(f'The query failed and retured the following error: {cmd.stderr}')
                raise exc
        # Send output to logger
        return cmd
        
    def create_tmp_schema(self):
        cmd_str = 'psql -h {host} -U {user} -d {db} -c \'DROP SCHEMA IF EXISTS {tmp} CASCADE;\
                 CREATE SCHEMA {tmp};\''.format(
                host=shlex.quote(self.host), 
                user=shlex.quote(self.user), 
                db=shlex.quote(self.db_name), 
                tmp=shlex.quote(self.tmp_schema), 
                )
        cmd_list = shlex.split(cmd_str)
        cmd = self.run_psql_command(command)
        # cmd = subprocess.run(cmd_lst, capture_output=True, text=True, shell=True)
        return cmd
    
    def psql_create_tables(self):
        """
        Run PSQL on specific SQL file which uses PSQL to run a series of SQL files to create
        tables for OSG & Street Gaz schema.
        """
        cmd_list = self.create_psql_command(self.create_sql)
        cmd = self.run_psql_command(cmd_list)
        # cmd = subprocess.run(cmd_lst, capture_output=True, text=True, shell=True)
        return cmd

    def psql_authorise_reader_user(self):
        """
        Authorise a user to select data from the tables.
        """
        cmd_str = 'psql -h {host} -U {user} -d {db} -c \
                \'GRANT SELECT ON ALL TABLES IN SCHEMA {tmp} TO "{reader}";\''.format(
                host=shlex.quote(self.host), 
                user=shlex.quote(self.user), 
                db=shlex.quote(self.db_name), 
                tmp=shlex.quote(self.tmp_schema), 
                reader=shlex.quote(self.read_user)
                )
        cmd_list = shlex.split(cmd_str)
        cmd = self.run_psql_command(cmd_list)
        # cmd = subprocess.run(cmd_lst, capture_output=True, text=True, shell=True)
        return cmd
    
    def psql_load_data(self, temp_dir):
        """
        Run PSQL on specific SQL file which uses PSQL COPY command to load split SDTF 
        files to Postgres database.  Very specifically points to sql file.
        """
        # get current working directory then change to temp data directory.
        self.load_sql = os.path.abspath(self.load_sql)
        cwd = os.getcwd()
        os.chdir(temp_dir)
        command = self.create_psql_command(self.load_sql)
        cmd = self.run_psql_command(command)
        print(cmd)
        # Change directory back to old directory
        os.chdir(cwd)
        return cmd

    def psql_add_geom(self):
        """
        Use SQL file to build constraints on tables after load.
        """
        command = create_psql_command(self.add_geom_sql)
        run_psql_command(command)    
    
    def create_tmp_schema(self):
        """
        Create temporary schema if it doesn't exist.
        """     
        conn = psycopg2.connect(f"dbname={self.db_name} user={self.user}")
        cur = conn.cursor()
        cur.execute(
                    f'DROP SCHEMA IF EXISTS {self.tmp_schema} CASCADE; \
                    CREATE SCHEMA IF NOT EXISTS {self.tmp_schema} \
                    AUTHORIZATION "{self.read_user}";'
                    )
        conn.commit()
        cur.close()
        conn.close()
        return None

    def move_temp_to_live(self):
        """
        Move temp tables to live by renaming the schema and all tables within.
        """     
        #sql = f'ALTER SCHEMA {self.temp_schema} RENAME TO {self.live_schema}'
        conn = psycopg2.connect(f"dbname={self.db_name} user={self.user}")
        cur = conn.cursor()
        cur.execute(f'DROP SCHEMA {self.live_schema} CASCADE;')
        cur.execute(f'ALTER SCHEMA {self.tmp_schema} RENAME TO {self.live_schema};')
        conn.commit()
        cur.close()
        conn.close()
        return None