import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.services.search_service import normalize_search_words


def design_row_to_text(design):
    """
    Convert a design database row into one searchable text document.
    """
    fields = [
        design["product_name"],
        design["category"],
        design["subcategory"],
        design["fit"],
        design["style"],
        design["primary_color"],
        design["secondary_color"],
        design["pattern"],
        design["graphic_type"],
        design["logo_position"],
        design["sleeve_type"],
        design["neck_type"],
        design["season"],
        design["fabric_look"],
        design["mood"],
        design["tags"],
        design["notes"],
    ]

    clean_fields = []

    for field in fields:
        if field is not None and str(field).strip():
            clean_fields.append(str(field).strip())

    return " ".join(clean_fields)


def normalize_query_text(query):
    """
    Convert Arabic/English query into normalized searchable text.
    """
    words = normalize_search_words(query)

    if not words:
        return query

    return " ".join(words)


def search_designs_with_tfidf(query, designs, top_k=10):
    """
    Search designs using TF-IDF vectors and cosine similarity.

    Returns a list of dictionaries:
    {
        "design": sqlite row,
        "score": float
    }
    """
    if not query or len(designs) == 0:
        return []

    documents = [design_row_to_text(design) for design in designs]
    normalized_query = normalize_query_text(query)

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english",
        ngram_range=(1, 2)
    )

    document_vectors = vectorizer.fit_transform(documents)
    query_vector = vectorizer.transform([normalized_query])

    similarities = cosine_similarity(query_vector, document_vectors).flatten()

    ranked_indices = similarities.argsort()[::-1]

    results = []

    for index in ranked_indices[:top_k]:
        score = float(similarities[index])

        if score <= 0:
            continue

        results.append({
            "design": designs[index],
            "score": score
        })

    return results


def results_to_dataframe(results):
    """
    Convert ML search results into a pandas DataFrame for display.
    """
    rows = []

    for result in results:
        design = result["design"]

        rows.append({
            "score": round(result["score"], 4),
            "product_name": design["product_name"],
            "category": design["category"],
            "fit": design["fit"],
            "style": design["style"],
            "primary_color": design["primary_color"],
            "tags": design["tags"],
        })

    return pd.DataFrame(rows)