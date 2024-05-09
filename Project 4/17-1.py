import requests
import plotly.express as px

languages = ['javascript', 'ruby', 'c', 'java', 'perl', 'haskell', 'go']

for lang in languages:
    url = f"https://api.github.com/search/repositories?q=language:{lang}+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code for {lang}: {r.status_code}")

    response_dict = r.json()
    print(response_dict.keys())
    print(f"Total repositories for {lang}: {response_dict['total_count']}")
    print(f"Complete results for {lang}: {not response_dict['incomplete_results']}")

    repo_dicts = response_dict['items']
    repo_links, stars, hover_texts = [], [], []

    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        hover_text = f"{owner}<br />{description}"
        hover_texts.append(hover_text)

    title = f"Most-Starred {lang.upper()} Projects on GitHub"
    labels = {'x': 'Repository', 'y': 'Stars'}
    fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)
    fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
    fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
    fig.show()