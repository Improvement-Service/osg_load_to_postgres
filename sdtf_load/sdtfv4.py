class SdtfV4:
    """
    Test way of doing this with classes and inheritance.
    Needs a little work.
    """
    tables = [ 
        (10, 'header_10'),
        (11, 'streets_11'),
        (12, 'street_xrefs_12'),
        (13, 'esus_13'),
        (15, 'street_descriptions_15'),
        (21, 'blpus_21'),
        (22, 'provenance_22'),
        (23, 'application_xrefs_23'),
        (24, 'lpis_24'),
        (25, ''),
        (26, ''),
        (27, ''),
        (29, 'metadata_29'),
        (30, 'successor_xrefs_30'),
        (31, 'organisations_31'),
        (32, 'blpu_classifications_32'),
        (51, 'maitenance_responsibilities_51'),
        (52, 'reinstatement_categories_52'),
        (53, 'special_designations_53'),
        (99, 'trailer_99')
    ]

    def __init__(self):
        pass

    def a(self):
        """
        Return only  those tables
        which are included in the SDTF Type A file.
        """
        sdtf_a = []
        for table in self.tables:
            if table[0] in [
                10, 11, 12, 13, 15, 21, 22, 23, 24, 28, 30, 31, 32, 99
            ]:
                sdtf_a.append(table)
        return sdtf_a

    def e(self):
        """
        Return only  those tables
        which are included in the SDTF Type A file.
        """
        sdtf_e = []
        for table in self.tables:
            if table[0] in [
            10, 11, 12, 13, 15, 29, 51, 52, 53, 99
            ]:
                sdtf_e.append(table)
        return sdtf_e



######
# Simpler method with simple funcitons to return tables as list of tuples.

def sdtfv4():
    """Return a list of tuples of OSG SDTF valid tables.
       First element is the table number (int)
       Second element is table name as will be created in Posgres db
    """
    sdtf = [ 
        (10, 'header_10'),
        (11, 'streets_11'),
        (12, 'street_xrefs_12'),
        (13, 'esus_13'),
        (15, 'street_descriptions_15'),
        (21, 'blpus_21'),
        (22, 'provenance_22'),
        (23, 'application_xrefs_23'),
        (24, 'lpis_24'),
        (25, ''),
        (26, ''),
        (27, ''),
        (29, 'metadata_29'),
        (30, 'successor_xrefs_30'),
        (31, 'organisations_31'),
        (32, 'blpu_classifications_32'),
        (51, 'maitenance_responsibilities_51'),
        (52, 'reinstatement_categories_52'),
        (53, 'special_designations_53'),
        (99, 'trailer_99')
    ]
    return sdtf

def sdtf_a():
    """
    Return tuples from sdtfv4() however only return those tables
    which are included in the SDTF Type A file.
    """
    sdtfv4_a = []
    for table in sdtfv4():
        if table[0] in [
            10, 11, 12, 13, 15, 21, 22, 23, 24, 28, 30, 31, 32, 99
        ]:
            sdtfv4_a.append(table)
    return sdtfv4_a

def sdtf_e():
    """
    Return tuples from sdtfv4() however only return those tables
    which are included in the SDTF Type E file.
    """    
    sdtfv4_e = []
    for table in sdtfv4():
        if table[0] in [
            10, 11, 12, 13, 15, 29, 51, 52, 53, 99
        ]:
            sdtfv4_e.append(table)
    return sdtfv4_e



# Using simple function
print(sdtf_e())

# Using inherited class attributes
#test = sdtfv4.SdtfV4()
print(SdtfV4().a())
