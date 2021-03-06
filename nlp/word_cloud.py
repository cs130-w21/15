import os

import numpy as np
import matplotlib.pyplot as plt
import spacy
from wordcloud import WordCloud

# Run the folling command to instll english model for the first time
# python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")


def remove_stop_words(article):
    """Remove stop words from an article, as they should not be shown on the
       word cloud
    :param article: a string representing the article
    :returns: the filtered tokens for the input article
    :rtype: a list of string
    """
    doc = nlp(article.lower())
    filtered_tokens = []
    for word in doc:
        if word.text not in nlp.Defaults.stop_words:
            if word.text not in ',.!?':
                filtered_tokens.append(word.text)

    return filtered_tokens

def plot_word_cloud(artcile, target_path='figs/cloud.png'):
    """Plot word cloud and save it to a local file
    :param: artcile: a string representing the article
    :param: target_path: the path to save word cloud figure
    :return: None
    """
    tokens = remove_stop_words(artcile)
    article = ' '.join(tokens)
    wordcloud = WordCloud(width=1600,
                          height=800,
                          background_color="white").generate(article)
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(target_path, bbox_inches='tight', dpi=500)
    # plt.show()

# plot_word_cloud('This article is a sample article.')