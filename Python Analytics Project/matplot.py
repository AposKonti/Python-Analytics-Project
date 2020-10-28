import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt4
import operator
import csv
import os
from tkinter import *
import tkinter as tk


#>>>>>>>>>>>>>>>SECTION 1
change_char_place = []
path = os.path.dirname(os.path.realpath(__file__))
for i in range( len(path) ):
    if path[i] == "\\":
        change_char_place.append(i)
path = list(path)
for i in change_char_place:
    #print(i)
    path[i] = "/"
path = "".join(path)

x_axis = ["2011","2012","2013","2014"]                          # list of year date for x axis
x_axis_q =["'11 Q1", "'11 Q2", "'11 Q3", "'11 Q4","'12 Q1", "'12 Q2", "'12 Q3", "'12 Q4", "'13 Q1", "'13 Q2", "'13 Q3", "'13 Q4","'14 Q1", "'14 Q2", "'14 Q3", "'14 Q4"] #list of quarter names for x axis
sum_total = []                                                  # list of each year's total tourists
sum_plane = 0                                                   # sum of tourists who use as means of transport planes
sum_rail = 0                                                    # sum of tourists who use as means of transport trains
sum_ship = 0                                                    # sum of tourists who use as means of transport ships
sum_road = 0                                                    # sum of tourists who use means of transport by road
transport = []                                                  # list of tourists by means of transport
sum_quarter = []                                                # list of quarters
quarter = 0                                                     # quarter tourists counter
country_dict = {}                                               # dictionary of countries an their total tourist's arrivals
country_name_list = []                                          # list of top 10 countries with highest tourist's arrivals
country_tourist_count_list = []                                 # list for number of tourists by country
#>>>>>>>>>>>END SECTION 1


#>>>>>>>>>>>>>>>SECTION 2
for date in range(2011,2015):                                   # for each year

    year_s = 0                                                  # setting the year sum to 0

    for month in range(1,13):                                   # for each month
        
        name = "Month_"+str(month)+"_"+str(date)+".csv"         # constructing csv name
        path_csv = path + "/" + name                            # constructing csv path
        f = open (path_csv)                                     # openning csv 
        csv_f = csv.reader(f)                                   # creating a csv reader
        next(f)                                                 # skipping the first line (the header)          
        for row in csv_f:
            #------------------------------------               # fixing issue with blank cells
            if row[1] == '':                                    # counting plane tourists
                row[1] = 0
                sum_plane = sum_plane + float(row[1])
            else:
                sum_plane = sum_plane + float(row[1])

            if row[2] == '':                                    # counting rail tourists
                row[2] = 0
                sum_rail = sum_rail + float(row[2])
            else:
                sum_rail = sum_rail + float(row[2])

            if row[3] == '':
                row[3] = 0
                sum_ship = sum_ship + float(row[3])             # counting ship tourists
            else:
                sum_ship = sum_ship + float(row[3])
            if row[4] == '':
                row[4] = 0
                sum_road = sum_road + float(row[4])             # counting road tourists
            else:
                sum_road = sum_road + float(row[4])
            if row[5] == '':
                row[5] = 0
            #------------------------------------
            year_s = year_s + float(row[5])                     # counting tourists by year
            #------------------------------------
            quarter = quarter + float(row[5])                   # counting tourists by quarter
            #------------------------------------
            if row[0] in country_dict:
                country_dict[row[0]] += round(float(row[5]))    # if a country is already in the dictionary the number of tourists is added to the current value
            else:
                country_dict[row[0]] = round(float(row[5]))     # if a country is not in the dictionary a key with its name is add and as value the tourist num
            #------------------------------------
        if month%3 == 0:                                        # counting tourists by quarter 
            sum_quarter.append(quarter)                         # when a quarter is complete it added to the sum quarter list
            quarter = 0                                         # the quarter counter get 0 for the next one
        f.close()
    sum_total.append(round(year_s))                             # when the whole year has be calculted the value is added to the sum total list
#>>>>>>>>>>>END SECTION 2


#>>>>>>>>>>>>>>>SECTION 3
def plot_total_tourists():

    #-----------Total Number of Tourists each year CHART-----------
    plt1.plot(x_axis,sum_total)
    plt1.xlabel("Date")
    plt1.ylabel("No of Tourists")
    plt1.title("Total number of Tourists for each year")
    plt1.show()
    #--------------------------------------------------------------

def plot_means_of_transport():
    #-----------------Means of transport PIE CHART-----------------
    transport = [round(sum_plane, 2), round(sum_rail, 2), round(sum_ship, 2), round(sum_road, 2)]
    transport_labels = ["By Plane", "By Rail", "By Ship", "By Road"]
    colors = ['b', 'r', 'y', 'g']
    plt2.title("Percentage by means of transport")
    plt2.axis("equal")
    plt2.pie(transport, labels = transport_labels, colors = colors, autopct='%1.3f%%')
    plt2.legend(transport_labels)
    plt2.show()
    #--------------------------------------------------------------

def plot_tourists_by_quarter():    
    #----------Total Number of Tourists each year Quarter----------
    plt3.plot(x_axis_q, sum_quarter)
    plt3.xticks(x_axis_q, x_axis_q, rotation='vertical')
    plt3.xlabel("Date")
    plt3.ylabel("No of Tourists")
    plt3.title("Total number of Tourists for each quarter")
    plt3.show()
    #--------------------------------------------------------------

def plot_top_countries():
    #-----------------Top 10 countries by tourists-----------------
    sorted_country_dict = sorted(country_dict.items(), key=operator.itemgetter(1),reverse=True)
    for x in list(sorted_country_dict)[0:10]:
        country_name_list.append(x[0])
        country_tourist_count_list.append(x[1])
    plt4.bar(country_name_list, country_tourist_count_list)
    plt4.xticks(country_name_list, country_name_list, rotation='vertical')
    plt4.title("Top countries by number of tourists")
    plt4.show()
    #--------------------------------------------------------------

#>>>>>>>>>>>END SECTION 3

#>>>>>>>>>>>>>>>SECTION 4
root = tk.Tk()                                                  # panel initilization                          

root.title("Tourists statistics")                               # panel title
root.geometry("1000x500")                                       # panel initial size
background_image=tk.PhotoImage(file=path+"/assets/background.png") # setting background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

all_tourists_button = tk.Button(root, text = "Total Number of Tourists by year", padx = 30, pady = 10, command = plot_total_tourists) # button for total tourists
all_tourists_button.pack()

means_of_transport_button = tk.Button(root, text = "Percentage by means of transport", padx = 30, pady = 10, command = plot_means_of_transport) # button for means of transport
means_of_transport_button.pack()

tourists_by_quarter_button = tk.Button(root, text = "Number of tourists by quarter of year", padx = 30, pady = 10, command = plot_tourists_by_quarter) # tourists by quarter
tourists_by_quarter_button.pack()

top_countries_by_tourist_count_button = tk.Button(root, text = "Top 10 countries by total tourist count", padx = 30, pady = 10, command = plot_top_countries) # top countries by tourists
top_countries_by_tourist_count_button.pack()


root.mainloop()
#>>>>>>>>>>>END SECTION 4