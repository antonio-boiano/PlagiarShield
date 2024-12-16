
# PlagiarShield

PlagiarShield is a powerful tool designed to detect plagiarism in source files by comparing them with others in a specified directory.
## Installation

PlagiarShield uses the standard Python 'setup.py' installation file.

Install PlagiarShield with the following command:

1. **Clona the repository:**

   ```bash
   git clone https://github.com/antonio-boiano/PlagiarShield.git
   cd PlagiarShield
2. **Create a virtaul enviroment and enable it (OPTIONAL)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
3. **Install PlagiarShield**
   ```bash
   python3 -m pip install .
   
Usage
================
PlagiarShield provides a command-line interface (CLI) for flexible usage. Below are the available options and examples for using the tool.

### Command Syntax

```bash
PlagiarShield directory --file <pattern> [options]
```

### Arguments and Options

| Argument/Option     | Description                                                                                       |
|---------------------|---------------------------------------------------------------------------------------------------|
| `directory`         | The directory to search for files.                                                               |
| `--file`, `-f`      | File pattern to search for, e.g., `*.txt`, `homework*.pdf`, `*route.nc`. **(Required)**           |
| `--filetype`, `-t`  | Force a specific file type (e.g., `pdf`, `txt`, `nc`). Default: inferred from file extension.     |
| `--similarity`, `-s`| Similarity threshold (float) to consider two files as similar. Default: `0.8` (80%).             |
| `-r` or `-R`        | Perform a recursive search in subdirectories. Only one of these can be used at a time.           |

### Examples

#### 1. Compare `.txt` files in a directory

```bash
PlagiarShield /path/to/directory --file "*.txt"
```

This command compares all `.txt` files in the specified directory.

#### 2. Specify a similarity threshold

```bash
PlagiarShield /path/to/directory --file "*.txt" --similarity 0.9
```

This will only consider files as similar if their similarity score is 90% or higher.

#### 3. Force file type

```bash
PlagiarShield /path/to/directory --file "*.data" --filetype "txt"
```

This command forces the tool to treat `.data` files as text files.

#### 4. Recursive search

```bash
PlagiarShield /path/to/directory --file "*.pdf" -r
```

Perform a recursive search in the specified directory and its subdirectories.

### Output

- The tool prints a list of file pairs that are above the similarity threshold.
- It also provides a detailed similarity score for each pair.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is distributed under the MIT License. See the [LICENSE](LICENSE) file for details.
