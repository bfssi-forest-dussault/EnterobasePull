# EnterobasePull

This script allows for simple retrieval/update of the Enterobase schemes.

Currently requires a separate config file with your API token and some other parameters.
The config file must be in the same folder as the `EnterobasePull.py` script. See below for an example.

**config.py**
```python
from pathlib import Path

OUTDIR = Path("/home/your_name/Enterobase")
SERVER_ADDRESS = 'http://enterobase.warwick.ac.uk'
DATABASE = 'senterica'
SCHEME_LIST = ['wgMLST',
               'cgMLST',
               'cgMLST_v2',
               'MLST_Achtman']
API_TOKEN = "your secret API token goes here"
```