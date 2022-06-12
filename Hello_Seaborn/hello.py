import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns

print("Setup Complete")

#Path of the file to read
fifa_filepath = "/Users/jpereira/Desktop/fifa.csv"

#Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)

plt.figure(figsize=(16,6))
sns.lineplot(data=fifa_data)
plt.show()
