# Data Theme: Higher Education

## About

How has tuition changed for Canadian and international students, and how does Alberta compare with Canada overall?

This Datawrapper project explores average annual tuition across four student groups, two geographies, and 20 academic years from 2006/2007 through 2025/2026. Values are inflation-adjusted Canadian dollars according to the assignment brief; its inflation base year was not supplied.

The gallery preserves the five original charts from Manavpreet Singh's final submission. [Full submitted commentary](report.md) · [Dataset and preparation notes](Dataset/README.md)

## Visualization 1: Canadian undergraduate tuition over time

![Canadian undergraduate tuition in Alberta and Canada](Visualizations/Viz1.png)

**Design:** Two lines share a time axis so readers can compare trajectories and identify when the regions cross. Direct labels identify the series. The truncated vertical scale emphasizes differences, so absolute gaps should be read from the values rather than inferred from line separation.

**Finding:** In 2025/2026, Alberta's average was **$6,995**, compared with **$6,706** nationally: a **$289** difference.

## Visualization 2: International undergraduate tuition relationship

![International undergraduate tuition scatter plot](Visualizations/Viz2.png)

**Design:** Each point represents one academic year. Canada's tuition is on the horizontal axis and Alberta's on the vertical axis. This shows association and clusters, but the lack of year labels makes chronological interpretation harder.

**Finding:** Higher national tuition generally coincides with higher Alberta tuition. The 2025/2026 values were **$36,199** nationally and **$30,245** in Alberta, a **$5,954** gap. Association does not establish causation.

## Visualization 3: Tuition by student group in 2025/2026

![Tuition dot plot across four student groups](Visualizations/Viz3.png)

**Design:** Paired dots compare Alberta and Canada within each student group on one shared scale. This makes cross-group differences visible, although small domestic-tuition differences are less prominent beside international tuition.

**Finding:** Alberta's tuition was lower in three of four groups. International undergraduate tuition was the highest in both geographies; the international graduate gap was **$6,103**.

## Visualization 4: Alberta international undergraduate tuition

![Alberta international undergraduate tuition column chart](Visualizations/Viz4.png)

**Design:** Columns use a zero baseline to keep heights proportional to tuition amounts. Annual bars highlight changes and plateaus; a line chart would make longer-term comparisons easier to follow.

**Finding:** Tuition increased from **$16,376** in 2006/2007 to **$30,245** in 2025/2026, an increase of **84.7%** in the supplied constant-dollar series.

## Visualization 5: Percentage change by student group

![Percentage tuition change ranked horizontal bar chart](Visualizations/Viz5.png)

**Design:** Ranked horizontal bars compare percentage changes relative to each group's starting tuition. A shared zero separates increases from decreases. Endpoint comparisons summarize change but hide intermediate fluctuations.

**Finding:** International undergraduate tuition rose **108.5%** nationally and **84.7%** in Alberta. Canadian graduate tuition fell **17.2%** in Alberta and **1.1%** nationally.

## Data quality and reproducibility

The CSV has 160 unique geography/student-group/academic-year observations. Forty original international-graduate rows have inconsistent `Year` values. The prepared CSV derives `Year` from `School Year`, preserving tuition values; this assumption is documented rather than treated as an externally verified correction. The original charts have not been redrawn.

Run `python3 scripts/validate_data.py` from the repository root to verify preparation and endpoint calculations. Original Datawrapper URLs were not supplied, so the repository provides image exports rather than live embeds. Government of Canada attribution is retained; the exact source table and inflation base year remain unspecified.
