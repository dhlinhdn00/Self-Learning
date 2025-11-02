#!/bin/bash

FILE_NAME="Implementation.c++"
OUTPUT_NAME="Implementation"

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
