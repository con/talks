%.png: %.svg
	@echo "Rendering $@"
	-rm -f "$@"
	@inkscape --export-filename "$@" -d 150 "$<"
	git annex add "$@"
	git annex metadata --set derived-from="$<" "$@"

#
# SVGTune
#
# SVGTUNE_OPTS is meant to be overridden per target.  Use --previews for
# artwork that does not survive a non-Inkscape renderer -- Inkscape flowed
# text (<flowRoot>, which browsers and librsvg drop) or fonts a viewer is
# unlikely to have -- so the slides can reference the rendered PNG instead
# of the SVG.
SVGTUNE_OPTS ?=

%_tuned: %.svgtune %.svg
	@echo "Splitting SVG using $<"
	@svgtune $(SVGTUNE_OPTS) $<
# Touch it to adjust the timestamp so make does not think that we are
# out of date later on
	@touch "$@"


# The STAMPED poster keeps its note boxes in <flowRoot> and uses Latin
# Modern / Droid Sans, so its extracts render blank boxes in a browser:
# also produce *_preview.png and point the slides at those.
repronim-containers-stamped_tuned: SVGTUNE_OPTS = --previews
