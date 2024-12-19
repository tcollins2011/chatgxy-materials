import frontmatter

def parse_file(path: str) -> tuple[dict, str]:
    """
    Parse a file and extract its metadata and content.

    Args:
        path (str): Path to the file.
    
    Returns:
        tuple[dict, str]: A tuple containing metadata (dict) and content (str).
    """
    try:
        post = frontmatter.load(path)
        metadata = post.metadata
        content = post.content
        return metadata, content
    except Exception as e:
        raise ValueError(f"Error parsing file {path}: {e}")
