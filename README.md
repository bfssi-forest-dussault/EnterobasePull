# EnterobasePull

This script allows for simple retrieval/update of the Enterobase schemes.

Currently requires a separate config file with your API token and a
desired output directory. The config file must be in the same folder as
the `EnterobasePull.py` script. See below for an example.

**config.py**
```python
from pathlib import Path

OUTDIR = Path("/home/your_name/Enterobase")
API_TOKEN = "your secret API token goes here"
```