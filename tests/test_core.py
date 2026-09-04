from modelwatch import compare_models


def test_compare_models():
    assert compare_models({"version": 1}, {"version": 2}) == {"version": (1, 2)}
