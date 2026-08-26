# Troubleshooting Notes

## Incorrect time-range views
Several early screenshots used Last 24 hours / Last 60 minutes while the investigation required a narrow five-minute window. These are preserved in `screenshots_all/` but excluded from curated public evidence.

## Baseline SPL error
The original baseline search attempted `round(avg(...),2)` directly inside `stats`. Splunk rejected that syntax.

Fix: calculate `avg(...)` in `stats`, then round the resulting fields with a later `eval`.

See:
- `06_baseline_original_failed_test.spl`
- `07_baseline_corrected.spl`

## Duplicate ML fields after `spath`
`dns_soc_ml` fields were already extracted. Running `spath` again caused duplicate multivalue display values.

Fix: remove `spath` and table the existing fields directly.

See:
- `12_ml_spath_duplicate_test.spl`
- `13_ml_clean_final.spl`

## Duplicate AI fields after `spath`
`dns_soc_ai` fields were already extracted. Running `spath` again produced duplicate multivalue display values.

Fix: remove `spath` and use `mvindex(...,0)` to normalize extracted multivalue fields in the clean table.

See:
- `15_ai_spath_duplicate_test.spl`
- `16_ai_summary_clean_final.spl`

## Public documentation recommendation
Keep troubleshooting/error screenshots in the full archive for reproducibility, but use only the curated evidence images for the GitHub case narrative.
