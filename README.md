# modelwatch

Lightweight model metadata comparison utilities.

## Install

```bash
pip install -e .
```

## Usage

```python
from modelwatch import compare_models

changes = compare_models({"version": "1", "family": "demo"}, {"version": "2", "family": "demo"})
print(changes)
```

## Test

```bash
pytest
```

## License

MIT

Built by meduuv. `guns.lol/meduu`
