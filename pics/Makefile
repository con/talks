%.png: %.svg
	@echo "Rendering $@"
	-rm -f "$@"
	@inkscape --export-filename "$@" -d 150 "$<"
	git annex add "$@"
	git annex metadata --set derived-from="$<" "$@"
