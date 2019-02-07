# EnterobasePull

This script allows for simple retrieval/update of the Enterobase schemes.

Currently requires a separate config file with your API token and some other parameters.
The config file must be in the same folder as the `EnterobasePull.py` script. See below for an example.

**config.py**
```python
from pathlib import Path

OUTDIR = Path("/home/your_name/Enterobase")
API_TOKEN = "your secret API token goes here"

SERVER_ADDRESS = 'http://enterobase.warwick.ac.uk'
DATABASE = 'senterica'
SCHEME_LIST = ['cgMLST_v2',
               'MLST_Achtman']
```

## Notes on config.py
Note that there are several databases available on EnteroBase:
- Salmonella
- Escherichia/Shigella
- Clostridioides
- Vibrio
- Yersinia
- Helicobacter
- Moraxella

Each of these **requires its own API key**.

The names of the databases and scheme lists are not immediately clear on the EnteroBase documentation, so here's a table of the available schemes for E. coli and Salmonella:

| Database   | Database keyword | Scheme keyword |
| ---------- | ---------------- | -------------- |
| Salmonella | senterica        | MLST_Achtman      |
|  |         | cgMLST_v2   |
|  |         | rMLST   |
|  |         | wgMLST   |
| Escherichia/Shigella | ecoli        | MLST_Achtman      |
|  |         | rMLST   |
|  |         | cgMLST   |

Enter these values into your *config.py* file accordingly.

To view schemes for other databases, you'll need to send a GET request to http://enterobase.warwick.ac.uk/api/v2.0/DATABASE_NAME_HERE/schemes.
Note that your username must be your API token, and you'll need to set the Content-Type to application/json in the header of your request. I suggest using [PostMan](https://www.getpostman.com/) to do this easily.