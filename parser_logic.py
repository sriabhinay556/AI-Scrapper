open_issues = [
    {
        "repo_name": "CorsixTH / CorsixTH",
        "issues_count": "10 issues",
        "description": "Open source clone of",
        "language": "Lua",
        "stars": "4.02K",
        "last_activity": "2 days ago"
    },
    {
        "repo_name": "tarantool / tarantoo",
        "issues_count": "10 issues",
        "description": "Get your data in RAM",
        "language": "Lua",
        "stars": "3.4K",
        "last_activity": "3 days ago"
    }
]

for issue in open_issues:
    if issue["language"] == "Lua" and float(issue["stars"][:-1]) < 5:
        print(f'Repo: {issue["repo_name"]}')
        print(f'Issues: {issue["issues_count"]}')
        print(f'Description: {issue["description"]}')
        print(f'Stars: {issue["stars"]}')
        print(f'Last Activity: {issue["last_activity"]}')