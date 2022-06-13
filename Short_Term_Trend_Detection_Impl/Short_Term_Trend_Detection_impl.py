import pandas as pd

import numpy as np
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import pairwise_distances
import sys
import csv
import json

considered_rows = []



def find_all_clusters(keywords, scores):
    
    number_of_titles = len(keywords)
    keyword_score = np.array(scores).reshape(number_of_titles, 1)
    cluster = AgglomerativeClustering(n_clusters=None, affinity='euclidean', linkage='average', distance_threshold=0.5)
    cluster.fit(keyword_score)
    labels = cluster.labels_
    final_topics = []
    for index in range(cluster.n_clusters_):
        topics = []
        for i, val in enumerate(labels):
            if val == index:
                topics.append(keywords[i])
        final_topics.append(topics)
    return final_topics


def generate_ngrams(text):
    n_grams = ngrams(nltk.word_tokenize(text), 3)#Change based on the ngrams
    return [' '.join(grams) for grams in n_grams]


def sports_trends():
    tweetsS = pd.read_csv(r'DataSet_5_Aggregated_Sports.csv')
    find_sports_trends(tweetsS)

def politics_trends():
    tweetsP = pd.read_csv(r'Weighted_Aggregated_Politic_Tweets_2.csv')
    find_politic_trends(tweetsP)


def entertainment_trends():
    tweetsE = pd.read_csv(r'Weighted_Aggregated_Entertainment_Tweets_2.csv')
    find_entertainment_trends(tweetsE)

def crime_trends():
    tweetsC = pd.read_csv(r'Weighted_Aggregated_Crime_Tweets_2.csv')
    find_crime_trends(tweetsC)

def other_trends():
    tweetsO = pd.read_csv(r'Weighted_Aggregated_Other_Tweets_2.csv')
    find_other_trends(tweetsO)

def find_trends(tweets):
    df = pd.DataFrame(tweets, columns=['created_at', 'text'])
    df["text"] = df["text"].apply(lambda x: generate_ngrams(x))

    inp = {}
    for index in df.index:
        inp[df["created_at"][index]] = df["text"][index]

    number_of_days = df.shape[0]
    day_one = df.iloc[0, df.columns.get_loc('created_at')]
    count = {}

    for dateIdx, date in enumerate(sorted(inp)):
        for keywordIndex, keyword in enumerate(inp[date]):
            if keyword not in count:
                count[keyword] = [0] * number_of_days
            count[keyword][dateIdx] += 1

    res = {}
    dates = sorted(inp.keys())
    for date in dates:
        res[date] = {}

    for keyword in count:
        for cIndex, c in enumerate(count[keyword]):
            if cIndex > 0 and count[keyword][cIndex] > 0:
                res[dates[cIndex]][keyword] = round(
                    (count[keyword][cIndex] + 1) / (np.log((sum(count[keyword][0:cIndex]) / cIndex) + 1) + 1), 2)

    del res[day_one]

    for key, val in res.items():
        keywords = []
        scores = []
        for index in val:
            keywords.append(index)
            scores.append(val[index])

        for i in find_all_clusters(keywords, scores):
            Response = list(dict.fromkeys(w for s in i for w in s.split()))
            considered_rows.append([key, Response])
            df = pd.DataFrame(considered_rows, columns=["Date", "Text"])
            df.to_csv("output.csv", index=False)
            print(key, Response)
        print("_________________________________________________________")

def find_sports_trends(tweets):
    df = pd.DataFrame(tweets, columns=['created_at', 'text'])
    df["text"] = df["text"].apply(lambda x: generate_ngrams(x))

    inp = {}
    for index in df.index:
        inp[df["created_at"][index]] = df["text"][index]

    number_of_days = df.shape[0]
    # print(number_of_days)
    day_one = df.iloc[0, df.columns.get_loc('created_at')]
    count = {}

    for dateIdx, date in enumerate(sorted(inp)):
        for keywordIndex, keyword in enumerate(inp[date]):
            if keyword not in count:
                count[keyword] = [0] * number_of_days
            count[keyword][dateIdx] += 1

    res = {}
    dates = sorted(inp.keys())
    for date in dates:
        res[date] = {}

    for keyword in count:
        for cIndex, c in enumerate(count[keyword]):
            if cIndex > 0 and count[keyword][cIndex] > 0:
                res[dates[cIndex]][keyword] = round(
                    (count[keyword][cIndex] + 1) / (np.log((sum(count[keyword][0:cIndex]) / cIndex) + 1) + 1), 2)

    del res[day_one]

    for key, val in res.items():
        keywords = []
        scores = []
        for index in val:
            keywords.append(index)
            scores.append(val[index])

        for i in find_all_clusters(keywords, scores):
            Response = list(dict.fromkeys(w for s in i for w in s.split()))
            considered_rows.append([key, Response])
            df = pd.DataFrame(considered_rows, columns=["Date", "Text"])
            df.to_csv("outputSports.csv", index=False)
            print(key, Response)
        print("_________________________________________________________")

def find_politic_trends(tweets):
    df = pd.DataFrame(tweets, columns=['created_at', 'text'])
    df["text"] = df["text"].apply(lambda x: generate_ngrams(x))

    inp = {}
    for index in df.index:
        inp[df["created_at"][index]] = df["text"][index]

    number_of_days = df.shape[0]
    day_one = df.iloc[0, df.columns.get_loc('created_at')]
    count = {}

    for dateIdx, date in enumerate(sorted(inp)):
        for keywordIndex, keyword in enumerate(inp[date]):
            if keyword not in count:
                count[keyword] = [0] * number_of_days
            count[keyword][dateIdx] += 1

    res = {}
    dates = sorted(inp.keys())
    for date in dates:
        res[date] = {}

    for keyword in count:
        for cIndex, c in enumerate(count[keyword]):
            if cIndex > 0 and count[keyword][cIndex] > 0:
                res[dates[cIndex]][keyword] = round(
                    (count[keyword][cIndex] + 1) / (np.log((sum(count[keyword][0:cIndex]) / cIndex) + 1) + 1), 2)

    del res[day_one]
    # print(res)
    for key, val in res.items():
        keywords = []
        scores = []
        for index in val:
            keywords.append(index)
            scores.append(val[index])
        for i in find_all_clusters(keywords, scores):
            Response = list(dict.fromkeys(w for s in i for w in s.split()))
            considered_rows.append([key, Response])
            df = pd.DataFrame(considered_rows, columns=["Date", "Text"])
            df.to_csv("outputPolitics.csv", index=False)
            print(key, Response)
        print("_________________________________________________________")

def find_entertainment_trends(tweets):
    df = pd.DataFrame(tweets, columns=['created_at', 'text'])
    df["text"] = df["text"].apply(lambda x: generate_ngrams(x))

    inp = {}
    for index in df.index:
        inp[df["created_at"][index]] = df["text"][index]

    number_of_days = df.shape[0]
    day_one = df.iloc[0, df.columns.get_loc('created_at')]
    count = {}

    for dateIdx, date in enumerate(sorted(inp)):
        for keywordIndex, keyword in enumerate(inp[date]):
            if keyword not in count:
                count[keyword] = [0] * number_of_days
            count[keyword][dateIdx] += 1

    res = {}
    dates = sorted(inp.keys())
    for date in dates:
        res[date] = {}

    for keyword in count:
        for cIndex, c in enumerate(count[keyword]):
            if cIndex > 0 and count[keyword][cIndex] > 0:
                res[dates[cIndex]][keyword] = round(
                    (count[keyword][cIndex] + 1) / (np.log((sum(count[keyword][0:cIndex]) / cIndex) + 1) + 1), 2)

    del res[day_one]
    # print(res)
    for key, val in res.items():
        keywords = []
        scores = []
        for index in val:
            keywords.append(index)
            scores.append(val[index])
        for i in find_all_clusters(keywords, scores):
            Response = list(dict.fromkeys(w for s in i for w in s.split()))
            considered_rows.append([key, Response])
            df = pd.DataFrame(considered_rows, columns=["Date", "Text"])
            df.to_csv("outputEntertainment.csv", index=False)
            print(key, Response)
        print("_________________________________________________________")

def find_crime_trends(tweets):
    df = pd.DataFrame(tweets, columns=['created_at', 'text'])
    df["text"] = df["text"].apply(lambda x: generate_ngrams(x))

    inp = {}
    for index in df.index:
        inp[df["created_at"][index]] = df["text"][index]

    number_of_days = df.shape[0]
    day_one = df.iloc[0, df.columns.get_loc('created_at')]
    count = {}

    for dateIdx, date in enumerate(sorted(inp)):
        for keywordIndex, keyword in enumerate(inp[date]):
            if keyword not in count:
                count[keyword] = [0] * number_of_days
            count[keyword][dateIdx] += 1

    res = {}
    dates = sorted(inp.keys())
    for date in dates:
        res[date] = {}

    for keyword in count:
        for cIndex, c in enumerate(count[keyword]):
            if cIndex > 0 and count[keyword][cIndex] > 0:
                res[dates[cIndex]][keyword] = round(
                    (count[keyword][cIndex] + 1) / (np.log((sum(count[keyword][0:cIndex]) / cIndex) + 1) + 1), 2)

    del res[day_one]
    # print(res)
    for key, val in res.items():
        keywords = []
        scores = []
        for index in val:
            keywords.append(index)
            scores.append(val[index])
        for i in find_all_clusters(keywords, scores):
            Response = list(dict.fromkeys(w for s in i for w in s.split()))
            considered_rows.append([key, Response])
            df = pd.DataFrame(considered_rows, columns=["Date", "Text"])
            df.to_csv("outputCrime.csv", index=False)
            print(key, Response)
        print("_________________________________________________________")
def find_other_trends(tweets):
    df = pd.DataFrame(tweets, columns=['created_at', 'text'])
    df["text"] = df["text"].apply(lambda x: generate_ngrams(x))

    inp = {}

    for index in df.index:
        inp[df["created_at"][index]] = df["text"][index]

    number_of_days = df.shape[0]
    day_one = df.iloc[0, df.columns.get_loc('created_at')]
    count = {}

    for dateIdx, date in enumerate(sorted(inp)):
        for keywordIndex, keyword in enumerate(inp[date]):
            if keyword not in count:
                count[keyword] = [0] * number_of_days
            count[keyword][dateIdx] += 1

    res = {}
    dates = sorted(inp.keys())
    for date in dates:
        res[date] = {}

    for keyword in count:
        for cIndex, c in enumerate(count[keyword]):
            if cIndex > 0 and count[keyword][cIndex] > 0:
                res[dates[cIndex]][keyword] = round(
                    (count[keyword][cIndex] + 1) / (np.log((sum(count[keyword][0:cIndex]) / cIndex) + 1) + 1), 2)

    del res[day_one]

    for key, val in res.items():
        keywords = []
        scores = []
        for index in val:
            keywords.append(index)
            scores.append(val[index])
        for i in find_all_clusters(keywords, scores):
            Response = list(dict.fromkeys(w for s in i for w in s.split()))
            considered_rows.append([key, Response])
            df = pd.DataFrame(considered_rows, columns=["Date", "Text"])
            df.to_csv("outputOther.csv", index=False)
            print(key, Response)
        print("_________________________________________________________")


def filterData():
    tweets = pd.read_csv(r'FinalListPreprocessedDataNew.csv')
    df = pd.DataFrame(tweets, columns=['CREATED_AT', 'STEMMING WORDS', 'LABEL', 'RETWEET COUNT'])
    # df['CREATED_AT'] = pd.to_datetime(df['CREATED_AT'])
    df['CREATED_AT'] = pd.to_datetime(df['CREATED_AT'])
    df = df.sort_values(by='CREATED_AT')

    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    dict = {'CREATED_AT': 'created_at',
            'LABEL': 'label',
            'STEMMING WORDS': 'text',
            'RETWEET COUNT': 'retweet_count'
            }
    # call rename () method
    df.rename(columns=dict,
              inplace=True)
    # df['created_at'] = df['CREATED_AT'].apply(lambda x: str(x))
    # df['label'] = df['LABEL'].apply(lambda x: str(x))
    # df['tweet'] = df['STEMMING WORDS'].apply(lambda x: str(x))
    # df['retweet_count'] = df['RETWEET COUNT'].apply(lambda x: str(x))
    return df
    print(df)


def similarity():
    tweets = pd.read_csv(r'DataSet_2_Sorted_Date_Wise.csv')
    # pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    df = pd.DataFrame(tweets, columns=['created_at', 'text', 'label', 'retweet_count'])
    df['created_at'] = pd.to_datetime(df['created_at']).dt.date
    # df['likes_count'] = pd.(df['likes_count'])
    df['retweet_count'] = df['retweet_count'].apply(lambda x: str(x))

    df['text'] = df['text'].apply(lambda x: str(x))
    df["text"] = df["text"].apply(lambda x: replacesynonyms(x))
    df['label'] = df['label'].apply(lambda x: str(x))

    return df


def create_sets():
    lists_sets = []
    file = open('new_syn.txt', 'r', encoding="utf8")
    lines = file.readlines()
    for line in lines:
        s = set()
        words = line.split(',')
        for word in words:
            s.add(word.strip())
        lists_sets.append(s)
    return lists_sets


def create_syn_list():
    first_syn_name = []
    file = open('new_syn.txt', 'r', encoding="utf8")
    lines = file.readlines()
    for line in lines:
        first_syn_name.append(line.split(',')[0].strip())
    return first_syn_name


lists_sets = create_sets()
first_syn_list = create_syn_list()


def replacesynonyms(tweet):
    words = tweet.split()
    new_sentence_l = []
    for word in words:
        to_add = True
        for idx, syn_set in enumerate(lists_sets):
            if word in syn_set:
                new_sentence_l.append(first_syn_list[idx])
                to_add = False
                break
        if to_add:
            new_sentence_l.append(word)
    return ' '.join(new_sentence_l)


def saveFile():
    df = pd.read_csv('DataSet_3_Synonyms_Considered.csv');
    categories = df['label'].unique()
    for category in categories:
        df[df['label'] == category].to_csv(category + '.csv', index=False, header=True)


def weightSportsReTweets():
    df = pd.read_csv(r'Sport.csv')
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['label'] = df['label'].apply(lambda x: str(x))

    # df = df.loc[df.index.repeat(df.pop('retweet_count') + 1)].reset_index(drop=True)
    df = df.loc[df.index.repeat(df.pop('retweet_count') + 1)].reset_index(drop=True)
    # print(df)
    return df


def aggregatedSports():
    tweets = pd.read_csv(r'DataSet_4_Retweet_Considered.csv')
    df = pd.DataFrame(tweets, columns=['created_at', 'text', 'label'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    # df['created_at'] = pd.to_datetime(df['created_at'])
    # df['tweet'] = df['tweet'].apply(lambda x: str(x))
    # df['category'] = df['category'].apply(lambda x: str(x))
    # pd.set_option('display.max_colwidth', 0)
    # df = df.groupby(pd.Grouper(key='created_at', freq='1D')).agg(lambda x: ' '.join(set(x)))
    out = df.groupby(['created_at', 'label'], sort=False, as_index=False)['text'] \
        .apply(lambda x: ' '.join(x))[df.columns]
    out = out.reindex(columns=["created_at", "text", "label"])
    # print(out)
    return out


def weightCrimeReTweets():
    df = pd.read_csv(r'Crime.csv')
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['label'] = df['label'].apply(lambda x: str(x))

    # df = df.loc[df.index.repeat(df.pop('retweet_count') + 1)].reset_index(drop=True)
    df = df.loc[df.index.repeat(df.pop('retweet_count') + 1)].reset_index(drop=True)
    # print(df)
    return df


def aggregatedCrime():
    tweets = pd.read_csv(r'Weighted_Crime_Tweets_1.csv')
    df = pd.DataFrame(tweets, columns=['created_at', 'text', 'label'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    # df['created_at'] = pd.to_datetime(df['created_at'])
    # df['tweet'] = df['tweet'].apply(lambda x: str(x))
    # df['category'] = df['category'].apply(lambda x: str(x))
    # pd.set_option('display.max_colwidth', 0)
    # df = df.groupby(pd.Grouper(key='created_at', freq='1D')).agg(lambda x: ' '.join(set(x)))
    out = df.groupby(['created_at', 'label'], sort=False, as_index=False)['text'] \
        .apply(lambda x: ' '.join(x))[df.columns]
    out = out.reindex(columns=["created_at", "text", "label"])
    # print(out)
    return out


def weightPoliticReTweets():
    df = pd.read_csv(r'Politics.csv')
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['label'] = df['label'].apply(lambda x: str(x))

    # df = df.loc[df.index.repeat(df.pop('retweet_count') + 1)].reset_index(drop=True)
    df = df.loc[df.index.repeat(df.pop('retweet_count') + 1)].reset_index(drop=True)
    # print(df)
    return df


def aggregatedPolitic():
    tweets = pd.read_csv(r'Weighted_Politic_Tweets_1.csv')
    df = pd.DataFrame(tweets, columns=['created_at', 'text', 'label'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    # df['created_at'] = pd.to_datetime(df['created_at'])
    # df['tweet'] = df['tweet'].apply(lambda x: str(x))
    # df['category'] = df['category'].apply(lambda x: str(x))
    # pd.set_option('display.max_colwidth', 0)
    # df = df.groupby(pd.Grouper(key='created_at', freq='1D')).agg(lambda x: ' '.join(set(x)))
    out = df.groupby(['created_at', 'label'], sort=False, as_index=False)['text'] \
        .apply(lambda x: ' '.join(x))[df.columns]
    out = out.reindex(columns=["created_at", "text", "label"])
    # print(out)
    return out


def weightEntertainmentReTweets():
    df = pd.read_csv(r'Entertainment.csv')
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['label'] = df['label'].apply(lambda x: str(x))

    # df = df.loc[df.index.repeat(df.pop('retweet_count') + 1)].reset_index(drop=True)
    df = df.loc[df.index.repeat(df.pop('retweet_count') + 1)].reset_index(drop=True)
    # print(df)
    return df


def aggregatedEntertainment():
    tweets = pd.read_csv(r'Weighted_Entertainment_Tweets_1.csv')
    df = pd.DataFrame(tweets, columns=['created_at', 'text', 'label'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    # df['created_at'] = pd.to_datetime(df['created_at'])
    # df['tweet'] = df['tweet'].apply(lambda x: str(x))
    # df['category'] = df['category'].apply(lambda x: str(x))
    # pd.set_option('display.max_colwidth', 0)
    # df = df.groupby(pd.Grouper(key='created_at', freq='1D')).agg(lambda x: ' '.join(set(x)))
    out = df.groupby(['created_at', 'label'], sort=False, as_index=False)['text'] \
        .apply(lambda x: ' '.join(x))[df.columns]
    out = out.reindex(columns=["created_at", "text", "label"])
    # print(out)
    return out


def weightOtherReTweets():
    df = pd.read_csv(r'Other.csv')
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['label'] = df['label'].apply(lambda x: str(x))

    # df = df.loc[df.index.repeat(df.pop('retweet_count') + 1)].reset_index(drop=True)
    df = df.loc[df.index.repeat(df.pop('retweet_count') + 1)].reset_index(drop=True)
    # print(df)
    return df


def aggregatedOther():
    tweets = pd.read_csv(r'Weighted_Other_Tweets_1.csv')
    df = pd.DataFrame(tweets, columns=['created_at', 'text', 'label'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    # df['created_at'] = pd.to_datetime(df['created_at'])
    # df['tweet'] = df['tweet'].apply(lambda x: str(x))
    # df['category'] = df['category'].apply(lambda x: str(x))
    # pd.set_option('display.max_colwidth', 0)
    # df = df.groupby(pd.Grouper(key='created_at', freq='1D')).agg(lambda x: ' '.join(set(x)))
    out = df.groupby(['created_at', 'label'], sort=False, as_index=False)['text'] \
        .apply(lambda x: ' '.join(x))[df.columns]
    out = out.reindex(columns=["created_at", "text", "label"])
    # print(out)
    return out


def filterDataOnDate():
    df = pd.read_csv('DataSet_1_Filtered.csv', parse_dates=['created_at'])
    out = df[df['created_at'].between('2021-07-24', '2021-07-31')]
    return out;

def sportTrendsJson():
    df = pd.read_csv("outputSports.csv", encoding='utf-8')
    df = df.sort_values(by='Date')
    df["Category"] = "Sports"
    df.to_csv("outputSportsFinal.csv", index=False)
    with open('outputSportsFinal.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open('outputSports.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)

    # code here

def politicTrendsJson():
    df = pd.read_csv("outputPolitics.csv", encoding='utf-8')
    df = df.sort_values(by='Date')
    df["Category"] = "Politics"
    df.to_csv("outputPoliticsFinal.csv", index=False)
    with open('outputPoliticsFinal.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open('outputPolitics.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)

def entertainmentTrendsJson():
    df = pd.read_csv("outputEntertainment.csv", encoding='utf-8')
    df = df.sort_values(by='Date')
    df["Category"] = "Entertainment"
    df.to_csv("outputEntertainmentFinal.csv", index=False)
    with open('outputEntertainmentFinal.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open('outputEntertainment.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)

def crimeTrendsJson():
    df = pd.read_csv("outputCrime.csv", encoding='utf-8')
    df = df.sort_values(by='Date')
    df["Category"] = "Crime"
    df.to_csv("outputCrimeFinal.csv", index=False)
    with open('outputCrimeFinal.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open('outputCrime.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)

def otherTrendsJson():
    df = pd.read_csv("outputOther.csv", encoding='utf-8')
    df = df.sort_values(by='Date')
    df["Category"] = "Other"
    df.to_csv("outputOtherFinal.csv", index=False)
    with open('outputOtherFinal.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    with open('outputOther.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False)


if __name__ == '__main__':
    # Write a code to get data for specific time period
    # print(filterData())
    filterData().to_csv(r'DataSet_1_Filtered.csv', header=['created_at', 'text', 'label', 'retweet_count'],
                        index=False)
    filterDataOnDate().to_csv('DataSet_2_Sorted_Date_Wise.csv', index=False)
    similarity().to_csv(r'DataSet_3_Synonyms_Considered.csv', index=False, header=True)

    saveFile()
    print("Category wise Files Saved......")

    weightSportsReTweets().to_csv(r'DataSet_4_Retweet_Considered.csv', index=False, header=True)
    aggregatedSports().to_csv(r'DataSet_5_Aggregated_Sports.csv', index=False, header=True)
    print("Sports Aggregation & Retweet Consideration Done....")


    weightCrimeReTweets().to_csv(r'Weighted_Crime_Tweets_1.csv', index=False, header=True)
    aggregatedCrime().to_csv(r'Weighted_Aggregated_Crime_Tweets_2.csv', index=False, header=True)
    print("Crime Aggregation & Retweet Consideration Done....")

    weightPoliticReTweets().to_csv(r'Weighted_Politic_Tweets_1.csv', index=False, header=True)
    aggregatedPolitic().to_csv(r'Weighted_Aggregated_Politic_Tweets_2.csv', index=False, header=True)
    print("Politics Aggregation & Retweet Consideration Done....")

    weightEntertainmentReTweets().to_csv(r'Weighted_Entertainment_Tweets_1.csv', index=False, header=True)
    aggregatedEntertainment().to_csv(r'Weighted_Aggregated_Entertainment_Tweets_2.csv', index=False, header=True)
    print("Entertainment Aggregation & Retweet Consideration Done....")

    weightOtherReTweets().to_csv(r'Weighted_Other_Tweets_1.csv', index=False, header=True)
    aggregatedOther().to_csv(r'Weighted_Aggregated_Other_Tweets_2.csv', index=False, header=True)
    print("Other Aggregation & Retweet Consideration Done....")

    print("Sports Trend detection started")
    sports_trends()
    print("Politics Trend detection started")
    politics_trends()
    print("Entertainment Trend detection started")
    entertainment_trends()
    print("Crime Trend detection started")
    crime_trends()
    print("Other Trend detection started")
    other_trends()
    print("Generating Sports Jsons")
    sportTrendsJson()
    print("Generating Politics Jsons")
    politicTrendsJson()
    print("Generating Entertainment Jsons")
    entertainmentTrendsJson()
    print("Generating Crime Jsons")
    crimeTrendsJson()
    print("Generating Other Jsons")
    otherTrendsJson()
