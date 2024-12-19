import os
import pytest
from file_finder import find_files

@pytest.fixture
def create_test_environment(tmp_path):
    """
    Create a temporary test directory structure for testing.
    """
    # Create directories and files
    dir_a = tmp_path / "dir_a"
    dir_a.mkdir()
    dir_b = tmp_path / "dir_b"
    dir_b.mkdir()

    file1 = dir_a / "file1.md"
    file1.write_text("# Markdown File 1")

    file2 = dir_a / "file2.txt"
    file2.write_text("This is a text file.")

    file3 = dir_b / "notes.md"
    file3.write_text("# Notes Markdown")

    file4 = dir_b / "report.docx"
    file4.write_text("This is a Word document.")

    return tmp_path

def test_find_files_by_extension(create_test_environment):
    """
    Test finding files by their extension.
    """
    base_dir = create_test_environment

    # Find all .md files
    md_files = find_files(str(base_dir), extension=".md")
    assert len(md_files) == 2
    assert any("file1.md" in file for file in md_files)
    assert any("notes.md" in file for file in md_files)

def test_find_files_by_pattern(create_test_environment):
    """
    Test finding files by filename pattern.
    """
    base_dir = create_test_environment

    # Find files containing "file" in their name
    pattern_files = find_files(str(base_dir), pattern="file")
    assert len(pattern_files) == 2
    assert any("file1.md" in file for file in pattern_files)
    assert any("file2.txt" in file for file in pattern_files)

def test_find_files_by_extension_and_pattern(create_test_environment):
    """
    Test finding files by both extension and pattern.
    """
    base_dir = create_test_environment

    # Find .md files with "notes" in their name
    filtered_files = find_files(str(base_dir), extension=".md", pattern="notes")
    assert len(filtered_files) == 1
    assert "notes.md" in filtered_files[0]

def test_find_files_no_matches(create_test_environment):
    """
    Test case where no files match the criteria.
    """
    base_dir = create_test_environment

    # Find .csv files (none exist)
    csv_files = find_files(str(base_dir), extension=".csv")
    assert len(csv_files) == 0

    # Find files with "nonexistent" in their name
    nonexistent_files = find_files(str(base_dir), pattern="nonexistent")
    assert len(nonexistent_files) == 0
