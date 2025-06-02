import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


import keras
#import keras_tuner as kt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, SimpleRNN, TimeDistributed, Dropout, Bidirectional, GRU
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from keras.callbacks import EarlyStopping
from tensorflow.keras.utils import plot_model

from sklearn.linear_model import Ridge
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_validate, train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error

import itertools

from scipy.stats import linregress
import seaborn as sns


import datetime

