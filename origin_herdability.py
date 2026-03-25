#!/usr/bin/env python3

import re

if __name__ == "__main__":
    herit_pattern_str = r"\b(?:herit|inherit)\w*"
    herit_pattern = re.compile(herit_pattern_str, re.IGNORECASE)

    input_file  = "origin.txt"    
    output_file = "herit_results.txt"

    results = []
    with open(input_file, "r", encoding="utf-8", errors="replace") as fh:
        for line_num, line in enumerate(fh, start=1):
            for match in herit_pattern.finditer(line):
                results.append((line_num, match.group()))

    with open(output_file, "w", encoding="utf-8") as out:
        for line_num, word in results:
            out.write(f"{line_num}\t{word}\n")

    print(f"Found {len(results)} match(es). Results saved to '{output_file}'.")
