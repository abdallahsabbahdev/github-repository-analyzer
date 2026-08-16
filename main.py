import logging

import requests

from github_api import get_user, get_repositories
from analysis import (
    calculate_total_stars,
    calculate_average_stars,
    get_top_repository,
    count_languages,
    get_top_language,
)


logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def display_user(user_data):
    """Display basic GitHub user information."""

    print("\n===== GitHub User =====")

    print(
        f"Username: "
        f"{user_data.get('login', 'Unknown')}"
    )

    print(
        f"Followers: "
        f"{user_data.get('followers', 0)}"
    )

    print(
        f"Following: "
        f"{user_data.get('following', 0)}"
    )

    print(
        f"Public repositories: "
        f"{user_data.get('public_repos', 0)}"
    )


def display_repositories(repos):
    """Display repository information."""

    print("\n===== Repositories =====")

    for repo in repos:
        name = repo.get("name", "Unknown")
        stars = repo.get("stargazers_count", 0)
        language = repo.get("language") or "Unknown"

        print(
            f"Repository: {name} | "
            f"Stars: {stars} | "
            f"Language: {language}"
        )


def display_analysis(repos):
    """Display repository statistics."""

    total_stars = calculate_total_stars(repos)

    average_stars = calculate_average_stars(repos)

    top_repo = get_top_repository(repos)

    language_counts = count_languages(repos)

    top_language = get_top_language(language_counts)

    print("\n===== Repository Analysis =====")

    print(f"Repositories analyzed: {len(repos)}")

    print(f"Total stars: {total_stars}")

    print(
        f"Average stars per repository: "
        f"{average_stars:.2f}"
    )


    if top_repo is not None:
        top_repo_stars = top_repo.get(
            "stargazers_count",
            0,
        )

        if top_repo_stars > 0:
            print("\nMost Starred Repository:")

            print(
                f"Name: "
                f"{top_repo.get('name', 'Unknown')}"
            )

            print(
                f"Stars: {top_repo_stars}"
            )

        else:
            print(
                "\nNo repositories have "
                "received stars yet."
            )


    if top_language is not None:
        print("\nLanguage Analysis:")

        for language, count in language_counts.items():
            print(f"{language}: {count}")

        print(
            f"\nMost Used Language: "
            f"{top_language}"
        )

        print(
            f"Repositories Using It: "
            f"{language_counts[top_language]}"
        )

    else:
        print("\nNo language data available.")


def main():
    """Run the GitHub Repository Analyzer."""

    username = input(
        "Enter GitHub username: "
    ).strip()

    if not username:
        print("Username cannot be empty.")
        return

    try:
        user_data = get_user(username)

        repos = get_repositories(username)

        display_user(user_data)

        if not repos:
            print(
                "\nNo public repositories found."
            )

            return

        display_repositories(repos)

        display_analysis(repos)

    except requests.exceptions.Timeout:
        logging.exception(
            "GitHub request timed out."
        )

        print(
            "GitHub request timed out."
        )

    except requests.exceptions.ConnectionError:
        logging.exception(
            "Could not connect to GitHub."
        )

        print(
            "Could not connect to GitHub."
        )

    except requests.exceptions.HTTPError as error:
        logging.exception(
            "GitHub returned an HTTP error."
        )

        if (
            error.response is not None
            and error.response.status_code == 404
        ):
            print(
                "GitHub user not found."
            )

        else:
            print(
                "GitHub returned an HTTP error."
            )

    except requests.exceptions.RequestException:
        logging.exception(
            "GitHub request failed."
        )

        print(
            "Something went wrong "
            "with the request."
        )

    except RuntimeError as error:
        logging.exception(
            "Configuration error."
        )

        print(error)


if __name__ == "__main__":
    main()