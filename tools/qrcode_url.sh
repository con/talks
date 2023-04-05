#!/bin/bash

set -eux
cd $(realpath "$0" | xargs dirname | xargs dirname)

pwd
url="$1"

out="${url##*/}"
out="pics/${out%%.*}-qrcode.png"


datalad run -m "Produce QR code for $url" --output "$out" --explicit qrencode -s 50 -d 300 -l H -o "$out" "$url"

echo "Done. Output file: $out"
