"""Validate preparation and reported endpoint findings using only Python's stdlib."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'DataWrapper1' / 'Dataset'
with (DATA / 'tuition_original.csv').open(encoding='utf-8-sig', newline='') as handle:
    original = list(csv.DictReader(handle))
with (DATA / 'tuition_normalized.csv').open(encoding='utf-8', newline='') as handle:
    prepared = list(csv.DictReader(handle))
assert len(original) == len(prepared) == 160
for before, after in zip(original, prepared):
    assert after == {**before, 'Year': before['School Year'][:4]}
    assert int(after['VALUE']) > 0
keys = [(row['School Year'], row['GEO'], row['Level of study']) for row in prepared]
assert len(set(keys)) == 160
assert len({row['School Year'] for row in prepared}) == 20
lookup = {(r['School Year'], r['GEO'], r['Level of study']): int(r['VALUE']) for r in prepared}
assert lookup['2025/2026', 'Alberta', 'Canadian undergraduate'] - lookup['2025/2026', 'Canada', 'Canadian undergraduate'] == 289
assert lookup['2025/2026', 'Canada', 'International undergraduate'] - lookup['2025/2026', 'Alberta', 'International undergraduate'] == 5954
assert lookup['2025/2026', 'Canada', 'International graduate'] - lookup['2025/2026', 'Alberta', 'International graduate'] == 6103
for region in ['Alberta', 'Canada']:
    for group in ['Canadian undergraduate', 'Canadian graduate', 'International undergraduate', 'International graduate']:
        first = lookup['2006/2007', region, group]
        last = lookup['2025/2026', region, group]
        print(f'{region}: {group}: {first:,} -> {last:,}; {(last / first - 1) * 100:+.1f}%')
print('PASS: 160 unique observations; values preserved; academic-year normalization and endpoint gaps verified.')
