from configparser import ConfigParser

def read_db_config(filename='DbConfig.ini',section='mysql'):
    '''
    Reads database configuration from file
    :param filename: name of the config file
    :param section: name of the section in the config file
    :return: a dictionary of parameters
    '''

    parser = ConfigParser()
    parser.read(filename)
    db={}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} section is not in {1} file'.format(section,filename))

    return db