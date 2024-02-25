import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

print(tips.head())

# sns.displot(tips['total_bill'],kde=True)
# sns.jointplot(x='total_bill', y='tip', data=tips,kind='reg')
sns.pairplot(tips,hue='sex')

plt.tight_layout()
plt.show()
