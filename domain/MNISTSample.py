"""
Name - Karan Patel, PSU ID - 965051876

Class that represents a sample from the MNIST dataset
"""

import csv
import logging
import random

import numpy as np


class MNISTSample:
    logger = logging.getLogger('MINSTSample')
    expected_features = 784

    def __init__(self, sample_number, true_class_label, features):
        assert type(sample_number) is int, 'Sample number not found!'
        assert 0 <= true_class_label <= 9, 'Expected true class label to be between 0 and 9 for sample #{}'.format(sample_number)
        assert len(features) == 784, 'Expected exactly {} features for sample #{}'.format(MNISTSample.expected_features, sample_number)

        self.sample_number = sample_number
        self.true_class_label = int(true_class_label)
        self.features = features

    def __str__(self):
        return "Sample #{} : true class label = {}, features = {}".format(self.sample_number, self.true_class_label,
                                                                        self.features)

    @staticmethod
    def load_and_shuffle_samples_from_dataset(dataset_file_location, scaling_factor=255, shuffle_samples=True):
        """
        :param scaling_factor features to be scaled by dividing them by scaling_factor
        :param dataset_file_location
        :param shuffle_samples
        :return: list of samples scaled and loaded from dataset_file_location
        """
        MNISTSample.logger.info('Loading samples from {} ...'.format(dataset_file_location))

        with open(dataset_file_location) as csv_file:
            samples = [MNISTSample(row_num, int(row[0]), (np.array(row[1:], dtype=np.double) / scaling_factor)) for row_num, row in enumerate(csv.reader(csv_file))]

        if shuffle_samples:
            random.shuffle(samples)

        MNISTSample.logger.info('Found {} samples in {}'.format(len(samples), dataset_file_location))
        return samples
