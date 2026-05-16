from pathlib import Path
import os
from src.services.prompt_service import improve_prompt, prompt_to_txt
import streamlit as st

from src.database.generated_design_repository import (
    insert_generated_design,
    get_generated_designs,
    delete_generated_design,
    update_generated_design_prompt
)
from src.services.prompt_service import improve_prompt, prompt_to_txt
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
            placeholder=t("generated_design_prompt_placeholder"),
            height=160
        )

        notes = st.text_area(
            t("notes"),
            placeholder=t("generated_design_notes_placeholder"),
            height=120
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

    for design in generated_designs:
        with st.container():
            st.markdown("---")

            col_img, col_workspace = st.columns([1, 2])

            with col_img:
                if design["image_path"] and Path(design["image_path"]).exists():
                    st.image(design["image_path"], width="stretch")
                else:
                    st.info(t("no_image_uploaded"))

                st.subheader(design["title"])
                st.caption(f"{t('created_at')}: {design['created_at']}")

            with col_workspace:
                st.subheader(t("prompt_workspace"))

                edited_prompt = st.text_area(
                    t("generated_design_prompt"),
                    value=design["prompt"] or "",
                    height=180,
                    key=f"prompt_editor_{design['id']}"
                )

                edited_notes = st.text_area(
                    t("notes"),
                    value=design["notes"] or "",
                    height=120,
                    key=f"notes_editor_{design['id']}"
                )

                col1, col2, col3 = st.columns(3)

                with col1:
                    if st.button(t("improve_prompt"), key=f"improve_prompt_{design['id']}"):
                        improved_prompt = improve_prompt(edited_prompt)

                        update_generated_design_prompt(
                            design_id=design["id"],
                            prompt=improved_prompt,
                            notes=edited_notes
                        )

                        st.success(t("prompt_improved_success"))
                        st.rerun()

                with col2:
                    if st.button(t("save_prompt_changes"), key=f"save_prompt_{design['id']}"):
                        update_generated_design_prompt(
                            design_id=design["id"],
                            prompt=edited_prompt,
                            notes=edited_notes
                        )

                        st.success(t("prompt_saved_success"))
                        st.rerun()

                with col3:
                    txt_content = prompt_to_txt(
                        title=design["title"],
                        prompt=edited_prompt,
                        notes=edited_notes
                    )

                    st.download_button(
                        label=t("download_prompt"),
                        data=txt_content,
                        file_name=f"leaf_image_prompt_{design['id']}.txt",
                        mime="text/plain",
                        key=f"download_prompt_{design['id']}"
                    )

                with st.expander(t("delete_design")):
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