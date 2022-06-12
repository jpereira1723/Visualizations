import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
import sys
print("Setup Complete")


def init():
    # Path of the file to read
    spotify_filepath = "/Users/jpereira/Desktop/spotify.csv"

    # Read the file into a variable spotify_data
    spotify_data = pd.read_csv(spotify_filepath, index_col="Date", parse_dates=True)
    return spotify_data

def option_one(spotify_data):
    # Line chart showing daily global streams of each song
    sns.lineplot(data=spotify_data)
    plt.show()


def option_two(spotify_data):
    # Set the width and height of the figure
    plt.figure(figsize=(14,6))

    # Add title
    plt.title("Daily Global Streams of Popular Songs in 2017-2018")

    # Line chart showing daily global streams of each song
    sns.lineplot(data=spotify_data)
    plt.show()

def option_three(spotify_data):
    # Set the width and height of the figure
    plt.figure(figsize=(14, 6))

    # Add title
    plt.title("Daily Global Streams of Popular Songs in 2017-2018")

    # Line chart showing daily global streams of 'Shape of You'
    sns.lineplot(data=spotify_data['Shape of You'], label="Shape of You")

    # Line chart showing daily global streams of 'Despacito'
    sns.lineplot(data=spotify_data['Despacito'], label="Despacito")

    # Add label for horizontal data
    plt.xlabel("Date")
    plt.show()



option = sys.argv[1]

spotify_data = init()
options = {0: print("Not appropriate option"),1: option_one(spotify_data), 2: option_two(spotify_data), 3: option_three(spotify_data)}

options[1]()
