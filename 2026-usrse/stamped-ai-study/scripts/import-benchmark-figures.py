#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Center for Open Neuroscience
# SPDX-License-Identifier: Apache-2.0
"""Import or verify display copies; scientific generation belongs to the benchmark."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = Path('experiments/narps-poster/figures/poster-figure-manifest.json')
BINDING = ROOT / 'figures/benchmark-source.json'
EXPECTED = {f'{name}.{ext}' for name in ('narps-group-map', 'narps-spatial-agreement', 'round-progression') for ext in ('svg', 'png')}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_path(root, relative):
    path = Path(relative)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError(f'Expected repository-relative path: {relative}')
    return root / path


def verify(root, entries):
    for entry in entries:
        path = checked_path(root, entry['path'])
        if digest(path) != entry['sha256'] or path.stat().st_size != entry['bytes']:
            raise ValueError(f'Figure source or display copy changed: {path}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--benchmark', type=Path, help='Import from a committed benchmark checkout; omit to verify existing display copies')
    args = parser.parse_args()
    if args.benchmark:
        benchmark = args.benchmark.resolve()
        raw = (benchmark / MANIFEST).read_bytes()
        source = json.loads(raw)
        if {Path(row['path']).name for row in source['figures']} != EXPECTED:
            raise ValueError('Benchmark must export the expected three SVG and three PNG figures')
        entries = source['figures'] + source['sources']
        verify(benchmark, entries)
        paths = [MANIFEST.as_posix(), *[row['path'] for row in entries]]
        subprocess.run(['git', '-C', str(benchmark), 'ls-files', '--error-unmatch', '--', *paths], check=True, stdout=subprocess.DEVNULL)
        subprocess.run(['git', '-C', str(benchmark), 'diff', '--quiet', 'HEAD', '--', *paths], check=True)
        revision = subprocess.check_output(['git', '-C', str(benchmark), 'rev-parse', 'HEAD'], text=True).strip()
        rows = []
        for row in source['figures']:
            destination = ROOT / 'figures' / Path(row['path']).name
            destination.parent.mkdir(parents=True, exist_ok=True)
            # Preserve existing annex symlinks when the exported bytes are unchanged.
            if not destination.exists() or digest(destination) != row['sha256']:
                if destination.is_symlink():
                    raise ValueError(f'Unlock annexed display copy before replacing it: {destination}')
                shutil.copyfile(benchmark / row['path'], destination)
            rows.append({**row, 'source_path': row['path'], 'path': destination.relative_to(ROOT).as_posix()})
        binding = {
            'schema_version': 1, 'repository': source['repository'],
            'branch': source['branch'], 'revision': revision,
            'source_manifest': {'path': MANIFEST.as_posix(), 'sha256': hashlib.sha256(raw).hexdigest()},
            'source_manifest_content': source, 'figures': rows,
            'scope': 'Verified display copies. Scientific code, inputs, environment and provenance are retained in the benchmark repository.'
        }
        BINDING.write_text(json.dumps(binding, indent=2) + '\n')
    binding = json.loads(BINDING.read_text())
    verify(ROOT, binding['figures'])
    print(json.dumps({'verified_display_copies': len(binding['figures']), 'benchmark_revision': binding['revision']}))


if __name__ == '__main__':
    main()
