# Churn Risk Flagging Solution

## Project Purpose
This project aims to identify accounts at risk of churn based on their weekly login activity. By analyzing trends in login behavior, the solution flags accounts as "AT RISK," "WATCH," "HEALTHY," or "INSUFFICIENT HISTORY," enabling proactive interventions to retain customers.

## Churn-Risk Rules
1. **At Risk**: Decline of 30% or more in login activity over the last 4 weeks compared to the previous 4 weeks.
2. **Watch**: Decline of 15% to less than 30% in login activity over the same period.
3. **Healthy**: Decline less than 15%, stable, or increasing login activity.
4. **Insufficient History**: Accounts with fewer than 8 weeks of login data.

The 4-week comparison window and thresholds are initial v1 assumptions and should be calibrated using real churn/renewal data in the future.

## Project File Structure
```
project-root/
├── data/
│   └── account_usage.json  # Input dataset with weekly login data for accounts
├── starter_kit/
│   ├── churn_utils.py      # Main Python script for churn-risk analysis
│   └── sample_accounts.json # Example JSON file (optional)
├── SOLUTION_DESIGN.md      # Detailed solution design document
└── README.md               # Project overview and instructions
```

## Requirements
- Python 3.6 or higher
- No additional dependencies are required (uses Python's built-in `json` module).

## How to Run the Solution
1. Open a terminal.
2. Navigate to the `starter_kit` directory:
   ```bash
   cd c:\Users\Admin\Downloads\case-study-3-churn-risk-flagging\starter_kit
   ```
3. Run the script:
   ```bash
   python churn_utils.py
   ```

## Example Results
```
Account A-01 (Northwind Traders):
  Status: AT RISK
  Trend: -60.75%
  Recent Avg: 10.5
  Previous Avg: 26.75
  Reason: Significant decline in usage (30% or more).

Account A-02 (Bluepeak Corp):
  Status: HEALTHY
  Trend: 4.82%
  Recent Avg: 21.75
  Previous Avg: 20.75
  Reason: Stable or increasing usage.

Account A-03 (Solace Digital):
  Status: HEALTHY
  Trend: 41.18%
  Recent Avg: 24.0
  Previous Avg: 17.0
  Reason: Stable or increasing usage.

Account A-04 (Harborview Inc):
  Status: WATCH
  Trend: -17.44%
  Recent Avg: 17.75
  Previous Avg: 21.5
  Reason: Moderate decline in usage (15% to less than 30%).

Account A-05 (Cascade Meridian):
  Status: AT RISK
  Trend: -73.20%
  Recent Avg: 6.5
  Previous Avg: 24.25
  Reason: Significant decline in usage (30% or more).

Account A-06 (Fresh Startup Co):
  Status: INSUFFICIENT HISTORY
  Trend: None%
  Recent Avg: None
  Previous Avg: None
  Reason: Not enough weekly login data (minimum 8 weeks required).

Account A-07 (Choppy Retail Co):
  Status: HEALTHY
  Trend: -5.06%
  Recent Avg: 18.75
  Previous Avg: 19.75
  Reason: Stable or increasing usage.

Account A-08 (New Signup LLC):
  Status: INSUFFICIENT HISTORY
  Trend: None%
  Recent Avg: None
  Previous Avg: None
  Reason: Not enough weekly login data (minimum 8 weeks required).
```

## Known Limitations
- **Thresholds and Windows**: The 4-week comparison and 30% risk threshold are initial v1 assumptions and not scientifically validated.
- **Data Quality**: Assumes accurate and complete weekly login data.
- **External Factors**: Does not account for seasonality, promotions, or other external influences.
- **Limited Features**: Only uses weekly login counts; additional features (e.g., plan tier, demographics) could improve predictions.

This solution provides a simple, interpretable starting point for churn-risk analysis. Future iterations can refine thresholds, incorporate more data, and leverage advanced models for improved accuracy.