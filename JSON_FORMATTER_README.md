# JSON Formatter

A Python-based JSON formatting tool that follows common style guidelines similar to PEP 8 principles adapted for JSON.

## Features

- Proper indentation (default 2 spaces)
- Alphabetical key sorting
- Clean spacing around separators
- Command-line interface
- File input/output support

## Usage

### Basic Usage
```bash
python json_fmt.py input.json
```

### With Options
```bash
# Specify indentation size
python json_fmt.py -i 4 input.json

# Output to a file
python json_fmt.py input.json -o output.json

# Don't sort keys
python json_fmt.py --no-sort-keys input.json

# Ensure ASCII characters
python json_fmt.py --ensure-ascii input.json
```

### From Stdin
```bash
echo '{"name":"John","age":30}' | python json_fmt.py
```

## Options

- `-i, --indent`: Number of spaces for indentation (default: 2)
- `-o, --output`: Output file (writes to stdout if not provided)
- `--no-sort-keys`: Do not sort keys alphabetically
- `--ensure-ascii`: Escape non-ASCII characters

## Example

**Input:**
```json
{"name":"John","age":30,"city":"New York","hobbies":["reading","swimming"],"address":{"street":"123 Main St","zipcode":"10001"}}
```

**Output:**
```json
{
  "address": {
    "street": "123 Main St",
    "zipcode": "10001"
  },
  "age": 30,
  "city": "New York",
  "hobbies": [
    "reading",
    "swimming"
  ],
  "name": "John"
}
```

The formatter sorts keys alphabetically and applies consistent indentation for better readability.