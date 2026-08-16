from analysis import (
    calculate_total_stars,
    calculate_average_stars,
    get_top_repository,
    count_languages,
    get_top_language,
)


def test_calculate_total_stars():
    repos = [
        {"stargazers_count": 5},
        {"stargazers_count": 3},
        {"stargazers_count": 2},
    ]

    result = calculate_total_stars(repos)

    assert result == 10


def test_calculate_total_stars_empty():
    repos = []

    result = calculate_total_stars(repos)

    assert result == 0


def test_calculate_average_stars():
    repos = [
        {"stargazers_count": 10},
        {"stargazers_count": 20},
    ]

    result = calculate_average_stars(repos)

    assert result == 15


def test_calculate_average_stars_empty():
    repos = []

    result = calculate_average_stars(repos)

    assert result == 0.0


def test_get_top_repository():
    repos = [
        {
            "name": "Repo A",
            "stargazers_count": 5,
        },
        {
            "name": "Repo B",
            "stargazers_count": 20,
        },
        {
            "name": "Repo C",
            "stargazers_count": 10,
        },
    ]

    result = get_top_repository(repos)

    assert result is not None
    assert result["name"] == "Repo B"


def test_get_top_repository_empty():
    repos = []

    result = get_top_repository(repos)

    assert result is None


def test_count_languages():
    repos = [
        {"language": "Python"},
        {"language": "Python"},
        {"language": "C"},
        {"language": None},
    ]

    result = count_languages(repos)

    assert result == {
        "Python": 2,
        "C": 1,
    }


def test_get_top_language():
    language_counts = {
        "Python": 5,
        "C": 2,
        "JavaScript": 1,
    }

    result = get_top_language(language_counts)

    assert result == "Python"


def test_get_top_language_empty():
    language_counts = {}

    result = get_top_language(language_counts)

    assert result is None