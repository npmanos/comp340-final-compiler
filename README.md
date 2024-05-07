## Requirements

- Tested with Python 3.12
- Should work with Python 3.10 or higher

## Installation

Install the optional dependencies by running pip install -r requirements.txt
(though it should work without them).

I have spent years trying, but I still don't understand how Python's imports and
packages work. Putting all the files in one package gave me endless grief. As
such, the following directory structure must be used:

```text
.

├── compiler

│   ├── __init__.py

│   ├── binarytree.py

│   ├── simple_evaluator.py

│   ├── simple_parser.py

│   ├── simple_tokenizer.py

│   └── simple_tokens.py

├── main.py

└── requirements.txt
```

## Usage

`python main.py`
