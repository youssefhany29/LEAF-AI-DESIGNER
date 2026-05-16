from collections import Counter
from src.translations import get_text


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
    Generate a manual rule-based design brief.
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


def generate_design_brief_from_library(user_prompt, matching_designs):
    """
    Generate a new original design brief by reading metadata from matching library designs.
    """
    if len(matching_designs) == 0:
        return f"""
    ## {get_text("no_matching_refs_title")}

    {get_text("no_matching_refs_body")}
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