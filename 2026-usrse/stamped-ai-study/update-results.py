#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Center for Open Neuroscience
# SPDX-License-Identifier: Apache-2.0
"""Render all allocated iterations from saved assessments, without network access."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONDITIONS = [('baseline', 'No supplied skills'), ('discover-general', 'Find useful skills'),
              ('discover-science', 'Find research skills'), ('stamped-explicit', 'Use STAMPED skills')]
EVIDENCE = 'https://github.com/con/talks/blob/codex/stamped-example-poster/2026-usrse/stamped-ai-study/data/assessment-snapshot.json'
SKILLS = 'https://github.com/con/skills/tree/codex/pr26-operational-environment/skills'


def run_link(row):
    target = row.get('result_url') or EVIDENCE
    return f'<a href="{html.escape(target)}" title="{row["run"]}">{row["run"].split("-")[-1]}</a>'


def outcome_cells(row, data):
    primary = row['primary']
    if not primary or primary['status'] != 'completed':
        return '<td>—</td>' * 3
    sc = primary['science']
    science = {'supported':'S', 'qualified':'Q', 'not supported':'N', 'unable to assess':'U', 'not checked':'U'}[sc['reported_adequacy']]
    if sc['display_qualifier']:
        science += '*'
    source = data['sources'][sc['source_id']].get('public_url') or EVIDENCE
    science = f'<a href="{html.escape(source)}">{science}</a>'
    rp = primary['replay']
    replay = {'met':'P', 'passed':'P', 'pass':'P', 'partial':'~', 'unmet':'F', 'failed':'F', 'unavailable':'NA', 'invalid':'NA', 'not-checked':'U', 'not checked':'U'}[rp['comparable_status']] if rp else '—'
    checklist = primary['checklist']
    counts = '/'.join(str(checklist['comparable_counts'][k]) for k in ('met','partial','unmet'))
    evidence = data['sources'][checklist['source_id']].get('public_url') or EVIDENCE
    counts = f'<a href="{html.escape(evidence)}">{counts}</a>'
    return ''.join(f'<td>{value}</td>' for value in (science, replay, counts))


def main():
    data = json.loads((ROOT / 'data/assessment-snapshot.json').read_text())
    assert not data['warnings'], data['warnings']
    parts = ['<table class="outcome-table"><colgroup><col><col><col><col><col></colgroup>',
             '<thead><tr><th>Instruction</th><th>Run</th><th>Science</th><th>Replay</th><th>STAMPED<br>met / partial / unmet</th></tr></thead><tbody>']
    for iteration in data['rounds']:
        number = iteration['iteration']
        revision = iteration.get('skills_commit')
        label = f'Iteration {number}' + (' · final evaluation' if iteration['final_untuned_evaluation'] else '')
        if revision:
            label += f' · <a href="{SKILLS}">skill revision {revision[:7]}</a>'
        parts.append(f'<tr class="iteration"><th colspan="5">{label}</th></tr>')
        iteration_started = any(r.get('result_url') for r in data['rows'] if r['iteration'] == number)
        for condition, label in CONDITIONS:
            rows = sorted((r for r in data['rows'] if r['iteration'] == number and r['condition'] == condition), key=lambda r:r['replicate'])
            assert len(rows) == 3
            if not iteration_started:
                # Reserved iterations expand to individual run rows when data arrive.
                parts.append(f'<tr class="reserved"><th class="condition-cell">{label}</th><td class="run-cell">'+
                             ' · '.join(run_link(row) for row in rows)+'</td><td>—</td><td>—</td><td>—</td></tr>')
                continue
            for index, row in enumerate(rows):
                condition_cell = f'<th class="condition-cell" rowspan="3">{label}</th>' if index == 0 else ''
                parts.append(f'<tr>{condition_cell}<th class="run-cell">{run_link(row)}</th>'+outcome_cells(row, data)+'</tr>')
    parts.append('</tbody></table>')
    content = (ROOT/'index.html').read_text()
    start, tail = content.split('<!-- ARM_RESULTS_START -->',1)
    _, end = tail.split('<!-- ARM_RESULTS_END -->',1)
    (ROOT/'index.html').write_text(start+'<!-- ARM_RESULTS_START -->\n'+ '\n'.join(parts)+'\n<!-- ARM_RESULTS_END -->'+end)
    print(json.dumps({'allocated_runs':len(data['rows']), 'iterations':len(data['rounds']), 'completed_primary_judgments':sum(r['primary'] is not None and r['primary']['status']=='completed' for r in data['rows'])}))


if __name__ == '__main__':
    main()
