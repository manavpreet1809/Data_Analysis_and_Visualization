# Data Analysis and Visualization

**Manavpreet Singh** · Data analysis and visual storytelling

A collection of coursework visualizations exploring higher education in Canada. The first project uses five Datawrapper chart types to compare inflation-adjusted tuition in Alberta and Canada across 20 academic years.

## Projects

| Project | Theme | Tools | Deliverables |
|---|---|---|---|
| [DataWrapper1](DataWrapper1/) | Higher education: tuition, 2006/2007 to 2025/2026 | Datawrapper; CSV; Python validation | Five original charts, design commentary, original and prepared data |

## Visualizations

All five original Datawrapper visualizations are shown below. [Full submitted commentary](DataWrapper1/report.md) and [dataset notes](DataWrapper1/Dataset/README.md) provide additional detail.

## Visualization 1: Canadian undergraduate tuition over time

![Canadian undergraduate tuition in Alberta and Canada](DataWrapper1/Visualizations/Viz1.png)

**Design:** Two lines share a time axis so readers can compare trajectories and identify when the regions cross. Direct labels identify the series. The truncated vertical scale emphasizes differences, so absolute gaps should be read from the values rather than inferred from line separation.

**Finding:** In 2025/2026, Alberta's average was **$6,995**, compared with **$6,706** nationally: a **$289** difference.

## Visualization 2: International undergraduate tuition relationship

![International undergraduate tuition scatter plot](DataWrapper1/Visualizations/Viz2.png)

**Design:** Each point represents one academic year. Canada's tuition is on the horizontal axis and Alberta's on the vertical axis. This shows association and clusters, but the lack of year labels makes chronological interpretation harder.

**Finding:** Higher national tuition generally coincides with higher Alberta tuition. The 2025/2026 values were **$36,199** nationally and **$30,245** in Alberta, a **$5,954** gap. Association does not establish causation.

## Visualization 3: Tuition by student group in 2025/2026

![Tuition dot plot across four student groups](DataWrapper1/Visualizations/Viz3.png)

**Design:** Paired dots compare Alberta and Canada within each student group on one shared scale. This makes cross-group differences visible, although small domestic-tuition differences are less prominent beside international tuition.

**Finding:** Alberta's tuition was lower in three of four groups. International undergraduate tuition was the highest in both geographies; the international graduate gap was **$6,103**.

## Visualization 4: Alberta international undergraduate tuition

![Alberta international undergraduate tuition column chart](DataWrapper1/Visualizations/Viz4.png)

**Design:** Columns use a zero baseline to keep heights proportional to tuition amounts. Annual bars highlight changes and plateaus; a line chart would make longer-term comparisons easier to follow.

**Finding:** Tuition increased from **$16,376** in 2006/2007 to **$30,245** in 2025/2026, an increase of **84.7%** in the supplied constant-dollar series.

## Visualization 5: Percentage change by student group

![Percentage tuition change ranked horizontal bar chart](DataWrapper1/Visualizations/Viz5.png)

**Design:** Ranked horizontal bars compare percentage changes relative to each group's starting tuition. A shared zero separates increases from decreases. Endpoint comparisons summarize change but hide intermediate fluctuations.

**Finding:** International undergraduate tuition rose **108.5%** nationally and **84.7%** in Alberta. Canadian graduate tuition fell **17.2%** in Alberta and **1.1%** nationally.

## Repository structure

```text
DataWrapper1/
  Dataset/          Original CSV, normalized CSV, and data-quality notes
  Visualizations/   Five charts extracted from the submitted report
  README.md         Chart gallery, rationale, and findings
  report.md         Submitted written commentary
scripts/
  validate_data.py  Reproducible dataset and finding checks
```

## Validation

Run with Python 3.10 or newer; no third-party packages are needed:

```sh
python3 scripts/validate_data.py
```

The script checks the dataset grain, preservation of tuition values, academic-year normalization, and three reported endpoint gaps, then prints percentage changes for all eight geography/student-group combinations. Original Datawrapper project links and editable project files were not supplied; these checks do not regenerate the chart images.

## Attribution and scope

The visualizations and written submission were supplied by Manavpreet Singh. The assignment identifies the data source as the Government of Canada and specifies constant dollars. The exact source table and inflation base year are not available in the supplied files. See [data-quality notes](DataWrapper1/Dataset/README.md) before reusing the data.

This repository publishes the portfolio material, not the assignment handout or the original PDF named with a student identifier. Reference screenshots guided the folder organization; the charts shown here come from the supplied final submission.
