# GitHub Repository Analyzer

A Python command-line application that analyzes a public GitHub user and their repositories using the GitHub REST API.

## Project Goal

The goal of this project is to practice working with:

- HTTP requests
- REST APIs
- JSON data
- API authentication
- Environment variables
- Error handling
- Pagination
- Python modules and functions
- Logging
- Automated testing with pytest
- Git and GitHub

## Features

- Search for a GitHub user by username
- Display basic user information:
  - Username
  - Followers
  - Following
  - Number of public repositories
- Fetch all public repositories using pagination
- Display:
  - Repository name
  - Star count
  - Primary programming language
- Calculate:
  - Total stars
  - Average stars per repository
  - Most-starred repository
  - Programming language usage
  - Most-used programming language
- Handle:
  - Invalid usernames
  - Connection errors
  - Request timeouts
  - HTTP errors
  - Missing repository data
  - Users with no public repositories
- Store the GitHub API token securely using environment variables
- Log application errors
- Test analysis functions with pytest

## Project Structure

```text
github-repository-analyzer/
│
├── main.py
├── github_api.py
├── analysis.py
├── config.py
├── requirements.txt
│
├── tests/
│   └── test_analysis.py
│
├── images/
│   ├── analyzer-output.png
│   └── tests-passed.png
│
├── .env.example
├── .gitignore
└── README.md