# Tuition dataset

The supplied coursework dataset contains 160 observations: 20 academic years (2006/2007 to 2025/2026), two geographies (Alberta and Canada), and four student groups. `VALUE` is average annual tuition in inflation-adjusted Canadian dollars, according to the assignment brief. The inflation base year and original government table identifier were not supplied; do not infer them.

- `tuition_original.csv`: unmodified supplied CSV, including its UTF-8 BOM and original metadata issues.
- `tuition_normalized.csv`: same rows and values, with `Year` derived from the starting year in `School Year`.

## Data-quality note

40 original rows have a `Year` that disagrees with `School Year`; these are the international-graduate rows in both geographies, including a `#N/A` value. The normalized copy changes only `Year`. It treats `School Year` as the academic-period key, an explicit preparation assumption rather than independently verified source correction. Tuition values are unchanged. The five original chart images are preserved; normalization does not claim to regenerate or correct those images.

## Fields

| Field | Meaning |
|---|---|
| Year | Academic starting year; normalized from School Year in the prepared copy |
| School Year | Academic year label |
| GEO | Alberta or Canada |
| Level of study | Canadian/international undergraduate/graduate category |
| VALUE | Average annual tuition, constant CAD as described in the brief |

Source attribution: Government of Canada, as identified by the supplied assignment and chart footers. No exact source table or new redistribution license is asserted.
