# OSG Load to Postgres DB

Script to load a [One Scotland Gazetter (OSG)](https://osg.scot) SDTF v4 file to a Postgres database.

---

## Requirements:

### 1) PSQL
This script relies on use of the [PSQL](https://www.postgresql.org/docs/13/app-psql.html) client. The PSQL COPY command is much quicker than unpacking the data and sending it through Psychopg2 or similar when doing a builk load of millions of records as is the case here.  In addition, the credentials to the Postgres database will need to be stored in a [pgpass]() file in order for the connection to proceed.  This pgpass file should be stored in a secure folder only accessible to the user running the script.

### 2) OSG FTP Access - IP whitelist
The script downloads the SDTF file from the OSG FTP site.  Access is restricted by IP address.  Check to make sure you have agreed access with the OSG custodians.  For example the Improvement Service SIS remote desktop IP has been whitelisted.

---

# Usage:

This script must be run from the root level of this project.  When run, a parameter must be passed to the script using the `-t` flag specifying which SDTF file type to load (_a or e_).  For example to load a type A file:
```
cd <repository root> 
python -m sdtf_load -t a
```

NOTE: this package must be run from the repository root in order to acces the relevant config and sql files.
