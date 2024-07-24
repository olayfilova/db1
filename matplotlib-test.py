import matplotlib.pyplot as plt
import seaborn as sns

# Load a sample dataset
data = sns.load_dataset('iris')

# Create a pairplot
sns.pairplot(data)

# Show the plot
plt.show()
