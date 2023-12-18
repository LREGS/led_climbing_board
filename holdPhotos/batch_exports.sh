#!/bin/bash

output_dir="./output"

mkdir -p "$output_dir"

for file in *.xcf; do
    output_file="$output_dir/$(basename "$file" .xcf).jpg"
    gimp -i -b "(let* ((image (car (gimp-file-load RUN-NONINTERACTIVE \"$file\" \"$file\")))
                        (drawable (car (gimp-image-get-active-layer image))))
                    (gimp-image-scale image (round (* 0.132 (gimp-image-width image))) (round (* 0.132 (gimp-image-height image))))
                    (file-jpeg-save RUN-NONINTERACTIVE image drawable \"$output_file\" \"$output_file\" 0.9 0 1 0 \"\" 0 1 0 0)
                    (gimp-image-delete image))" -b "(gimp-quit 0)"
done
