#!/usr/bin/env python3
"""
JSON Formatter - A tool to format JSON according to common style guidelines
Following best practices similar to PEP 8 principles adapted for JSON
"""

import json
import sys
import argparse


def format_json(input_data, indent=2, sort_keys=True, ensure_ascii=False):
    """
    Format JSON data with proper indentation and ordering
    
    Args:
        input_data: JSON string or object to format
        indent: Number of spaces for indentation (default: 2)
        sort_keys: Whether to sort keys alphabetically (default: True)
        ensure_ascii: Whether to escape non-ASCII characters (default: False)
    
    Returns:
        Formatted JSON string
    """
    try:
        # Parse the input if it's a string
        if isinstance(input_data, str):
            parsed = json.loads(input_data)
        else:
            parsed = input_data
        
        # Format with specified options
        formatted = json.dumps(
            parsed,
            indent=indent,
            sort_keys=sort_keys,
            ensure_ascii=ensure_ascii,
            separators=(',', ': ')  # Standard separator spacing
        )
        
        return formatted
    
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON input: {e}")


def main():
    parser = argparse.ArgumentParser(description='Format JSON according to style guidelines')
    parser.add_argument('input_file', nargs='?', type=argparse.FileType('r'), default=sys.stdin,
                       help='Input JSON file (reads from stdin if not provided)')
    parser.add_argument('-o', '--output', type=argparse.FileType('w'), default=sys.stdout,
                       help='Output file (writes to stdout if not provided)')
    parser.add_argument('-i', '--indent', type=int, default=2,
                       help='Number of spaces for indentation (default: 2)')
    parser.add_argument('--no-sort-keys', action='store_true',
                       help='Do not sort keys alphabetically')
    parser.add_argument('--ensure-ascii', action='store_true',
                       help='Escape non-ASCII characters')
    
    args = parser.parse_args()
    
    try:
        # Read input
        input_content = args.input_file.read()
        
        # Format JSON
        formatted = format_json(
            input_data=input_content,
            indent=args.indent,
            sort_keys=not args.no_sort_keys,
            ensure_ascii=args.ensure_ascii
        )
        
        # Write output
        args.output.write(formatted + '\n')
        
        if args.input_file != sys.stdin:
            args.input_file.close()
        if args.output != sys.stdout:
            args.output.close()
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()