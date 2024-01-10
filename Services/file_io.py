'''
helps to read, write, append , write multiple list in .csv file
'''

def file_reader(file):
    '''
    helps to read .csv files 
    '''
    with open(file, 'r', encoding="utf-8") as f:
        data = f.readlines()
    return data 

def file_writer(file, data):
    '''
    helps to write in .csv model
    '''
    with open(file, 'w', encoding="utf-8") as f:
        f.write(data)
    return True

def file_appender(file, data):
    '''
    helps to add data in .csv 
    '''
    with open(file,'a', encoding="utf-8") as f:
        f.write(data)
    return True

def file_list_writer(file, data):
    '''
    helps to wrie multiple lines in .csv
    '''
    with open(file, 'w', encoding="utf-8") as f:
        f.writelines(data)
    return True