"""Prepare coursework data and reproduce chart summaries using Python's stdlib."""
import csv
import json
from collections import Counter, defaultdict
from datetime import datetime
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'Tableau1' / 'Dataset'
with (DATA / 'water_quality_original.csv').open(encoding='utf-8-sig', newline='') as handle:
    original = list(csv.DictReader(handle))
seen = set()
rows = []
duplicates = 0
excluded_ph = 0
for raw in original:
    row = {key: value.strip() for key, value in raw.items()}
    row['SITE_NAME'] = row['SITE_NAME'].rstrip(',').strip()
    row['DATE'] = datetime.strptime(row['DATE'], '%d/%m/%Y').date().isoformat()
    key = tuple(row.items())
    if key in seen:
        duplicates += 1
        continue
    seen.add(key)
    if row['VARIABLE'] == 'PH':
        excluded_ph += 1
        continue
    assert 2013 <= int(row['DATE'][:4]) <= 2016
    Decimal(row['VALUE'])
    rows.append(row)
with (DATA / 'water_quality_prepared.csv').open('w', newline='') as handle:
    writer = csv.DictWriter(handle, fieldnames=list(original[0]), lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
chloride = defaultdict(list)
oxygen = defaultdict(list)
nitrogen = []
guidelines = defaultdict(lambda: [0, 0])
for row in rows:
    value = Decimal(row['VALUE'])
    site = row['SITE_NAME']
    if row['VARIABLE'] == 'CHLORIDE DISSOLVED' and row['DATE'].startswith('2016'):
        chloride[site].append(value)
    if row['VARIABLE'] == 'OXYGEN DISSOLVED' and row['DATE'].startswith('2016'):
        oxygen[site].append(value)
    if row['VARIABLE'] == 'NITROGEN TOTAL' and site.startswith('SOUTH SASKATCHEWAN'):
        nitrogen.append(value)
    lower = row['LOWER_GUIDELINE_RECOMMENDATION']
    upper = row['UPPER_GUIDELINE_RECOMMENDATION']
    if lower or upper:
        outside = (bool(lower) and value < Decimal(lower)) or (bool(upper) and value > Decimal(upper))
        tally = guidelines[site, row['VARIABLE']]
        tally[0] += int(outside)
        tally[1] += 1
assert len(original) == 1001
assert len(nitrogen) == 41 and sum(value > 1 for value in nitrogen) == 18
assert len(chloride) == len(oxygen) == 4
assert all(len(values) == 12 for values in chloride.values())
assert all(len(values) == 12 for values in oxygen.values())
summary = {
    'raw_rows': len(original), 'duplicates_removed': duplicates, 'ph_rows_excluded': excluded_ph,
    'prepared_rows': len(rows), 'date_format': 'day/month/year in source, ISO dates in prepared data',
    'chloride_2016': {site: {'n': len(values), 'mean_mg_l': round(float(sum(values) / len(values)), 2)} for site, values in sorted(chloride.items())},
    'oxygen_2016': {site: {'n': len(values), 'minimum_mg_l': float(min(values)), 'below_supplied_6_5': sum(value < Decimal('6.5') for value in values)} for site, values in sorted(oxygen.items())},
    'nitrogen_hwy41': {'n': len(nitrogen), 'above_supplied_1_0': sum(value > 1 for value in nitrogen), 'percent': round(sum(value > 1 for value in nitrogen) / len(nitrogen) * 100, 2)},
    'guideline_comparisons': [{'site': site, 'variable': variable, 'outside': outside, 'n': n, 'percent': round(outside/n*100, 2)} for (site, variable), (outside, n) in sorted(guidelines.items())],
}
(DATA / 'validation_summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps({key: value for key, value in summary.items() if key != 'guideline_comparisons'}, indent=2))
