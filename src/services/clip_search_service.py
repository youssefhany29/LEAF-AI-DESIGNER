from pathlib import Path

import pandas as pd
import streamlit as st
from PIL import Image
from sentence_transformers import SentenceTransformer, util

from src.services.search_service import normalize_search_words


MODEL_NAME = "clip-ViT-B-32"


@st.cache_resource
def load_clip_model():
    """
    Load CLIP model once and reuse it across Streamlit reruns.
    """
    return SentenceTransformer(MODEL_NAME)


def normalize_clip_query(query):
    """
    Convert Arabic/English query into a cleaner English search query when possible.
    """
    words = normalize_search_words(query)

    if not words:
        return query

    return " ".join(words)


def get_valid_image_designs(designs):
    """
    Return only designs that have existing image paths.
    """
    valid_designs = []

    for design in designs:
        image_path = design["image_path"]

        if image_path and Path(image_path).exists():
            valid_designs.append(design)

    return valid_designs


def build_image_cache_key(designs):
    """
    Build a stable cache key based on image paths and modification times.

    If an image changes, the cache key changes too.
    """
    key_parts = []

    for design in designs:
        image_path = design["image_path"]

        if image_path and Path(image_path).exists():
            path = Path(image_path)
            modified_time = path.stat().st_mtime
            key_parts.append(f"{design['id']}|{path}|{modified_time}")

    return "||".join(key_parts)


@st.cache_data(show_spinner=False)
def encode_image_paths_cached(image_paths, cache_key):
    """
    Encode images using CLIP and cache the embeddings.

    cache_key is only used to invalidate cache when image files change.
    """
    model = load_clip_model()

    images = []

    for image_path in image_paths:
        image = Image.open(image_path).convert("RGB")
        images.append(image)

    image_embeddings = model.encode(
        images,
        convert_to_tensor=True,
        show_progress_bar=False
    )

    return image_embeddings


def search_images_with_clip(query, designs, top_k=10):
    """
    Search image references using CLIP text-to-image similarity.
    """
    valid_designs = get_valid_image_designs(designs)

    if not query or len(valid_designs) == 0:
        return []

    model = load_clip_model()

    normalized_query = normalize_clip_query(query)

    text_embedding = model.encode(
        [normalized_query],
        convert_to_tensor=True,
        show_progress_bar=False
    )

    image_paths = [design["image_path"] for design in valid_designs]
    cache_key = build_image_cache_key(valid_designs)

    image_embeddings = encode_image_paths_cached(
        image_paths=image_paths,
        cache_key=cache_key
    )

    scores = util.cos_sim(text_embedding, image_embeddings)[0]
    top_results = scores.topk(k=min(top_k, len(valid_designs)))

    results = []

    for score, index in zip(top_results.values, top_results.indices):
        results.append({
            "design": valid_designs[int(index)],
            "score": float(score)
        })

    return results


def clear_clip_cache():
    """
    Clear cached CLIP model and image embeddings.
    """
    load_clip_model.clear()
    encode_image_paths_cached.clear()


def clip_results_to_dataframe(results):
    """
    Convert CLIP results into a dataframe.
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