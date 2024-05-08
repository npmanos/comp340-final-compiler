My first submission had every file attached except the screen recording. I
rushed to try and resubmit it before midnight. I uploaded at exactly midnight,
had the video, but missed a few other files. (I'm operating on *very* little
sleep.)

This submission has every file. I hope you'll accept the first two submissions
as proof that I had all parts of the assignment completed by the deadline.

## Requirements

- Tested with Python 3.12
- Should work with Python 3.10 or higher

## Installation

Install the optional dependencies by running `pip install -r requirements.txt`
(though it should work without them).

I have spent years trying, but I still don't understand how Python's imports and
packages work. Putting all the files in one package gave me endless grief. As
such, the following directory structure must be used:

```text
.
├── compiler
│   ├── __init__.py
│   ├── _utils.py
│   ├── binarytree.py
│   ├── simple_baby.py
│   ├── simple_evaluator.py
│   ├── simple_parser.py
│   ├── simple_tokenizer.py
│   └── simple_tokens.py
├── main.py
└── requirements.txt
```

## Usage

`python main.py`
