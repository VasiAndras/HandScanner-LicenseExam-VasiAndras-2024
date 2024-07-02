#!/bin/bash

UI_DIR="uiFiles"
PY_DIR="pyFiles"

mkdir -p "$PY_DIR"

for ui_file in "$UI_DIR"/*.ui; do
  base_name=$(basename "$ui_file" .ui)
  output_file="$PY_DIR/${base_name}.py"
  pyuic5 -o "$output_file" "$ui_file"
  echo "$output_file"
done
