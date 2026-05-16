import streamlit as st

from src.database.brief_repository import (
    get_generated_briefs,
    delete_generated_brief
)
from src.database.generated_design_repository import insert_generated_design
from src.ui.shared import setup_page, show_app_header
from src.translations import get_text


setup_page("Saved Briefs", "💾")
show_app_header()

t = get_text

st.header(t("saved_briefs_title"))


def create_export_text(brief):
    """
    Create plain text export content for a saved brief.
    """
    content = f"""
LEAF AI Designer - Saved Design Brief

ID: {brief['id']}
Created At: {brief['created_at']}
Language: {brief['language']}
Prompt: {brief['prompt']}
References: {brief['reference_names'] or t('not_specified')}

--------------------------------------------------

{brief['brief']}
"""
    return content.strip()


def create_markdown_export(brief):
    """
    Create markdown export content for a saved brief.
    """
    content = f"""# LEAF AI Designer - Saved Design Brief

## Metadata

- **ID:** {brief['id']}
- **Created At:** {brief['created_at']}
- **Language:** {brief['language']}
- **Prompt:** {brief['prompt']}
- **References:** {brief['reference_names'] or t('not_specified')}

---

{brief['brief']}
"""
    return content.strip()


def extract_image_prompt(brief_text):
    """
    Extract the image generation prompt from a saved brief.

    Works with English and Arabic generated briefs.
    If no prompt section is found, it returns an empty string.
    """
    if not brief_text:
        return ""

    english_marker = "## 6. Image Generation Prompt For Later"
    arabic_marker = "## 6. وصف توليد الصورة لاحقاً"

    markers = [english_marker, arabic_marker]

    for marker in markers:
        if marker in brief_text:
            after_marker = brief_text.split(marker, 1)[1].strip()

            stop_markers = [
                "## 7.",
                "###",
                "---"
            ]

            extracted_text = after_marker

            for stop_marker in stop_markers:
                if stop_marker in extracted_text:
                    extracted_text = extracted_text.split(stop_marker, 1)[0].strip()

            return extracted_text.strip()

    return ""


def create_design_title_from_prompt(prompt):
    """
    Create a simple generated design title from the original prompt.
    """
    if not prompt:
        return "Generated LEAF Design"

    clean_prompt = prompt.strip()

    if len(clean_prompt) > 50:
        clean_prompt = clean_prompt[:50].strip() + "..."

    return clean_prompt


def create_generated_design_draft(brief):
    """
    Create a generated design draft from a saved brief.
    """
    image_prompt = extract_image_prompt(brief["brief"])

    if not image_prompt:
        image_prompt = brief["prompt"]

    title = create_design_title_from_prompt(brief["prompt"])

    notes = f"""
Generated from saved brief #{brief['id']}

Original prompt:
{brief['prompt']}

References:
{brief['reference_names'] or t('not_specified')}

Full saved brief:
{brief['brief']}
""".strip()

    insert_generated_design(
        title=title,
        prompt=image_prompt,
        image_path=None,
        notes=notes
    )


briefs = get_generated_briefs()

if len(briefs) == 0:
    st.info(t("no_saved_briefs"))
else:
    st.write(f"{t('found_designs')} **{len(briefs)}** {t('saved_briefs_count')}.")

    for brief in briefs:
        with st.container():
            st.markdown("---")

            st.subheader(f"{t('saved_brief')} #{brief['id']}")

            st.write(f"**{t('write_prompt')}:** {brief['prompt']}")
            st.write(f"**{t('language')}:** {brief['language']}")
            st.write(f"**{t('references')}:** {brief['reference_names'] or t('not_specified')}")
            st.caption(f"{t('created_at')}: {brief['created_at']}")

            image_prompt = extract_image_prompt(brief["brief"])

            if image_prompt:
                with st.expander(t("show_image_prompt")):
                    st.code(image_prompt, language="text")

            with st.expander(t("show_saved_brief")):
                st.markdown(brief["brief"])

            txt_content = create_export_text(brief)
            md_content = create_markdown_export(brief)

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.download_button(
                    label=t("download_txt"),
                    data=txt_content,
                    file_name=f"leaf_design_brief_{brief['id']}.txt",
                    mime="text/plain",
                    key=f"download_txt_{brief['id']}"
                )

            with col2:
                st.download_button(
                    label=t("download_md"),
                    data=md_content,
                    file_name=f"leaf_design_brief_{brief['id']}.md",
                    mime="text/markdown",
                    key=f"download_md_{brief['id']}"
                )

            with col3:
                if st.button(t("create_generated_design_draft"), key=f"draft_{brief['id']}"):
                    create_generated_design_draft(brief)
                    st.success(t("generated_design_draft_created"))

            with col4:
                if st.button(f"{t('delete_brief')} #{brief['id']}", key=f"delete_{brief['id']}"):
                    delete_generated_brief(brief["id"])
                    st.success(t("brief_deleted_success"))
                    st.rerun()