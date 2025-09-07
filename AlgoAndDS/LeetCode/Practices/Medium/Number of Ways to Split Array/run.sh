#!/bin/bash

FILE_NAME="Solutions.c++"
OUTPUT_NAME="Solutions"

if [ ! -f "$FILE_NAME" ]; then
    echo "Error: $FILE_NAME not found!"
    exit 1
fi

echo "Compiling $FILE_NAME..."
g++ -o $OUTPUT_NAME $FILE_NAME
if [ $? -ne 0 ]; then
    echo "Compilation failed!"
    exit 1
fi

echo "Running $OUTPUT_NAME..."
./$OUTPUT_NAME
