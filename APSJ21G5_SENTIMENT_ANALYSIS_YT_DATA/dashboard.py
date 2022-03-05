import textblob as tb
import matplotlib.pyplot as plt
import numpy as np
import csv
def main_sa():
    print("ENTER 1 TO SHOW POSITIVE:\r\nENTER 2 TO SHOW NEGATIVE:\r\nENTER 3 TO SHOW NEUTRAL:\r\nENTER 4 TO SHOW SCATTER CHART:\r\nENTER 5 TO SHOW BAR CHART:\r\nENTER 6 TO EXIT:")
    delimiters = ["[", "'", "]", "(", ")"]
    pos = 0
    neg = 0
    neu = 0
    y = []
    a = int(input())

    with open('yt_comments.csv', 'r',errors='ignore') as file:
        reader = csv.reader(file)
        for row in reader:
            data = row
            string_data = str(data)

            for i in delimiters:
                string_data = string_data.replace(i, '')
            input_to_textblob = tb.TextBlob(string_data)
            sentence_polarity = input_to_textblob.sentiment.polarity

            if (sentence_polarity > 0):
                y.append(sentence_polarity)
                pos += 1
            elif (sentence_polarity == 0):
                y.append(sentence_polarity)
                neu += 1
            elif (sentence_polarity < 0):
                y.append(sentence_polarity)
                neg += 1

    if a == 1:
        print("++++++++++++++++++++++++++\n   Total Positive: ",pos,"\n++++++++++++++++++++++++++")
        main_sa()
    elif a == 2:
        print("++++++++++++++++++++++++++\n   Total Negative: ", neg,"\n++++++++++++++++++++++++++")
        main_sa()
    elif a == 3:
        print("++++++++++++++++++++++++++\n   Total Neutral: ", neu, "\n++++++++++++++++++++++++++")
        main_sa()
    elif a == 4:
        x = np.random.normal(min(y), max(y), len(y))
        plt.scatter(x, y)
        plt.savefig("scatter_sentiment_analysis.pdf")
        plt.show()
        main_sa()
    elif a == 5:
       x=[5,10,15]
       y=[pos,neg,neu]
       plt.bar(x,y,color=['g','r','k'])
       plt.xticks(x,['+VE','-VE','NEUTRAL'])
       plt.savefig("bar_sentiment_analysis.pdf")
       plt.show()
       main_sa()
    elif a==6:
        exit()
