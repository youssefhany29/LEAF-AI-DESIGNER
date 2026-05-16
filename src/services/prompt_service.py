def improve_prompt(prompt):
    """
    Improve a basic image generation prompt using a rule-based enhancer.

    Later, this function can be replaced with a real AI prompt-improvement model.
    """
    if not prompt:
        return ""

    extra_details = (
        " clean studio lighting, realistic fabric texture, high quality fashion product photography, "
        "front view, centered composition, premium streetwear look, detailed garment shape, "
        "clear logo placement, professional clothing mockup, no watermark, no copied brand logo"
    )

    lower_prompt = prompt.lower()

    if "studio" in lower_prompt or "realistic fabric" in lower_prompt:
        return prompt

    return prompt.strip() + "," + extra_details


def prompt_to_txt(title, prompt, notes):
    """
    Create TXT content for exporting an image generation prompt.
    """
    content = f"""
LEAF AI Designer - Image Prompt

Title:
{title}

Prompt:
{prompt}

Notes:
{notes if notes else "No notes"}
"""
    return content.strip()