import requests
import matplotlib.pyplot as plt
from operator import itemgetter

url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

submission_ids = r.json()

submission_dicts = []
for submission_id in submission_ids[:5]:
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()

        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submission_dicts.append(submission_dict)
    except KeyError:
        pass

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

titles = [submission_dict['title'] for submission_dict in submission_dicts]
links = [submission_dict['hn_link'] for submission_dict in submission_dicts]
comments = [submission_dict['comments'] for submission_dict in submission_dicts]

plt.figure(figsize=(10, 6))
plt.barh(titles, comments, color='skyblue')
plt.xlabel('Number of Comments')
plt.ylabel('Submission Title')
plt.title('Most Active Discussions on Hacker News')
plt.gca().invert_yaxis()

for i, link in enumerate(links):
    plt.text(5, i, link, color='blue', va='center')

plt.tight_layout()
plt.show()
