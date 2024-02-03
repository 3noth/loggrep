#!/usr/bin/env python3

import argparse
import re
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Путь к входному файлу лога")
    parser.add_argument("--output", "-O", help="Путь к выходному файлу")
    parser.add_argument("--keywords", "-K", required=True, nargs="+", help="Ключевые слова для поиска")
    parser.add_argument("--id-pattern", "-Id", help="Шаблон для идентификации уникального идентификатора")
    parser.add_argument("--line-pattern", "-Ld", help="Шаблон для обработки строк")
    return parser.parse_args()

def filter_lines_by_keywords(lines, keywords):
    return [line for line in lines if any(keyword in line for keyword in keywords)]

def split_lines_by_id(lines, id_pattern=None):
    split_results = {}
    for line in lines:
        if id_pattern:
            match = re.search(id_pattern, line)
            if match:
                id_value = match.group()
                if id_value not in split_results:
                    split_results[id_value] = []
                split_results[id_value].append(line)
        else:
            split_results.setdefault("default", []).append(line)
    return split_results


def apply_line_pattern(lines, line_pattern):
    if not line_pattern:
        return lines
    pattern = re.compile(line_pattern)
    return [pattern.search(line).group() for line in lines if pattern.search(line)]


def main():
    args = parse_args()

    with open(args.input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    filtered_lines = filter_lines_by_keywords(lines, args.keywords)

    if args.id_pattern or args.line_pattern:
        if args.id_pattern:
            split_lines = split_lines_by_id(filtered_lines, args.id_pattern)
            for id_value, lines in split_lines.items():
                if args.output:
                    output_path = os.path.join(args.output, f"{id_value}.txt")
                    with open(output_path, 'w', encoding='utf-8') as f:
                        for line in lines:
                            f.write(line)
                else:
                    for line in lines:
                        print(line)
        if args.line_pattern:
            processed_lines = apply_line_pattern(filtered_lines, args.line_pattern)
            if args.output:
                with open(args.output, 'w', encoding='utf-8') as f:
                    for line in processed_lines:
                        f.write(f"{line}\n")
            else:
                for line in processed_lines:
                    print(line)
    else:
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                for line in filtered_lines:
                    f.write(line)
        else:
            for line in filtered_lines:
                print(line)


if __name__ == "__main__":
    main()
