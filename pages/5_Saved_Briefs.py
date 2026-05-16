import streamlit as st

from src.database.design_repository import (
    get_generated_briefs,
    delete_generated_brief
)
from src.services.export_service import (
    create_word_export,
    create_pdf_export
)
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

            with st.expander(t("show_saved_brief")):
                st.markdown(brief["brief"])

            txt_content = create_export_text(brief)
            md_content = create_markdown_export(brief)
            word_content = create_word_export(brief)
            pdf_content = create_pdf_export(brief)

            col1, col2, col3, col4, col5 = st.columns(5)

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
                st.download_button(
                    label=t("download_word"),
                    data=word_content,
                    file_name=f"leaf_design_brief_{brief['id']}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key=f"download_word_{brief['id']}"
                )

            with col4:
                st.download_button(
                    label=t("download_pdf"),
                    data=pdf_content,
                    file_name=f"leaf_design_brief_{brief['id']}.pdf",
                    mime="application/pdf",
                    key=f"download_pdf_{brief['id']}"
                )

            with col5:
                if st.button(f"{t('delete_brief')} #{brief['id']}", key=f"delete_{brief['id']}"):
                    delete_generated_brief(brief["id"])
                    st.success(t("brief_deleted_success"))
                    st.rerun()