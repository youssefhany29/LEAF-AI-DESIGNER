from src.database.design_repository import get_all_designs, search_designs
from src.services.clip_search_service import search_images_with_clip
from src.services.ml_search_service import search_designs_with_tfidf


SEARCH_METHOD_KEYWORD = "keyword"
SEARCH_METHOD_ML = "ml"
SEARCH_METHOD_CLIP = "clip"


def filter_designs(designs, category_filter="All", fit_filter="All", season_filter="All"):
    """
    Filter design rows by selected UI filters.
    """
    filtered_designs = []

    for design in designs:
        if category_filter != "All" and design["category"] != category_filter:
            continue

        if fit_filter != "All" and design["fit"] != fit_filter:
            continue

        if season_filter != "All" and design["season"] != season_filter:
            continue

        filtered_designs.append(design)

    return filtered_designs


def filter_scored_results(results, category_filter="All", fit_filter="All", season_filter="All"):
    """
    Filter scored search results while keeping their scores.
    """
    filtered_results = []

    for result in results:
        design = result["design"]

        if category_filter != "All" and design["category"] != category_filter:
            continue

        if fit_filter != "All" and design["fit"] != fit_filter:
            continue

        if season_filter != "All" and design["season"] != season_filter:
            continue

        filtered_results.append(result)

    return filtered_results


def get_reference_names(designs, limit=5):
    """
    Return comma-separated reference names.
    """
    reference_names = []

    for design in designs[:limit]:
        reference_names.append(design["product_name"])

    return ", ".join(reference_names)


def create_plain_results(designs):
    """
    Convert plain design rows into scored result format.
    """
    results = []

    for design in designs:
        results.append({
            "design": design,
            "score": None
        })

    return results


def extract_designs_from_results(results):
    """
    Extract only design rows from scored results.
    """
    designs = []

    for result in results:
        designs.append(result["design"])

    return designs


def find_reference_results(
    user_prompt,
    keyword,
    category_filter,
    fit_filter,
    season_filter,
    search_method,
    top_k=10
):
    """
    Find reference designs using keyword, TF-IDF ML, or CLIP image search.

    Returns:
        list[dict]
        [
            {"design": sqlite_row, "score": float_or_none}
        ]
    """
    search_keyword = keyword.strip()

    if not search_keyword:
        search_keyword = user_prompt.strip()

    if search_method == SEARCH_METHOD_KEYWORD:
        designs = search_designs(
            keyword=search_keyword,
            category=category_filter,
            fit=fit_filter,
            season=season_filter
        )

        return create_plain_results(designs)

    all_designs = get_all_designs()

    if search_method == SEARCH_METHOD_ML:
        ml_results = search_designs_with_tfidf(
            query=search_keyword,
            designs=all_designs,
            top_k=top_k
        )

        return filter_scored_results(
            results=ml_results,
            category_filter=category_filter,
            fit_filter=fit_filter,
            season_filter=season_filter
        )

    if search_method == SEARCH_METHOD_CLIP:
        clip_results = search_images_with_clip(
            query=search_keyword,
            designs=all_designs,
            top_k=top_k
        )

        return filter_scored_results(
            results=clip_results,
            category_filter=category_filter,
            fit_filter=fit_filter,
            season_filter=season_filter
        )

    return []