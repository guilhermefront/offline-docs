from flask import Flask, request, render_template
import os
from github import Github
from datetime import datetime, timedelta
import openai
import requests
import base64

app = Flask(__name__)

g = Github(login_or_token=os.getenv("GITHUB_API_KEY"))


def fetch_github_markdown_content(repo_owner, repo_name, file_path):
    api_url = (
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
    )
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        content = data.get("content")
        if content:
            # Base64-decode the content
            markdown_content = base64.b64decode(content).decode("utf-8")
            return markdown_content
    else:
        print(f"Failed to fetch content. Error: {response.text}")

    return None


# make it so you can grab everything from nextjs


@app.route("/")
def index():
    # Access github api and scrap a content from a markdown of the nextjs docs.

    # Example usage
    repo_owner = "vercel"
    repo_name = "next.js"
    file_path = "docs/getting-started.md"

    markdown_content = fetch_github_markdown_content(repo_owner, repo_name, file_path)

    if markdown_content:
        # Process and scrape the content as per your requirements
        # You can use a Markdown parser library like 'markdown-it-py' or 'mistune' here
        # For demonstration purposes, let's just print the content
        print(markdown_content)
    return render_template(
        "index.html",
    )
