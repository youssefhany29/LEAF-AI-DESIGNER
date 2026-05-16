from pathlib import Path
import os

import streamlit as st

from src.database.design_repository import (
    insert_generated_design,
    get_generated_designs,
    delete_generated_design
)
from src.services.image_service import save_generated_image
from src.ui.shared import setup_page, show_app_header
from src.translations import get_text


setup_page("Generated Designs", "🖼️")
show_app_header()

t = get_text

st.header(t("generated_designs_title"))

st.write(t("generated_designs_description"))


with st.expander(t("add_generated_design")):
    with st.form("add_generated_design_form"):
        title = st.text_input(
            t("generated_design_title"),
            placeholder=t("generated_design_title_placeholder")
        )

        prompt = st.text_area(
            t("generated_design_prompt"),
            placeholder=t("generated_design_prompt_placeholder")
        )

        notes = st.text_area(
            t("notes"),
            placeholder=t("generated_design_notes_placeholder")
        )

        uploaded_image = st.file_uploader(
            t("upload_generated_image"),
            type=["png", "jpg", "jpeg", "webp"]
        )

        submitted = st.form_submit_button(t("save_generated_design"))

        if submitted:
            if not title or not prompt:
                st.error(t("generated_design_required_error"))
            else:
                image_path = save_generated_image(uploaded_image)

                insert_generated_design(
                    title=title,
                    prompt=prompt,
                    image_path=image_path,
                    notes=notes
                )

                st.success(t("generated_design_saved_success"))
                st.rerun()


generated_designs = get_generated_designs()

if len(generated_designs) == 0:
    st.info(t("no_generated_designs"))
else:
    st.write(f"{t('found_designs')} **{len(generated_designs)}** {t('generated_designs_count')}.")

    columns_per_row = 3

    for start_index in range(0, len(generated_designs), columns_per_row):
        row_items = generated_designs[start_index:start_index + columns_per_row]
        columns = st.columns(columns_per_row)

        for column, design in zip(columns, row_items):
            with column:
                with st.container():
                    if design["image_path"] and Path(design["image_path"]).exists():
                        st.image(design["image_path"], width="stretch")
                    else:
                        st.info(t("no_image_uploaded"))

                    st.subheader(design["title"])
                    st.caption(f"{t('created_at')}: {design['created_at']}")

                    with st.expander(t("show_prompt")):
                        st.write(design["prompt"])

                    if design["notes"]:
                        with st.expander(t("notes")):
                            st.write(design["notes"])

                    delete_image_too = st.checkbox(
                        t("delete_image_too"),
                        key=f"delete_generated_image_{design['id']}"
                    )

                    confirm_delete = st.text_input(
                        t("type_delete_to_confirm"),
                        key=f"confirm_generated_delete_{design['id']}"
                    )

                    if st.button(t("delete_design"), key=f"delete_generated_design_{design['id']}"):
                        if confirm_delete.strip().upper() != "DELETE":
                            st.error(t("delete_confirm_error"))
                        else:
                            image_path = design["image_path"]

                            delete_generated_design(design["id"])

                            if delete_image_too and image_path and Path(image_path).exists():
                                try:
                                    os.remove(image_path)
                                except OSError:
                                    st.warning(t("image_delete_warning"))

                            st.success(t("generated_design_deleted_success"))
                            st.rerun()