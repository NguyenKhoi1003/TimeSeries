# Project Timeseries

Time series forecasting project focused on US macroeconomic indicators and inflation. This workspace includes raw data, processed datasets, exploratory analysis notebooks, and rolling forecast model outputs.

## Contents

- `Data/`: raw series (CPIAUCSL, FEDFUNDS, INDPRO, UNRATE)
- `processed_macro_1990_2026.csv`: merged macro dataset
- `processed_macro_lagged_1990_2026.csv`: lagged feature dataset
- `eda_us_inflation_forecasting.ipynb`: exploratory analysis and summary stats
- `modeling_us_inflation_forecasting_rolling_diagnostics.ipynb`: modeling and diagnostics
- `model_outputs_rolling/`: model configs, forecasts, and diagnostics
- `check_missing_months.py`: helper to validate monthly continuity
- `Paper/` and `REPORT/`: writing artifacts

## Quick Start

1. Open the notebooks in VS Code and run cells top to bottom.
2. Use `check_missing_months.py` to verify monthly coverage if you update or replace any data files.

## Data Sources

CSV files in `Data/` and the root folder represent commonly used US macro series (CPIAUCSL, FEDFUNDS, INDPRO, UNRATE). If you refresh these series, keep column formats consistent with the existing files.

## Outputs

Rolling forecast results and diagnostics are stored in `model_outputs_rolling/`, including:

- `model_config.json`
- `model_forecasts.csv`
- `forecast_performance_results.csv`
- `residual_diagnostics.csv`

## Notes

- Notebooks may depend on the processed CSVs in the root folder.
- If you regenerate processed data, re-run the notebooks to update outputs.
