import json

from ex02_json_csv import csv_to_json, load_json, read_csv, save_json, sum_column, write_csv


def test_save_and_load_json(tmp_path):
    path = tmp_path / "data.json"
    data = [{"title": "Dune", "price": 9.5}, {"title": "Emma", "price": 4.0}]
    save_json(path, data)
    assert json.loads(path.read_text(encoding="utf-8")) == data
    assert load_json(path, []) == data


def test_save_json_is_indented(tmp_path):
    path = tmp_path / "data.json"
    save_json(path, {"a": 1})
    assert "\n" in path.read_text(encoding="utf-8")


def test_load_json_missing_file(tmp_path):
    assert load_json(tmp_path / "nope.json", []) == []
    assert load_json(tmp_path / "nope.json", {"x": 1}) == {"x": 1}


def test_load_json_broken_file(tmp_path):
    path = tmp_path / "broken.json"
    path.write_text("{oops", encoding="utf-8")
    assert load_json(path, []) == []


def test_read_csv(tmp_path):
    path = tmp_path / "books.csv"
    path.write_text("title,price\nDune,9.5\nEmma,4.0\n", encoding="utf-8")
    assert read_csv(path) == [
        {"title": "Dune", "price": "9.5"},
        {"title": "Emma", "price": "4.0"},
    ]


def test_write_csv(tmp_path):
    path = tmp_path / "out.csv"
    rows = [{"name": "Ali", "score": 90}, {"name": "Sara", "score": 94}]
    write_csv(path, rows, ["name", "score"])
    with open(path, newline="", encoding="utf-8") as f:
        text = f.read()
    assert text.replace("\r\n", "\n") == "name,score\nAli,90\nSara,94\n"
    assert read_csv(path) == [{"name": "Ali", "score": "90"}, {"name": "Sara", "score": "94"}]


def test_sum_column(tmp_path):
    path = tmp_path / "e.csv"
    path.write_text("desc,amount\nPizza,30\nBad,oops\nTaxi,10.5\nEmpty,\n", encoding="utf-8")
    assert sum_column(path, "amount") == (40.5, 2)


def test_sum_column_floats(tmp_path):
    path = tmp_path / "e.csv"
    path.write_text("amount\n0.1\n0.2\n", encoding="utf-8")
    assert sum_column(path, "amount") == (0.3, 0)


def test_csv_to_json(tmp_path):
    csv_path = tmp_path / "b.csv"
    json_path = tmp_path / "b.json"
    csv_path.write_text("title,price\nDune,9.5\nEmma,4.0\n", encoding="utf-8")
    assert csv_to_json(csv_path, json_path) == 2
    assert json.loads(json_path.read_text(encoding="utf-8")) == [
        {"title": "Dune", "price": "9.5"},
        {"title": "Emma", "price": "4.0"},
    ]
