import pandas as pd


def rows_to_dataframe(rows):
    """
    Convert SQLite rows into a pandas DataFrame.
    """
    return pd.DataFrame([dict(row) for row in rows])


def count_unique_values(dataframe, column_name):
    """
    Count unique non-empty values in a column.
    """
    if dataframe.empty or column_name not in dataframe.columns:
        return 0

    values = dataframe[column_name].dropna()
    values = values[values.astype(str).str.strip() != ""]

    return values.nunique()


def get_top_values(dataframe, column_name, limit=10):
    """
    Return most common values for a selected column.
    """
    if dataframe.empty or column_name not in dataframe.columns:
        return pd.DataFrame(columns=[column_name, "count"])

    values = dataframe[column_name].fillna("Not specified")
    values = values.astype(str).str.strip()
    values = values.replace("", "Not specified")

    counts = values.value_counts().head(limit).reset_index()
    counts.columns = [column_name, "count"]

    return counts


def get_top_tags(dataframe, limit=15):
    """
    Count the most common tags from the tags column.
    """
    if dataframe.empty or "tags" not in dataframe.columns:
        return pd.DataFrame(columns=["tag", "count"])

    all_tags = []

    for tags in dataframe["tags"].dropna():
        split_tags = str(tags).split(",")

        for tag in split_tags:
            clean_tag = tag.strip()

            if clean_tag:
                all_tags.append(clean_tag)

    if not all_tags:
        return pd.DataFrame(columns=["tag", "count"])

    tag_series = pd.Series(all_tags)
    counts = tag_series.value_counts().head(limit).reset_index()
    counts.columns = ["tag", "count"]

    return counts