"""Offline smoke test for the text preprocessing example."""

import runpy

import matplotlib.pyplot as plt


def test_preprocessing_filters_known_tokens(monkeypatch, tmp_path):
    """Read sample records and verify the cleaning result and count summary."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    (data_dir / "text_data.txt").write_text(
        "The DOG, and cats!\nDogs run. The dog sleeps.\n", encoding="utf-8"
    )

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(plt, "show", lambda: plt.close("all"))

    result = runpy.run_module("nlp.text_preprocessing", run_name="__main__")

    assert result["clean_tokens"] == ["dog", "cats", "dogs", "run", "dog", "sleeps"]
    assert (
        result["freq_df"].filter(result["pl"].col("token") == "dog")["len"].item() == 2
    )
    assert result["count_of_clean_tokens"] == 6
