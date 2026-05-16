import streamlit as st

from src.database.design_repository import (
    get_generated_briefs,
    delete_generated_brief
)
from src.ui.shared import setup_page, show_app_header
from src.translations import get_text


setup_page("Saved Briefs", "💾")
show_app_header()

t = get_text

st.header(t("saved_briefs_title"))

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

            if st.button(f"{t('delete_brief')} #{brief['id']}", key=f"delete_{brief['id']}"):
                delete_generated_brief(brief["id"])
                st.success(t("brief_deleted_success"))
                st.rerun()