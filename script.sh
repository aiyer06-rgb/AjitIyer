#!/bin/bash

FILES=()

# Reads all the files in the current directory
while IFS= read -r file; do
    FILES+=("$file")
done < <(find . -maxdepth 1 -type f | sed 's|^\./||')

# Program will exit if there are no files in the directory with a warning
if [ "${#FILES[@]}" -eq 0 ]; then
    echo "No files in this directory."
    exit 1
fi

# Displays the list of files with corresponding numbers
echo "Select which files you want to create a zip file:"
for i in "${!FILES[@]}"; do
    printf "%d) %s\n" $((i+1)) "${FILES[$i]}"
done

# Prompts user for input when selecting files and naming the zip file
echo
read -p "Enter file numbers separated by spaces: " SELECTION
read -p "Enter name for zip file without the .zip extension: " ZIP_NAME

SELECTED_FILES=()

for num in $SELECTION; do
# Validates user input
    if ! [[ "$num" =~ ^[0-9]+$ ]]; then
        echo "Unacceptable input: $num"
        exit 1
    fi
# Adjusts for zero-based indexing
    index=$((num-1))
    if [[ "$index" -ge 0 && "$index" -lt "${#FILES[@]}" ]]; then
        SELECTED_FILES+=("${FILES[$index]}")
    else
        echo "Unacceptable selection: $num"
        exit 1
    fi
done

# Checks if any files were selected
if [ "${#SELECTED_FILES[@]}" -eq 0 ]; then
    echo "No files were selected."
    exit 1
fi

zip "$ZIP_NAME.zip" "${SELECTED_FILES[@]}"

echo "Created $ZIP_NAME.zip with ${#SELECTED_FILES[@]} files."
