"""Model comparison helpers."""


def compare_models(left: dict, right: dict) -> dict:
    """Return keys whose values differ between two model metadata mappings."""
    keys = set(left) | set(right)
    return {
        key: (left.get(key), right.get(key))
        for key in sorted(keys)
        if left.get(key) != right.get(key)
    }
