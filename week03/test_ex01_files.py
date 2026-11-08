from ex01_files import (
    append_line,
    file_stats,
    find_files,
    read_lines,
    read_or_default,
    write_lines,
)


def test_write_lines(tmp_path):
    path = tmp_path / "a.txt"
    write_lines(path, ["hello", "world"])
    assert path.read_text(encoding="utf-8") == "hello\nworld\n"


def test_write_lines_overwrites(tmp_path):
    path = tmp_path / "a.txt"
    write_lines(path, ["old", "stuff"])
    write_lines(path, ["new"])
    assert path.read_text(encoding="utf-8") == "new\n"


def test_read_lines(tmp_path):
    path = tmp_path / "a.txt"
    path.write_text("hello\nworld\n", encoding="utf-8")
    assert read_lines(path) == ["hello", "world"]


def test_read_lines_unicode(tmp_path):
    path = tmp_path / "names.txt"
    path.write_text("Muñoz\nمحمد\n", encoding="utf-8")
    assert read_lines(path) == ["Muñoz", "محمد"]


def test_append_line(tmp_path):
    path = tmp_path / "log.txt"
    append_line(path, "first")
    append_line(path, "second")
    assert path.read_text(encoding="utf-8") == "first\nsecond\n"


def test_file_stats(tmp_path):
    path = tmp_path / "s.txt"
    path.write_text("hi there\nbye\n", encoding="utf-8")
    assert file_stats(path) == {"lines": 2, "words": 3, "chars": 13}


def test_file_stats_empty(tmp_path):
    path = tmp_path / "empty.txt"
    path.write_text("", encoding="utf-8")
    assert file_stats(path) == {"lines": 0, "words": 0, "chars": 0}


def test_read_or_default(tmp_path):
    path = tmp_path / "x.txt"
    path.write_text("content", encoding="utf-8")
    assert read_or_default(path) == "content"
    assert read_or_default(tmp_path / "missing.txt") == ""
    assert read_or_default(tmp_path / "missing.txt", "N/A") == "N/A"


def test_find_files(tmp_path):
    for name in ["mar.csv", "jan.csv", "notes.txt"]:
        (tmp_path / name).write_text("x", encoding="utf-8")
    sub = tmp_path / "sub"
    sub.mkdir()
    (sub / "hidden.csv").write_text("x", encoding="utf-8")
    assert find_files(tmp_path, ".csv") == ["jan.csv", "mar.csv"]
    assert find_files(tmp_path, ".json") == []
