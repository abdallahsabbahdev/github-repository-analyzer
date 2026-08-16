import logging

import requests

from config import (
    GITHUB_TOKEN,
    GITHUB_API_URL,
    REQUEST_TIMEOUT,
    REPOS_PER_PAGE,
)


logger = logging.getLogger(__name__)


def get_headers():
    if not GITHUB_TOKEN:
        raise RuntimeError(
            "GITHUB_TOKEN is missing. Add it to your .env file."
        )

    return {
        "Accept": "application/json",
        "Authorization": f"Bearer {GITHUB_TOKEN}",
    }


def get_user(username):
    """Fetch information about a GitHub user."""

    url = f"{GITHUB_API_URL}/users/{username}"

    logger.info("Fetching GitHub user: %s", username)

    response = requests.get(
        url,
        headers=get_headers(),
        timeout=REQUEST_TIMEOUT,
    )

    response.raise_for_status()

    return response.json()


def get_repositories(username):
    """Fetch all public repositories for a GitHub user."""

    url = f"{GITHUB_API_URL}/users/{username}/repos"

    page = 1
    all_repos = []

    while True:
        params = {
            "per_page": REPOS_PER_PAGE,
            "page": page,
        }

        response = requests.get(
            url,
            headers=get_headers(),
            params=params,
            timeout=REQUEST_TIMEOUT,
        )

        response.raise_for_status()

        page_repos = response.json()

        if not page_repos:
            break

        all_repos.extend(page_repos)

        page += 1

    logger.info(
        "Fetched %s repositories for %s",
        len(all_repos),
        username,
    )

    return all_repos