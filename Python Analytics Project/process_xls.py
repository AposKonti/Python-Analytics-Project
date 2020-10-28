import xlrd 
import re
import sqlite3
import csv
import os

#>>>>>>>>>>>>>>>SECTION 1
change_char_place = []
path = os.path.dirname(os.path.realpath(__file__))
for i in range( len(path) ):
    if path[i] == "\\":
        change_char_place.append(i)
path = list(path)
for i in change_char_place:
    path[i] = "/"
path = "".join(path)


database_path = path +"/project.db"                              # database path construction
create_e_counter = 0                                             # create error counter
ins_e_counter = 0                                                # insert error counter        
csv_header = ["Country_Name","Airplay","Railway","Ship","Road","Total"]   # csv header
#>>>>>>>>>>>END SECTION 1


#>>>>>>>>>>>>>>>SECTION 2
#---------------Connector initialization-----------------------------------------------------------
conn = sqlite3.connect(database_path)
cur = conn.cursor()
#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
a = xlrd.open_workbook(path + "/2011.xls")                     
b = xlrd.open_workbook(path + "/2012.xls")                     
c = xlrd.open_workbook(path + "/2013.xls")                     
d = xlrd.open_workbook(path + "/2014.xls")                     
docs = [a, b, c, d]                                            # documents list
#>>>>>>>>>>>END SECTION 2



#>>>>>>>>>>>>>>>SECTION 3
#---------------XLS READING PROCESS - DB CREATE INSERT- CSV CREATE WRITE---------------------------
date = 2011                                                    # initial date
for m in docs:                                                 # running the documents 
    print(date)                                                # printing date
    n = m.nsheets                                              # n -> number of sheets of doc
    for i in range (n):                                        # reading each sheet
        table_n = "Month_"+str(i+1)+"_"+str(date)              # constructing table name
        try:                                                   # try to create table 
            cur.execute("CREATE TABLE IF NOT EXISTS "+table_n+" (Contry_Name text PRIMARY KEY, Airplane FLOAT, Railway FLOAT, Ship FLOAT, Road FLOAT, Total FLOAT)")    # constructing sqlite3 create query
            conn.commit()                                      # commiting query
            print("Successful creation of table with name: "+table_n)     # successful creation query
        except sqlite3.Error as error:                         # except 
            print(error)
            create_e_counter +=1                               # default error message
            print("Couldn't create table with name: " + table_n + "Could not create "+ str(create_e_counter) + "tables.") # personalized error message 
        s = m.sheet_by_index(i)                                # s -> the sheet
        s1 = s.nrows                                           # s1 -> num of rows in the sheet
        s2 = s.ncols                                           # s2 -> num of cols in the sheet
        table_rec = []                                         # list to store records in
        for j in range (s1):                                   # reading each row
            c = str(s.cell(j,0).value)                         # from each row the first cell is selected
            p = re.match(r'\d.',c)                             # regural expression matching numbers
            w = re.search("Source",c)                          # regural expression matching termination cell ()
            if w:                                              # if the termination regular expression is satified the program stops
                break                                          # termination regular expression
            if p:                                              # if the regual expresion of what is need is satified
                record = []                                    # is added into the record to store the values 
                for k in range (1, s2):                        # searching columns 
                    record.append(s.cell(j,k).value)           # inserting value into record
                table_rec.append(record)                       # inserting record in the table of records
                #---------Importing data to SQLite3-----------------------------------------------
                ins_q ="INSERT INTO "+table_n+" VALUES(?, ?, ?, ?, ?, ?)" # construction of isert query
                data = (str(record[0]), record[1], record[2], record[3], record[4], record[5]) # data values for insert query
                try:                                            # try to insert
                    cur.execute(ins_q,data)                     # excecuting query
                    print("Successful insert in table with name: "+table_n) # personalized successful insert message
                    conn.commit()                               # commiting query
                except sqlite3.Error as error:                  # except
                    ins_e_counter+=1                            # error counter
                    print(error)                                # default error message
                    print("Insertion failed. Number of failed insertion attemts: " + str(ins_e_counter)) # personalized error message
                #---------------------------------------------------------------------------------
        #---------Importing data to CSV---------------------------------------------------
        csv_n = table_n+".csv"                                  # constructing csv name 
        csv_p = path + "/" + csv_n                              # constructing csv creation path
        with open (csv_p, 'w', newline='') as file:             # opening csv file
            writer = csv.writer(file)                           # initiallizing writer
            writer.writerow(csv_header)                         # writing header
            for r in table_rec:                                 # reading table of records
                writer.writerow(r)                              # writing each row
        #---------------------------------------------------------------------------------
    record.clear()                                              # clearing record list
    table_rec.clear()                                           # clearing table of records
    date = date + 1                                             # increasing date for table name 
#--------------------------------------------------------------------------------------------------
#----------------------------------Connection closing----------------------------------------------
conn.close()                                                   #closing connection to the database
#--------------------------------------------------------------------------------------------------
#>>>>>>>>>>>END SECTION 3