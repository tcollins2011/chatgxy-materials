import os
import re
from typing import List

def find_files(directory: str, extension: str = None, pattern: str = None) -> List[str]:
    """
    Find files in a directory based on the specified extension and/or filename pattern.

    Args:
        directory (str): The root directory to search for files.
        extension (str, optional): File extension to filter by (e.g., ".md", ".txt").
        pattern (str, optional): Substring or regex pattern to match filenames.

    Returns:
        List[str]: A list of file paths matching the criteria.
    """
    files_found = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
 
            if extension and not file.endswith(extension):
                continue
            
            if pattern and not re.search(pattern, file):
                continue
            
            files_found.append(os.path.join(root, file))
    
    return files_found

