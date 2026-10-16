#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Center for Open Neuroscience
# SPDX-License-Identifier: Apache-2.0
"""Render all allocated iterations from saved assessments, without network access."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONDITIONS = [('baseline', 'Baseline'), ('discover-general', 'General'),
              ('discover-science', 'Science'), ('stamped-explicit', 'STAMPED')]
EVIDENCE = 'https://github.com/con/talks/blob/codex/stamped-example-poster/2026-usrse/stamped-ai-study/data/assessment-snapshot.json'


def main():
    data = json.loads((ROOT / 'data/assessment-snapshot.json').read_text())
    assert not data['warnings'], data['warnings']
    parts = ['<table class="outcome-table"><colgroup><col><col><col><col></colgroup>',
             '<thead><tr><th>Condition / runs</th><th>Science</th><th>Replay</th><th>STAMPED<br>met / partial / unmet</th></tr></thead><tbody>']
    for iteration in data['rounds']:
        number = iteration['iteration']
        revision = iteration.get('skills_commit')
        label = f'Iteration {number}' + (' · final evaluation' if iteration['final_untuned_evaluation'] else '')
        if revision:
            label += f' · <a href="https://github.com/con/skills/tree/{revision}">{revision[:7]}</a>'
        parts.append(f'<tr class="iteration"><th colspan="4">{label}</th></tr>')
        for condition, label in CONDITIONS:
            rows = sorted((r for r in data['rows'] if r['iteration'] == number and r['condition'] == condition), key=lambda r:r['replicate'])
            assert len(rows) == 3
            run_links, science, replay, counts = [], [], [], []
            for row in rows:
                rid = row['run'].split('-')[-1]
                target = row.get('result_url') or EVIDENCE
                run_links.append(f'<a href="{html.escape(target)}" title="{row["run"]}">{rid}</a>')
                primary = row['primary']
                if not primary or primary['status'] != 'completed':
                    science.append('—'); replay.append('—'); counts.append('—')
                    continue
                sc = primary['science']
                sci = {'supported':'S', 'qualified':'Q', 'not supported':'N', 'not checked':'—'}.get(sc['reported_adequacy'], '?')
                if sc['display_qualifier']:
                    sci += '*'
                source = data['sources'][sc['source_id']].get('public_url') or EVIDENCE
                science.append(f'<a href="{html.escape(source)}">{sci}</a>')
                rp = primary['replay']
                replay.append({'passed':'P', 'pass':'P', 'partial':'~', 'failed':'F', 'unavailable':'NA', 'invalid':'NA'}.get(rp['comparable_status'], '—') if rp else '—')
                ck = primary['checklist']
                val = ck['comparable_counts']
                counts.append('/'.join(str(val[k]) for k in ('met','partial','unmet')))
            # Three values in each cell map left-to-right onto the run IDs.
            parts.append('<tr><th class="condition-cell">'+label+'<span class="runs">'+' · '.join(run_links)+'</span></th>'+
                         ''.join('<td><span class="values">'+' · '.join(values)+'</span></td>' for values in (science,replay,counts))+'</tr>')
    parts.append('</tbody></table>')
    content = (ROOT/'index.html').read_text()
    start, tail = content.split('<!-- ARM_RESULTS_START -->',1)
    _, end = tail.split('<!-- ARM_RESULTS_END -->',1)
    (ROOT/'index.html').write_text(start+'<!-- ARM_RESULTS_START -->\n'+ '\n'.join(parts)+'\n<!-- ARM_RESULTS_END -->'+end)
    print(json.dumps({'allocated_runs':len(data['rows']), 'iterations':len(data['rounds']), 'completed_primary_judgments':sum(r['primary'] is not None and r['primary']['status']=='completed' for r in data['rows'])}))


if __name__ == '__main__':
    main()
