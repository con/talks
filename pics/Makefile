%.png: %.svg
	@echo "Rendering $@"
	-rm -f "$@"
	@inkscape --export-filename "$@" -d 150 "$<"
	git annex add "$@"
	git annex metadata --set derived-from="$<" "$@"

#
# SVGTune
#
%_tuned: %.svgtune %.svg
	@echo "Splitting SVG using $<"
	@svgtune $<
# Touch it to adjust the timestamp so make does not think that we are
# out of date later on
	@touch "$@"

