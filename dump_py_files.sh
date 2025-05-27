#!/bin/zsh

OUTPUT_FILE="project_dump.txt"
: > "$OUTPUT_FILE"

find . -type f \( -name "*.py" -o -name "*.json" \) -print0 | while IFS= read -r -d '' rel_path; do
    # Remove leading ./ for cleaner output
    clean_path="${rel_path#./}"
    echo "$clean_path" >> "$OUTPUT_FILE"
    echo '```' >> "$OUTPUT_FILE"
    cat "$rel_path" >> "$OUTPUT_FILE"
    echo '```' >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
done

echo "Dumped files to $OUTPUT_FILE"
