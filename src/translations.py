TRANSLATIONS = {
    "en": {
        "app_title": "🌱 LEAF AI Designer",
        "app_subtitle": "AI-powered clothing inspiration library and fashion design assistant.",
        "language": "Language",

        "home_welcome": "Welcome 👋",
        "home_description": """
LEAF AI Designer is an AI-powered fashion design assistant.

The goal of this project is to build a system that can:

- store clothing inspiration references
- organize designs by metadata
- search and filter design references
- generate new original design briefs
- later generate clothing mockup images
""",
"no_matching_refs_title": "No Matching References Found ⚠️",
"no_matching_refs_body": """
I could not find matching designs in the library.

Try one of these:
- Add more designs to the library.
- Use a broader category filter.
- Set fit and season to All.
- Use a simpler prompt.
""",

"reference_board_title": "🖼️ Reference Inspiration Board",
"save_generated_brief": "💾 Save Generated Brief",
"brief_saved_success": "Generated brief saved successfully ✅",
"saved_briefs_title": "💾 Saved Design Briefs",
"no_saved_briefs": "No saved briefs yet.",
"saved_briefs_count": "saved brief(s)",
"saved_brief": "Saved Brief",
"references": "References",
"show_saved_brief": "Show saved brief",
"delete_brief": "Delete Brief",
"brief_deleted_success": "Brief deleted successfully ✅",

"manage_design": "Manage Design",
"view_only": "View Only",
"edit_design": "Edit Design",
"delete_design": "Delete Design",
"save_changes": "Save Changes",
"design_updated_success": "Design updated successfully ✅",
"delete_warning": "Warning: deleting this design will remove it from the database.",
"delete_image_too": "Also delete image file from local storage",
"type_delete_to_confirm": "Type DELETE to confirm",
"delete_confirm_error": "Please type DELETE to confirm deletion.",
"design_deleted_success": "Design deleted successfully ✅",
"image_delete_warning": "Design was deleted, but the image file could not be removed.",

        "current_features": "Current Features ✅",
        "feature_add_single": "Add a single clothing reference",
        "feature_bulk_import": "Bulk import many designs from CSV",
        "feature_library": "View and search the design library",
        "feature_manual_brief": "Generate a design brief manually",
        "feature_library_brief": "Generate a design brief from library references",
        "workflow": "Project Workflow",

        "add_design_title": "➕ Add New Clothing Reference",
        "product_name": "Product Name",
        "category": "Category",
        "subcategory": "Subcategory",
        "fit": "Fit",
        "style": "Style",
        "primary_color": "Primary Color",
        "secondary_color": "Secondary Color",
        "pattern": "Pattern",
        "graphic_type": "Graphic Type",
        "logo_position": "Logo Position",
        "sleeve_type": "Sleeve Type",
        "neck_type": "Neck Type",
        "season": "Season",
        "fabric_look": "Fabric Look",
        "mood": "Mood",
        "tags": "Tags",
        "upload_design_image": "Upload Design Image",
        "notes": "Notes",
        "save_design": "Save Design",
        "required_fields_error": "Please fill Product Name, Primary Color, and Style.",
        "design_saved_success": "Design reference saved successfully ✅",

        "ph_product_name": "Example: LEAF Shirt Inspiration 001",
        "ph_subcategory": "Example: Oversized T-shirt",
        "ph_style": "Example: Minimal Streetwear",
        "ph_primary_color": "Example: Olive Green",
        "ph_secondary_color": "Example: White",
        "ph_pattern": "Example: Plain / Graphic / Striped",
        "ph_graphic_type": "Example: Small chest graphic",
        "ph_logo_position": "Example: Left chest",
        "ph_sleeve_type": "Example: Short sleeve",
        "ph_neck_type": "Example: Crew neck",
        "ph_fabric": "Example: Cotton / Fleece / Denim",
        "ph_mood": "Example: Clean premium / Sporty / Urban",
        "ph_tags": "Example: eco, urban, modern",
        "ph_notes": "Write anything important about this design...",

        "bulk_import_title": "📦 Bulk Import Designs",
        "bulk_import_description": """
Use this page when you want to import many designs at once.

Put your CSV file here:

`data/bulk_import/designs.csv`

Put your images here:

`data/bulk_import/images/`
""",
        "required_csv_format": "Required CSV Format",
        "start_bulk_import": "Start Bulk Import",
        "skipped_rows": "Skipped",

        "design_library_title": "📚 Design Library",
        "search_designs": "Search designs",
        "search_placeholder": "Search by style, color, tag, mood, category...",
        "all": "All",
        "no_designs_found": "No designs found yet.",
        "found_designs": "Found",
        "designs": "design(s)",
        "no_image_uploaded": "No image uploaded",
        "not_specified": "Not specified",
        "no_tags": "No tags",
        "no_notes": "No notes",
        "created_at": "Created at",

        "ai_brief_title": "🤖 AI Design Brief Generator",
        "ai_brief_description": "This page has two modes: manual design brief and generated brief from your library.",
        "choose_mode": "Choose Mode",
        "generate_from_library": "Generate From Library",
        "manual_design_brief": "Manual Design Brief",
        "generate_from_library_title": "🧠 Generate New Design From Library References",
        "write_prompt": "Write your design prompt",
        "prompt_placeholder": "Example: Create a black oversized t-shirt for LEAF with eco streetwear style and a small chest logo.",
        "search_category": "Search Category",
        "search_fit": "Search Fit",
        "search_season": "Search Season",
        "optional_keyword": "Optional search keyword",
        "keyword_placeholder": "Example: black, streetwear, eco, hoodie, cotton",
        "generate_button": "Generate From Library",
        "write_prompt_error": "Please write a design prompt first.",
        "show_references": "Show references used",
        "manual_brief_title": "✍️ Manual Design Brief",
        "generate_manual_button": "Generate Manual Design Brief",
        "matching_refs_found": "matching reference design(s).",

"download_txt": "⬇️ Download TXT",
"download_md": "⬇️ Download Markdown",
"download_word": "⬇️ Download Word",
"download_pdf": "⬇️ Download PDF",

"generated_designs_title": "🖼️ Generated Designs",
"generated_designs_description": "This page stores generated clothing mockups and design images. Later, AI-generated images will appear here automatically.",
"add_generated_design": "➕ Add Generated Design",
"generated_design_title": "Design Title",
"generated_design_title_placeholder": "Example: Black Oversized LEAF Shirt",
"generated_design_prompt": "Image Generation Prompt",
"generated_design_prompt_placeholder": "Paste or write the prompt used to generate this image...",
"generated_design_notes_placeholder": "Write notes about this generated design...",
"upload_generated_image": "Upload Generated Image",
"save_generated_design": "Save Generated Design",
"generated_design_required_error": "Please fill Design Title and Prompt.",
"generated_design_saved_success": "Generated design saved successfully ✅",
"no_generated_designs": "No generated designs saved yet.",
"generated_designs_count": "generated design(s)",
"show_prompt": "Show Prompt",
"generated_design_deleted_success": "Generated design deleted successfully ✅",

"show_image_prompt": "Show image generation prompt",
"create_generated_design_draft": "Create Design Draft",
"generated_design_draft_created": "Generated design draft created successfully ✅",

"prompt_workspace": "🧠 Prompt Workspace",
"improve_prompt": "Improve Prompt",
"save_prompt_changes": "Save Prompt Changes",
"prompt_improved_success": "Prompt improved successfully ✅",
"prompt_saved_success": "Prompt changes saved successfully ✅",
"download_prompt": "Download Prompt",

"analytics_title": "📊 Dataset Analytics",
"analytics_description": "Understand your clothing reference dataset before using it for AI and machine learning.",
"total_designs": "Total Designs",
"unique_categories": "Unique Categories",
"unique_colors": "Unique Colors",
"unique_styles": "Unique Styles",
"top_categories": "Top Categories",
"top_colors": "Top Colors",
"top_fits": "Top Fits",
"top_seasons": "Top Seasons",
"top_tags": "Top Tags",
"analytics_empty": "No designs found yet. Add or bulk import designs first.",

"ml_search_title": "🧠 ML Search",
"ml_search_description": "Search your clothing references using TF-IDF and cosine similarity.",
"ml_query": "Search prompt",
"ml_query_placeholder": "Example: clean sporty black oversized shirt",
"top_k_results": "Number of results",
"run_ml_search": "Run ML Search",
"ml_search_empty": "No matching results found.",
"ml_search_results": "ML Search Results",
"similarity_score": "Similarity Score",
    },

    "ar": {
        "app_title": "🌱 مصمم LEAF الذكي",
        "app_subtitle": "مكتبة إلهام للملابس ومساعد ذكي لتصميم الأزياء.",
        "language": "اللغة",

        "home_welcome": "مرحباً 👋",
        "home_description": """
مصمم LEAF الذكي هو مساعد لتصميم الأزياء باستخدام الذكاء الاصطناعي.

هدف المشروع هو بناء نظام يستطيع:

- حفظ مراجع وإلهامات تصميم الملابس
- تنظيم التصاميم باستخدام بيانات وصفية
- البحث والتصفية داخل مكتبة التصاميم
- توليد أفكار وتصميمات جديدة بشكل نصي
- لاحقاً توليد صور وموك أب للملابس
""",
"no_matching_refs_title": "لم يتم العثور على مراجع مطابقة ⚠️",
"no_matching_refs_body": """
لم أستطع العثور على تصاميم مطابقة داخل المكتبة.

جرّب واحداً من هذه الحلول:
- أضف تصاميم أكثر إلى المكتبة.
- استخدم فئة بحث أوسع.
- اجعل القَصّة والموسم على الكل.
- استخدم وصفاً أبسط للتصميم.
""",
"reference_board_title": "🖼️ لوحة مراجع الإلهام",

"save_generated_brief": "💾 حفظ فكرة التصميم",
"brief_saved_success": "تم حفظ فكرة التصميم بنجاح ✅",
"saved_briefs_title": "💾 أفكار التصميم المحفوظة",
"no_saved_briefs": "لا توجد أفكار تصميم محفوظة بعد.",
"saved_briefs_count": "فكرة محفوظة",
"saved_brief": "فكرة محفوظة",
"references": "المراجع",
"show_saved_brief": "عرض فكرة التصميم المحفوظة",
"delete_brief": "حذف الفكرة",
"brief_deleted_success": "تم حذف الفكرة بنجاح ✅",

"manage_design": "إدارة التصميم",
"view_only": "عرض فقط",
"edit_design": "تعديل التصميم",
"delete_design": "حذف التصميم",
"save_changes": "حفظ التعديلات",
"design_updated_success": "تم تحديث التصميم بنجاح ✅",
"delete_warning": "تحذير: حذف هذا التصميم سيزيله من قاعدة البيانات.",
"delete_image_too": "حذف صورة التصميم من التخزين المحلي أيضاً",
"type_delete_to_confirm": "اكتب DELETE لتأكيد الحذف",
"delete_confirm_error": "من فضلك اكتب DELETE لتأكيد الحذف.",
"design_deleted_success": "تم حذف التصميم بنجاح ✅",
"image_delete_warning": "تم حذف التصميم، لكن لم يتم حذف ملف الصورة.",


        "current_features": "الميزات الحالية ✅",
        "feature_add_single": "إضافة مرجع تصميم واحد",
        "feature_bulk_import": "استيراد عدد كبير من التصاميم من ملف CSV",
        "feature_library": "عرض مكتبة التصاميم والبحث داخلها",
        "feature_manual_brief": "توليد فكرة تصميم بشكل يدوي",
        "feature_library_brief": "توليد فكرة تصميم من مراجع المكتبة",
        "workflow": "مسار عمل المشروع",

        "add_design_title": "➕ إضافة مرجع تصميم جديد",
        "product_name": "اسم المنتج",
        "category": "الفئة",
        "subcategory": "الفئة الفرعية",
        "fit": "القَصّة / المقاس",
        "style": "الستايل",
        "primary_color": "اللون الأساسي",
        "secondary_color": "اللون الثانوي",
        "pattern": "النمط",
        "graphic_type": "نوع الرسمة",
        "logo_position": "مكان الشعار",
        "sleeve_type": "نوع الكم",
        "neck_type": "نوع الرقبة",
        "season": "الموسم",
        "fabric_look": "شكل القماش",
        "mood": "الإحساس العام",
        "tags": "الكلمات المفتاحية",
        "upload_design_image": "رفع صورة التصميم",
        "notes": "ملاحظات",
        "save_design": "حفظ التصميم",
        "required_fields_error": "من فضلك املأ اسم المنتج، اللون الأساسي، والستايل.",
        "design_saved_success": "تم حفظ مرجع التصميم بنجاح ✅",

        "ph_product_name": "مثال: مرجع تيشيرت LEAF رقم 001",
        "ph_subcategory": "مثال: تيشيرت واسع",
        "ph_style": "مثال: ستريت وير بسيط",
        "ph_primary_color": "مثال: أخضر زيتوني",
        "ph_secondary_color": "مثال: أبيض",
        "ph_pattern": "مثال: سادة / جرافيك / مخطط",
        "ph_graphic_type": "مثال: رسمة صغيرة على الصدر",
        "ph_logo_position": "مثال: يسار الصدر",
        "ph_sleeve_type": "مثال: كم قصير",
        "ph_neck_type": "مثال: رقبة دائرية",
        "ph_fabric": "مثال: قطن / فليس / دينم",
        "ph_mood": "مثال: نظيف وفخم / رياضي / حضري",
        "ph_tags": "مثال: بيئي، حضري، حديث",
        "ph_notes": "اكتب أي ملاحظات مهمة عن التصميم...",

        "bulk_import_title": "📦 استيراد التصاميم دفعة واحدة",
        "bulk_import_description": """
استخدم هذه الصفحة عندما تريد استيراد عدد كبير من التصاميم مرة واحدة.

ضع ملف CSV هنا:

`data/bulk_import/designs.csv`

وضع الصور هنا:

`data/bulk_import/images/`
""",
        "required_csv_format": "صيغة ملف CSV المطلوبة",
        "start_bulk_import": "بدء الاستيراد",
        "skipped_rows": "تم تخطي",

        "design_library_title": "📚 مكتبة التصاميم",
        "search_designs": "البحث في التصاميم",
        "search_placeholder": "ابحث بالستايل، اللون، الكلمات المفتاحية، الإحساس، الفئة...",
        "all": "الكل",
        "no_designs_found": "لا توجد تصاميم بعد.",
        "found_designs": "تم العثور على",
        "designs": "تصميم",
        "no_image_uploaded": "لا توجد صورة مرفوعة",
        "not_specified": "غير محدد",
        "no_tags": "لا توجد كلمات مفتاحية",
        "no_notes": "لا توجد ملاحظات",
        "created_at": "تاريخ الإضافة",

        "ai_brief_title": "🤖 مولد أفكار التصميم الذكي",
        "ai_brief_description": "هذه الصفحة تحتوي على وضعين: توليد يدوي، وتوليد اعتماداً على مكتبة التصاميم.",
        "choose_mode": "اختر الوضع",
        "generate_from_library": "توليد من المكتبة",
        "manual_design_brief": "توليد يدوي",
        "generate_from_library_title": "🧠 توليد تصميم جديد من مراجع المكتبة",
        "write_prompt": "اكتب وصف التصميم",
        "prompt_placeholder": "مثال: صمم تيشيرت أسود واسع لبراند LEAF بستايل إيكو ستريت وير وشعار صغير على الصدر.",
        "search_category": "فئة البحث",
        "search_fit": "القَصّة",
        "search_season": "الموسم",
        "optional_keyword": "كلمة بحث اختيارية",
        "keyword_placeholder": "مثال: أسود، ستريت وير، إيكو، هودي، قطن",
        "generate_button": "توليد من المكتبة",
        "write_prompt_error": "من فضلك اكتب وصف التصميم أولاً.",
        "show_references": "عرض المراجع المستخدمة",
        "manual_brief_title": "✍️ توليد يدوي لفكرة التصميم",
        "generate_manual_button": "توليد الفكرة اليدوية",
        "matching_refs_found": "مرجع تصميم مطابق.",

"download_txt": "⬇️ تحميل TXT",
"download_md": "⬇️ تحميل Markdown",
"download_word": "⬇️ تحميل Word",
"download_pdf": "⬇️ تحميل PDF",

"generated_designs_title": "🖼️ التصاميم المولدة",
"generated_designs_description": "هذه الصفحة تحفظ صور التصاميم والموك أب. لاحقاً ستظهر هنا الصور التي يولدها الذكاء الاصطناعي تلقائياً.",
"add_generated_design": "➕ إضافة تصميم مولد",
"generated_design_title": "عنوان التصميم",
"generated_design_title_placeholder": "مثال: تيشيرت LEAF أسود واسع",
"generated_design_prompt": "وصف توليد الصورة",
"generated_design_prompt_placeholder": "اكتب أو الصق الوصف المستخدم لتوليد هذه الصورة...",
"generated_design_notes_placeholder": "اكتب ملاحظات عن هذا التصميم المولد...",
"upload_generated_image": "رفع صورة التصميم المولد",
"save_generated_design": "حفظ التصميم المولد",
"generated_design_required_error": "من فضلك املأ عنوان التصميم ووصف التوليد.",
"generated_design_saved_success": "تم حفظ التصميم المولد بنجاح ✅",
"no_generated_designs": "لا توجد تصاميم مولدة محفوظة بعد.",
"generated_designs_count": "تصميم مولد",
"show_prompt": "عرض الوصف",
"generated_design_deleted_success": "تم حذف التصميم المولد بنجاح ✅",

"show_image_prompt": "عرض وصف توليد الصورة",
"create_generated_design_draft": "إنشاء مسودة تصميم",
"generated_design_draft_created": "تم إنشاء مسودة التصميم بنجاح ✅",

"prompt_workspace": "🧠 مساحة تعديل الوصف",
"improve_prompt": "تحسين الوصف",
"save_prompt_changes": "حفظ تعديلات الوصف",
"prompt_improved_success": "تم تحسين الوصف بنجاح ✅",
"prompt_saved_success": "تم حفظ تعديلات الوصف بنجاح ✅",
"download_prompt": "تحميل الوصف",

"analytics_title": "📊 تحليل بيانات التصاميم",
"analytics_description": "افهم بيانات مراجع الملابس قبل استخدامها في الذكاء الاصطناعي وتعلم الآلة.",
"total_designs": "إجمالي التصاميم",
"unique_categories": "عدد الفئات المختلفة",
"unique_colors": "عدد الألوان المختلفة",
"unique_styles": "عدد الستايلات المختلفة",
"top_categories": "أكثر الفئات تكراراً",
"top_colors": "أكثر الألوان تكراراً",
"top_fits": "أكثر القصّات تكراراً",
"top_seasons": "أكثر المواسم تكراراً",
"top_tags": "أكثر الكلمات المفتاحية تكراراً",
"analytics_empty": "لا توجد تصاميم بعد. أضف تصاميم أو استوردها أولاً.",

"ml_search_title": "🧠 بحث ذكي بتعلم الآلة",
"ml_search_description": "ابحث داخل مراجع الملابس باستخدام TF-IDF وقياس التشابه.",
"ml_query": "وصف البحث",
"ml_query_placeholder": "مثال: تيشيرت أسود واسع ستايل بسيط",
"top_k_results": "عدد النتائج",
"run_ml_search": "تشغيل البحث الذكي",
"ml_search_empty": "لم يتم العثور على نتائج مطابقة.",
"ml_search_results": "نتائج البحث الذكي",
"similarity_score": "درجة التشابه",
    }
}


def get_text(key):
    """
    Return translated text by key based on selected language.
    """
    import streamlit as st

    language = st.session_state.get("language", "en")
    return TRANSLATIONS.get(language, TRANSLATIONS["en"]).get(key, key)