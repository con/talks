#!/bin/bash
#
# Generate index.html listing all talks and posters from the "Chronology"
# table of INDEX.md, newest first, styled to loosely match
# https://centerforopenneuroscience.org/.
#
# Usage: tools/create_index.sh   (run from repo root, or anywhere)

set -eu

# Resolve repo root (parent of tools/)
REPO_ROOT="$(cd "$(dirname "$(realpath "$0")")/.." && pwd)"
cd "$REPO_ROOT"

OUT="index.html"

# HTML-escape a string (&, <, >, ", ')
html_escape() {
    sed -e 's/&/\&amp;/g' \
        -e 's/</\&lt;/g' \
        -e 's/>/\&gt;/g' \
        -e 's/"/\&quot;/g' \
        -e "s/'/\&#39;/g"
}

# Entries come from the "## Chronology" table of INDEX.md, one row per
# talk or poster: | Date | Kind | Entry | Title | Date from |.  Entry holds
# the path in backticks, optionally followed by a print PDF.  Rows are
# turned into "date|path|title|kind|pdf" and sorted newest first (stable,
# so rows sharing a date keep the table's order).
mapfile -t ENTRIES < <(
    awk '
        /^## / { in_table = ($0 == "## Chronology") }
        in_table && /^\| [0-9]{4}-[0-9]{2}/ {
            n = split($0, c, / \| /)
            date = c[1]; sub(/^\| */, "", date)
            kind = c[2]; title = c[4]
            gsub(/^ +| +$/, "", kind); gsub(/^ +| +$/, "", title)
            gsub(/\\\|/, "|", title)
            m = split(c[3], p, "`")
            pdf = (m >= 5) ? p[4] : ""
            print date "|" p[2] "|" title "|" (kind == "talk" ? "" : kind) "|" pdf
        }' INDEX.md | sort -s -t'|' -k1,1 -r
)

# A root deck missing from the table would silently drop off the index
for f in 20*.html 20*.pdf; do
    [ -e "$f" ] || continue
    printf '%s\n' "${ENTRIES[@]}" | grep -q "^[^|]*|$f|" \
        || echo "WARNING: $f is not in the Chronology table of INDEX.md" >&2
done

if [ "${#ENTRIES[@]}" -eq 0 ]; then
    echo "No entries found in the Chronology table of $REPO_ROOT/INDEX.md" >&2
    exit 1
fi

# Build list items grouped by year
list_items=""
prev_year=""
listed=0
for e in "${ENTRIES[@]}"; do
    IFS='|' read -r date f raw_title kind pdf <<<"$e"
    # Skip work-in-progress decks
    case "$raw_title" in '[WiP]'*|'[WIP]'*|'[wip]'*) continue ;; esac
    year="${date:0:4}"
    title=$(echo "$raw_title" | html_escape)
    name_escaped=$(echo "$f" | html_escape)
    extra=""
    [ -n "$kind" ] && extra+=" <span class=\"kind\">${kind}</span>"
    [ -n "$pdf" ] && extra+=" (<a class=\"alt\" href=\"$(echo "$pdf" | html_escape)\">PDF</a>)"
    if [ "$year" != "$prev_year" ]; then
        if [ -n "$prev_year" ]; then
            list_items+="      </ul>"$'\n'
        fi
        list_items+="      <h2>${year}</h2>"$'\n'
        list_items+="      <ul class=\"talks\">"$'\n'
        prev_year="$year"
    fi
    listed=$((listed + 1))
    list_items+="        <li><a href=\"${name_escaped}\">${title}</a>${extra} <span class=\"file\">${name_escaped}</span></li>"$'\n'
done
list_items+="      </ul>"$'\n'

cat > "$OUT" <<HTML
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CON Talks</title>
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700" rel="stylesheet" type="text/css">
  <style>
    /* Loose visual rhyme with https://centerforopenneuroscience.org/ */
    :root {
      --con-blue: #87AADE;
      --con-dark: #38434C;
      --con-text: #333;
      --con-muted: #777;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      font-weight: 400;
      color: var(--con-text);
      background: #fff;
      line-height: 1.5;
    }
    header {
      background: var(--con-blue);
      color: #fff;
      padding: 2em 1em;
    }
    header .inner { max-width: 960px; margin: 0 auto; }
    header h1 {
      margin: 0;
      font-weight: 600;
      font-size: 2em;
    }
    header h1 a { color: #fff; text-decoration: none; }
    header p {
      margin: 0.25em 0 0 0;
      font-weight: 300;
      font-size: 1.1em;
      opacity: 0.95;
    }
    main {
      max-width: 960px;
      margin: 0 auto;
      padding: 2em 1em 4em 1em;
    }
    main h2 {
      font-weight: 600;
      color: var(--con-dark);
      border-bottom: 2px solid var(--con-blue);
      padding-bottom: 0.25em;
      margin-top: 1.75em;
    }
    ul.talks {
      list-style: none;
      padding: 0;
      margin: 0.5em 0;
    }
    ul.talks li {
      padding: 0.5em 0;
      border-bottom: 1px solid #eee;
    }
    ul.talks a {
      color: var(--con-dark);
      text-decoration: none;
      font-weight: 600;
    }
    ul.talks a.alt { font-weight: 400; }
    ul.talks .kind {
      font-size: 0.75em;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #fff;
      background: var(--con-blue);
      border-radius: 3px;
      padding: 0.05em 0.4em;
      vertical-align: middle;
    }
    ul.talks a:hover { color: var(--con-blue); text-decoration: underline; }
    ul.talks .file {
      display: block;
      font-family: 'Source Code Pro', monospace;
      font-size: 0.85em;
      color: var(--con-muted);
      font-weight: 400;
    }
    footer {
      background: var(--con-dark);
      color: #fff;
      padding: 1.5em 1em;
      font-size: 0.9em;
    }
    footer .inner { max-width: 960px; margin: 0 auto; }
    footer a { color: var(--con-blue); }
  </style>
</head>
<body>
  <header>
    <div class="inner">
      <h1><a href="https://centerforopenneuroscience.org/">Center for Open Neuroscience</a></h1>
      <p>Talks, slide decks &amp; posters</p>
    </div>
  </header>
  <main>
    <p>Slides and posters from talks and workshops by CON people. This location is also a <a href="https://datasets.datalad.org/?dir=/centerforopenneuroscience/talks">DataLad dataset (git/git-annex repository)</a> so you can datalad clone it to get all the sources and materials.</p>
${list_items}  </main>
  <footer>
    <div class="inner">
      Auto-generated by <code>tools/create_index.sh</code>.
    </div>
  </footer>
</body>
</html>
HTML

echo "Wrote $OUT with ${listed} entries."
