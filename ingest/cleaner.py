import re

def clean_content(raw_content: str) -> str:
    """
    Clean raw content by removing Markdown/HTML tags and special characters.
    
    Args:
        raw_content (str): The raw file content.
    
    Returns:
        str: Cleaned content.
    """
    # Remove Markdown syntax
    cleaned = re.sub(r"\{([^}]*)\}", '', raw_content)
    cleaned = re.sub(r"\[.*?\]", '', cleaned)
    cleaned = re.sub(r"\(.*?\)", '', cleaned)
    cleaned = re.sub(r"<.*?>", '', cleaned)
    cleaned = cleaned.replace("#", "").strip()
    
    # Replace multiple spaces with a single space
    cleaned = re.sub(r"\s+", " ", cleaned)
    
    return cleaned
