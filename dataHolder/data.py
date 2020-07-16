from dataHolder.help_functions import *
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["dbGraphDonald"]

col2014 = db["collection2014"]
col2015 = db["collection2015"]
col2016 = db["collection2016"]
col2017 = db["collection2017"]
col2018 = db["collection2018"]
col2019 = db["collection2019"]
col2020 = db["collection2020"]

collections_list = [col2014, col2015, col2016, col2017, col2018, col2019, col2020]

data = create_counts_of_tweets_per_year(collections_list)

data_week2014 = find_list_for_each_year_per_week(col2014)
data_week2015 = find_list_for_each_year_per_week(col2015)
data_week2016 = find_list_for_each_year_per_week(col2016)
data_week2017 = find_list_for_each_year_per_week(col2017)
data_week2018 = find_list_for_each_year_per_week(col2018)
data_week2019 = find_list_for_each_year_per_week(col2019)
data_week2020 = find_list_for_each_year_per_week(col2020)

list_data = [data_week2014, data_week2015, data_week2016, data_week2017, data_week2018, data_week2019, data_week2020]

data_week = sum_of_all_per_week_posts(list_data)

data_for_happy = sum_all_posts_with_happy_in_for_years(collections_list)

data_for_angry = sum_all_posts_with_angry_in_for_years(collections_list)
