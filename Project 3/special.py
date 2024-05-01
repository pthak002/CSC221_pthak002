import matplotlib.pyplot as plt

# Fictional data for programming languages and the number of repositories
languages = ['Python', 'JavaScript', 'Java', 'C++', 'C#', 'PHP', 'Ruby', 'Go']
repositories = [1500000, 2000000, 1800000, 1000000, 900000, 800000, 700000, 6000]

plt.figure(figsize=(12, 6))
plt.bar(languages, repositories, color='skyblue')
plt.title('Number of GitHub Repositories by Programming Language')
plt.xlabel('Programming Language')
plt.ylabel('Number of Repositories')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('special.png')
plt.show()
