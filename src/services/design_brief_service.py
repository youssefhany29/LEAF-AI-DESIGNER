from collections import Counter

import streamlit as st

from src.translations import get_text


def current_language():
    """
    Return current selected language.
    """
    return st.session_state.get("language", "en")


def is_arabic():
    """
    Return True if current language is Arabic.
    """
    return current_language() == "ar"


def get_most_common_value(designs, column_name, default_value="Not enough data"):
    """
    Get the most common value from a database column.
    """
    values = []

    for design in designs:
        value = design[column_name]

        if value is not None and str(value).strip() != "":
            values.append(str(value).strip())

    if not values:
        return default_value

    counter = Counter(values)
    return counter.most_common(1)[0][0]


def get_all_tags(designs):
    """
    Collect all tags from matching designs.
    """
    all_tags = []

    for design in designs:
        tags = design["tags"]

        if tags is not None and str(tags).strip() != "":
            split_tags = str(tags).split(",")

            for tag in split_tags:
                clean_tag = tag.strip()

                if clean_tag:
                    all_tags.append(clean_tag)

    if not all_tags:
        return "eco, minimal, modern"

    counter = Counter(all_tags)
    top_tags = [tag for tag, count in counter.most_common(6)]

    return ", ".join(top_tags)


def generate_design_brief(
    category,
    subcategory,
    fit,
    style,
    primary_color,
    secondary_color,
    pattern,
    graphic_type,
    logo_position,
    sleeve_type,
    neck_type,
    season,
    fabric_look,
    mood,
    tags,
    notes
):
    """
    Generate a manual rule-based design brief in English or Arabic.
    """
    if is_arabic():
        return generate_manual_design_brief_ar(
            category=category,
            subcategory=subcategory,
            fit=fit,
            style=style,
            primary_color=primary_color,
            secondary_color=secondary_color,
            pattern=pattern,
            graphic_type=graphic_type,
            logo_position=logo_position,
            sleeve_type=sleeve_type,
            neck_type=neck_type,
            season=season,
            fabric_look=fabric_look,
            mood=mood,
            tags=tags,
            notes=notes
        )

    return generate_manual_design_brief_en(
        category=category,
        subcategory=subcategory,
        fit=fit,
        style=style,
        primary_color=primary_color,
        secondary_color=secondary_color,
        pattern=pattern,
        graphic_type=graphic_type,
        logo_position=logo_position,
        sleeve_type=sleeve_type,
        neck_type=neck_type,
        season=season,
        fabric_look=fabric_look,
        mood=mood,
        tags=tags,
        notes=notes
    )


def generate_manual_design_brief_en(
    category,
    subcategory,
    fit,
    style,
    primary_color,
    secondary_color,
    pattern,
    graphic_type,
    logo_position,
    sleeve_type,
    neck_type,
    season,
    fabric_look,
    mood,
    tags,
    notes
):
    """
    Generate a manual design brief in English.
    """
    secondary_color_text = secondary_color if secondary_color else "a natural neutral accent color"
    fabric_text = fabric_look if fabric_look else "organic cotton or recycled cotton blend"
    logo_text = logo_position if logo_position else "small LEAF logo on the left chest"
    graphic_text = graphic_type if graphic_type else "minimal nature-inspired graphic"

    brief = f"""
## AI Design Brief 🌱👕

### Product
- **Category:** {category}
- **Subcategory:** {subcategory if subcategory else "Not specified"}
- **Fit:** {fit if fit else "Relaxed / comfortable"}

### Visual Direction
- **Style:** {style}
- **Mood:** {mood if mood else "Clean, natural, and premium"}
- **Pattern:** {pattern if pattern else "Simple / not overcrowded"}
- **Tags:** {tags if tags else "eco, minimal, modern"}

### Color Palette
- **Primary Color:** {primary_color}
- **Secondary Color:** {secondary_color_text}

### Clothing Details
- **Sleeve Type:** {sleeve_type if sleeve_type else "Depends on product type"}
- **Neck Type:** {neck_type if neck_type else "Depends on product type"}
- **Season:** {season if season else "All season"}
- **Fabric Look:** {fabric_text}

### Logo and Graphic Placement
- **Logo Position:** {logo_text}
- **Graphic Type:** {graphic_text}

### Original Design Concept
Create a new original {fit.lower() if fit else "relaxed"} {category.lower()} for LEAF using {primary_color.lower()} as the main color and {secondary_color_text.lower()} as the supporting color.

The design should feel {mood.lower() if mood else "clean, premium, and eco-friendly"} with a {style.lower()} direction.
It should use {graphic_text.lower()} while keeping the layout balanced and not copied from any existing brand.

### Production Notes
- Keep the LEAF logo clean and readable.
- Avoid direct copying of famous brand logos or graphics.
- Keep enough empty space around the main design.
- Make the design suitable for a real clothing mockup.
- Use the dataset references only as inspiration, not as direct copies.

### Extra Notes
{notes if notes else "No extra notes added."}
"""
    return brief


def generate_manual_design_brief_ar(
    category,
    subcategory,
    fit,
    style,
    primary_color,
    secondary_color,
    pattern,
    graphic_type,
    logo_position,
    sleeve_type,
    neck_type,
    season,
    fabric_look,
    mood,
    tags,
    notes
):
    """
    Generate a manual design brief in Arabic.
    """
    secondary_color_text = secondary_color if secondary_color else "لون محايد طبيعي مناسب للبراند"
    fabric_text = fabric_look if fabric_look else "قطن عضوي أو خليط قطن معاد تدويره"
    logo_text = logo_position if logo_position else "شعار LEAF صغير على يسار الصدر"
    graphic_text = graphic_type if graphic_type else "رسمة بسيطة مستوحاة من الطبيعة"

    brief = f"""
## فكرة التصميم الذكية 🌱👕

### المنتج
- **الفئة:** {category}
- **الفئة الفرعية:** {subcategory if subcategory else "غير محدد"}
- **القَصّة / المقاس:** {fit if fit else "مريح ومناسب للاستخدام اليومي"}

### الاتجاه البصري
- **الستايل:** {style}
- **الإحساس العام:** {mood if mood else "نظيف، طبيعي، وفخم"}
- **النمط:** {pattern if pattern else "بسيط وغير مزدحم"}
- **الكلمات المفتاحية:** {tags if tags else "بيئي، بسيط، حديث"}

### لوحة الألوان
- **اللون الأساسي:** {primary_color}
- **اللون الثانوي:** {secondary_color_text}

### تفاصيل القطعة
- **نوع الكم:** {sleeve_type if sleeve_type else "حسب نوع المنتج"}
- **نوع الرقبة:** {neck_type if neck_type else "حسب نوع المنتج"}
- **الموسم:** {season if season else "مناسب لكل المواسم"}
- **شكل القماش:** {fabric_text}

### مكان الشعار والرسمة
- **مكان الشعار:** {logo_text}
- **نوع الرسمة:** {graphic_text}

### فكرة التصميم الأصلية
صمّم قطعة جديدة وأصلية من نوع **{category}** لبراند LEAF باستخدام **{primary_color}** كلون أساسي و **{secondary_color_text}** كلون مساعد.

يجب أن يكون التصميم بإحساس **{mood if mood else "نظيف وفخم وصديق للبيئة"}** وباتجاه بصري قريب من **{style}**.
استخدم **{graphic_text}** مع الحفاظ على توازن التصميم وعدم تقليد أي براند أو تصميم موجود.

### ملاحظات إنتاجية
- اجعل شعار LEAF واضحاً ونظيفاً.
- تجنب نسخ شعارات أو رسومات أو تخطيطات من براندات أخرى.
- اترك مساحة فارغة كافية حتى يبدو التصميم فخماً.
- اجعل التصميم مناسباً للاستخدام لاحقاً في موك أب حقيقي.
- استخدم مراجع الداتا كمصدر إلهام فقط، وليس للنسخ المباشر.

### ملاحظات إضافية
{notes if notes else "لا توجد ملاحظات إضافية."}
"""
    return brief


def generate_design_brief_from_library(user_prompt, matching_designs):
    """
    Generate a new original design brief by reading metadata from matching library designs.
    Output language follows selected UI language.
    """
    if len(matching_designs) == 0:
        return f"""
## {get_text("no_matching_refs_title")}

{get_text("no_matching_refs_body")}
"""

    if is_arabic():
        return generate_design_brief_from_library_ar(user_prompt, matching_designs)

    return generate_design_brief_from_library_en(user_prompt, matching_designs)


def generate_design_brief_from_library_en(user_prompt, matching_designs):
    """
    Generate a new original design brief from library references in English.
    """
    category = get_most_common_value(matching_designs, "category", "T-shirt")
    subcategory = get_most_common_value(matching_designs, "subcategory", "Modern clothing piece")
    fit = get_most_common_value(matching_designs, "fit", "Relaxed")
    style = get_most_common_value(matching_designs, "style", "Minimal Streetwear")
    primary_color = get_most_common_value(matching_designs, "primary_color", "Natural neutral color")
    secondary_color = get_most_common_value(matching_designs, "secondary_color", "White or beige")
    pattern = get_most_common_value(matching_designs, "pattern", "Plain")
    graphic_type = get_most_common_value(matching_designs, "graphic_type", "Minimal graphic")
    logo_position = get_most_common_value(matching_designs, "logo_position", "Left chest")
    sleeve_type = get_most_common_value(matching_designs, "sleeve_type", "Standard sleeve")
    neck_type = get_most_common_value(matching_designs, "neck_type", "Crew neck")
    season = get_most_common_value(matching_designs, "season", "All season")
    fabric_look = get_most_common_value(matching_designs, "fabric_look", "Cotton")
    mood = get_most_common_value(matching_designs, "mood", "Clean premium")
    tags = get_all_tags(matching_designs)

    reference_names = []

    for design in matching_designs[:5]:
        reference_names.append(f"- {design['product_name']}")

    reference_text = "\n".join(reference_names)

    image_generation_prompt = (
        f"A clean studio mockup of a {fit.lower()} {category.lower()} "
        f"for an eco-friendly fashion brand called LEAF, "
        f"{primary_color.lower()} main color, {secondary_color.lower()} accents, "
        f"{style.lower()} style, {graphic_type.lower()}, "
        f"logo placed at {logo_position.lower()}, {mood.lower()} mood, "
        f"premium streetwear, realistic fabric, front view, "
        f"high quality fashion product photography"
    )

    brief = f"""
## Generated From Library 🧠🌱

### Your Prompt
> {user_prompt}

### Matching References Used
The system found **{len(matching_designs)}** matching reference design(s).

{reference_text}

---

# New Original Design Brief

## 1. Product Direction
Create a new original **{fit} {category}** for LEAF.

The design should follow a **{style}** direction and should feel **{mood}**.
It should be inspired by the common patterns found in the selected references, but it must not directly copy any single design.

## 2. Suggested Clothing Structure
- **Category:** {category}
- **Subcategory:** {subcategory}
- **Fit:** {fit}
- **Sleeve Type:** {sleeve_type}
- **Neck Type:** {neck_type}
- **Season:** {season}
- **Fabric Look:** {fabric_look}

## 3. Suggested Visual Style
- **Primary Color:** {primary_color}
- **Secondary Color:** {secondary_color}
- **Pattern:** {pattern}
- **Graphic Type:** {graphic_type}
- **Mood:** {mood}
- **Tags:** {tags}

## 4. Logo and Graphic Placement
- Place the LEAF logo around: **{logo_position}**
- Keep the logo clean, readable, and not oversized.
- Use the graphic style: **{graphic_type}**
- Leave enough empty space so the design feels premium.

## 5. Original Concept
Design a fresh LEAF piece that combines:

- the fit logic from the matching references
- the color direction from the library
- the graphic placement patterns found in similar items
- LEAF’s eco-friendly and clean brand identity

The result should look like a new product from LEAF, not a copy of any existing brand.

## 6. Image Generation Prompt For Later

{image_generation_prompt}

## 7. Production Notes
- Use the references as inspiration only.
- Do not copy logos, graphics, or exact layouts from other brands.
- Keep the design balanced and wearable.
- Use a clean LEAF logo placement.
- Make sure the final design can be used later for mockups and product planning.
"""
    return brief


def generate_design_brief_from_library_ar(user_prompt, matching_designs):
    """
    Generate a new original design brief from library references in Arabic.
    """
    category = get_most_common_value(matching_designs, "category", "T-shirt")
    subcategory = get_most_common_value(matching_designs, "subcategory", "قطعة ملابس حديثة")
    fit = get_most_common_value(matching_designs, "fit", "Relaxed")
    style = get_most_common_value(matching_designs, "style", "Minimal Streetwear")
    primary_color = get_most_common_value(matching_designs, "primary_color", "لون طبيعي محايد")
    secondary_color = get_most_common_value(matching_designs, "secondary_color", "أبيض أو بيج")
    pattern = get_most_common_value(matching_designs, "pattern", "Plain")
    graphic_type = get_most_common_value(matching_designs, "graphic_type", "Minimal graphic")
    logo_position = get_most_common_value(matching_designs, "logo_position", "Left chest")
    sleeve_type = get_most_common_value(matching_designs, "sleeve_type", "Standard sleeve")
    neck_type = get_most_common_value(matching_designs, "neck_type", "Crew neck")
    season = get_most_common_value(matching_designs, "season", "All season")
    fabric_look = get_most_common_value(matching_designs, "fabric_look", "Cotton")
    mood = get_most_common_value(matching_designs, "mood", "Clean premium")
    tags = get_all_tags(matching_designs)

    reference_names = []

    for design in matching_designs[:5]:
        reference_names.append(f"- {design['product_name']}")

    reference_text = "\n".join(reference_names)

    image_generation_prompt = (
        f"تصميم موك أب نظيف لقطعة {category} بقَصّة {fit} "
        f"لبراند أزياء صديق للبيئة اسمه LEAF، "
        f"اللون الأساسي {primary_color}، اللون الثانوي {secondary_color}، "
        f"ستايل {style}، نوع الرسمة {graphic_type}، "
        f"الشعار في مكان {logo_position}، إحساس عام {mood}، "
        f"ملابس ستريت وير فخمة، قماش واقعي، منظر أمامي، جودة عالية"
    )

    brief = f"""
## تم التوليد من المكتبة 🧠🌱

### وصفك للتصميم
> {user_prompt}

### المراجع المستخدمة
وجد النظام **{len(matching_designs)}** مرجع تصميم مطابق.

{reference_text}

---

# فكرة تصميم أصلية جديدة

## 1. اتجاه المنتج
صمّم قطعة جديدة وأصلية من نوع **{category}** بقَصّة **{fit}** لبراند LEAF.

يجب أن يتبع التصميم اتجاه **{style}** وأن يعطي إحساساً عاماً **{mood}**.
يجب أن يكون مستوحى من الأنماط المشتركة في المراجع، لكن بدون نسخ أي تصميم بشكل مباشر.

## 2. هيكل قطعة الملابس المقترح
- **الفئة:** {category}
- **الفئة الفرعية:** {subcategory}
- **القَصّة / المقاس:** {fit}
- **نوع الكم:** {sleeve_type}
- **نوع الرقبة:** {neck_type}
- **الموسم:** {season}
- **شكل القماش:** {fabric_look}

## 3. الاتجاه البصري المقترح
- **اللون الأساسي:** {primary_color}
- **اللون الثانوي:** {secondary_color}
- **النمط:** {pattern}
- **نوع الرسمة:** {graphic_type}
- **الإحساس العام:** {mood}
- **الكلمات المفتاحية:** {tags}

## 4. مكان الشعار والرسمة
- ضع شعار LEAF في منطقة: **{logo_position}**
- اجعل الشعار واضحاً ونظيفاً وليس كبيراً أكثر من اللازم.
- استخدم نوع الرسمة: **{graphic_type}**
- اترك مساحة فارغة كافية حتى يبدو التصميم فخماً ومتوازناً.

## 5. الفكرة الأصلية
اصنع قطعة جديدة لبراند LEAF تجمع بين:

- منطق القَصّة الموجود في المراجع المطابقة
- اتجاه الألوان الموجود في المكتبة
- أماكن الرسومات والشعارات المتكررة في العناصر المشابهة
- هوية LEAF النظيفة والصديقة للبيئة

النتيجة يجب أن تبدو كمنتج جديد من LEAF، وليس نسخة من أي براند موجود.

## 6. وصف توليد الصورة لاحقاً

{image_generation_prompt}

## 7. ملاحظات إنتاجية
- استخدم المراجع كمصدر إلهام فقط.
- لا تنسخ الشعارات أو الرسومات أو التخطيطات من أي براند آخر.
- حافظ على توازن التصميم وقابليته للارتداء.
- استخدم مكاناً نظيفاً وواضحاً لشعار LEAF.
- اجعل التصميم مناسباً لاحقاً للموك أب والتخطيط الإنتاجي.
"""
    return brief