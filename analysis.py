def calculate_total_stars(repos):
    """Calculate the total number of stars across repositories."""

    return sum(
        repo.get("stargazers_count", 0)
        for repo in repos
    )


def calculate_average_stars(repos):
    """Calculate the average number of stars per repository."""

    if not repos:
        return 0.0

    total_stars = calculate_total_stars(repos)

    return total_stars / len(repos)


def get_top_repository(repos):
    """Return the repository with the highest star count."""

    if not repos:
        return None

    return max(
        repos,
        key=lambda repo: repo.get("stargazers_count", 0),
    )


def count_languages(repos):
    """Count how many repositories use each primary language."""

    language_counts = {}

    for repo in repos:
        language = repo.get("language")

        if language is not None:
            language_counts[language] = (
                language_counts.get(language, 0) + 1
            )

    return language_counts


def get_top_language(language_counts):
    """Return the most frequently used language."""

    if not language_counts:
        return None

    return max(
        language_counts,
        key=lambda language: language_counts[language],
    )