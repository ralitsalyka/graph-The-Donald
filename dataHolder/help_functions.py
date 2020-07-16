import pymongo


WEEK = ['^Mon', '^Tue', '^Wed', '^Thu', '^Fri', '^Sat', '^Sun']


def create_counts_of_tweets_per_year(colleciions_list):
    new_list = [elem.count() for elem in colleciions_list]
    return new_list


def find_list_for_each_year_per_week(collection):
    list_of_counts = []
    for week_day in WEEK:
        count = 0
        count = collection.find({"created_at": {'$regex': week_day}}).count()
        list_of_counts.append(count)
    return list_of_counts


def sum_of_all_per_week_posts(list_of_counts):
    list_all_counts = [sum([elem[i] for elem in list_of_counts]) for i in range(0, len(list_of_counts[0]))]
    return list_all_counts


def sum_all_posts_with_happy_in_for_years(collections):
    list_of_counts = [collection.find({"text": {'$regex': 'happy'}}).count() for collection in collections]
    return list_of_counts


def sum_all_posts_with_angry_in_for_years(collections):
    list_of_counts = [collection.find({"text": {'$regex': 'angry'}}).count() for collection in collections]
    return list_of_counts
