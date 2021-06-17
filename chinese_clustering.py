#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import fasttext
import fasttext.util
import numpy as np
from sklearn.cluster import KMeans

def main():
    ft = fasttext.load_model('cc.zh.300.bin')
    with open ('ChineseModernVocab.txt') as f:
        lines = f.readlines()

    # list of all vocab words from the input file
    common_words = []

    # list of the frequency rank of the vocab words
    # the order of word_freqs matches the order of common_words
    word_freqs = []

    # read the words and frequency ranks from the input file
    for line in lines:
        split_line = line.split('\t')
        line_word = split_line[0]
        line_freq = split_line[-1]
        common_words.append(line_word)
        word_freqs.append(int(line_freq.strip()))

    # number of vocab words read from the input file
    word_count = len(common_words)

    # number of dimensions in the vector representation of the words in the fasttext model ft
    dimension = len(ft.get_word_vector(common_words[0]))

    # dictionary mapping from word vectors to words
    vector_to_word = {}

    # NumPy matrix whose rows are the vocab words
    word_matrix = np.zeros((word_count, dimension))

    # populate the matrix of vocab words and the dictionary mapping word vectors to words
    for word_idx in range(word_count):
        word = common_words[word_idx]
        word_vector = ft.get_word_vector(word)
        word_matrix[word_idx, :] = word_vector
        vector_to_word[np.array2string(word_matrix[word_idx, :])] = word

    # k means clustering parameters
    num_init = 1
    num_clusters = 2
    cluster_size = 20
    # use the same rand_state each time so the output is the same every time
    rand_state = 0

    # start stopwatch
    start_time = time.time()

    # use k means clustering algorithm for the first division of the words into separate top-level clusters
    # https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans
    kmeans = KMeans(n_init = num_init, n_clusters = num_clusters, random_state = rand_state).fit(word_matrix)

    # global list of labels
    labels = kmeans.labels_

    # histogram of how many words have each label
    bin_count = np.bincount(labels)

    # the highest label number used
    max_cluster_number = np.amax(labels)

    # the label with the most words in its cluster
    max_label = bin_count.argmax()

    # the number of words in the largest cluster
    max_freq = bin_count[max_label]

    # iteratively run k means clustering on the largest cluster until all clusters are less than the maximum permitted size
    while max_freq > cluster_size:
        # the indices of the words in the largest cluster
        max_label_indices = np.where(labels == max_label)
        max_label_indices = max_label_indices[0]

        # matrix whose rows are only the words that are in the largest cluster
        largest_cluster = word_matrix[max_label_indices]

        # size of the largest cluster
        max_label_count = len(max_label_indices)

        # run k means clustering on the largest cluster
        sub_kmeans = KMeans(n_init = num_init, n_clusters = num_clusters, random_state = rand_state).fit(largest_cluster)

        # local list of labels for this iteration
        sub_labels = sub_kmeans.labels_

        # if k means returned just one cluster, manually separate the words into clusters of the desired size
        if np.amax(sub_labels) == 0:
            for label_idx in range(max_label_count):
                sub_labels[label_idx] = label_idx // cluster_size

        # update the global labels based on the sub-cluster labels
        for label_idx in range(max_label_count):
            sub_label = sub_labels[label_idx]

            # if the sub-cluster label is 0, then keep the original label value
            # else, use a new label not previously used without skipping over any label numbers
            if sub_label != 0:
                labels[max_label_indices[label_idx]] = max_cluster_number + sub_label

        # update variables for the next loop iteration
        bin_count = np.bincount(labels)
        max_label = bin_count.argmax()
        max_cluster_number = np.amax(labels)
        max_freq = bin_count[max_label]

    # use the stopwatch to output how long the algorithm took to run
    print(" --- %s seconds --- " % (time.time() - start_time))

    num_of_clusters = max_cluster_number + 1

    # each of these variables is a list of lists, used to map the index label to a list
    
    # mapping from label (list index) to the vocab frequency values of all words in the label's cluster
    labels_to_freqs = [ [] for _ in range(num_of_clusters) ]

    # mapping from label (list index) to the mean frequency value of the words in the label's cluster
    labels_to_means = [ [] for _ in range(num_of_clusters) ]

    # mapping from label (list index) to the list of words in the label's cluster
    labels_to_words = [ [] for _ in range(num_of_clusters) ]

    # populate labels_to_freqs and labels_to_words
    for label_idx in range(word_count):
        curr_word = str(vector_to_word[np.array2string(word_matrix[label_idx, :])])
        word_idx = common_words.index(curr_word)
        word_freq = word_freqs[word_idx]
        curr_label = int(labels[label_idx])
        labels_to_freqs[curr_label].append(word_freq)
        labels_to_words[curr_label].append(curr_word)

    # populate labels_to_means
    for label_idx in range (num_of_clusters):
        labels_to_means[label_idx] = np.mean(labels_to_freqs[label_idx])

    # retrieve the ordered list of indices, used to sort clusters by the mean word frequency of the words in the cluster
    sorted_labels = np.argsort(labels_to_means)

    # print the words in each cluster, ordered by the mean word frequency of the clusters
    for label in sorted_labels:
        for word in labels_to_words[label]:
            word_idx = common_words.index(word)
            word_freq = word_freqs[word_idx]
            print("Word: " + word + "\tFrequency: " + str(word_freq) + "\tLabel: " + str(label))

if __name__ == '__main__':
    main()
