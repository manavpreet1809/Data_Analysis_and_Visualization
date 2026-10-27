# River water quality dataset

Source attribution: Government of Canada, as identified by the supplied assignment. The exact source table, licensing reference, and guideline authority were not provided. The supplied guideline values are coursework comparison thresholds, not newly verified regulatory standards or a drinking-water safety assessment.

## Files

- `water_quality_original.csv`: unmodified supplied CSV (1,001 rows).
- `water_quality_prepared.csv`: 910 observations after preparation.
- `validation_summary.json`: reproducible counts, site means, and guideline comparison rates.

## Preparation

Run `python3 scripts/prepare_water_quality.py` from the repository root with Python 3.10 or newer; no third-party packages are needed. It regenerates the prepared CSV and validation summary.

1. Trim field whitespace and the trailing comma in the Highway 41 site name.
2. Parse dates as day/month/year and write ISO dates. Source values with a first component above 12 support this interpretation.
3. Remove 82 duplicate records after this normalization using all seven fields as the identity. Equal measurements on different dates remain distinct.
4. Exclude nine pH records, leaving ten variables across four sites from 2013 to 2016.
5. Preserve numeric values, units, and supplied guideline values. Compare with strict inequalities: below a lower threshold or above an upper threshold; equality is not outside.

`VALUE` units vary by variable (`MG/L` and `UG/L`); do not combine raw concentrations across different variables. Guideline percentages use the number of available unique observations per site/variable as their denominator. They do not describe the proportion of all time that a river was outside a threshold. Sampling frequencies differ across sites.

The preparation reproduces major reported summaries but does not recreate the original Tableau workbook. The original chart images remain unchanged. No editable Tableau workbook or Tableau Public URL was supplied.
