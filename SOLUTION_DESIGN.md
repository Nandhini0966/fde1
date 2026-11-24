# SOLUTION DESIGN

## Problem Statement
Vantage Retail Systems aims to identify accounts at risk of churn based on their weekly login activity. The goal is to proactively address potential churn by flagging accounts with declining engagement trends, enabling targeted interventions to retain customers.

## Assumptions
- Weekly login data is a reasonable proxy for customer engagement.
- A minimum of 8 weeks of login history is required to calculate meaningful trends.
- A 4-week window provides a balance between recent activity and historical trends.
- A decline of 30% or more in login activity indicates a significant risk of churn.
- A decline between 15% and 30% suggests moderate risk, warranting monitoring.
- Accounts with fewer than 8 weeks of data cannot be reliably assessed and are marked as having "INSUFFICIENT HISTORY."

## Churn-Risk Approach
1. **Data Loading**: Weekly login data is loaded from a JSON file containing account information.
2. **Trend Calculation**:
   - The average login activity for the most recent 4 weeks is compared to the average of the 4 weeks prior.
   - The percentage change is calculated to determine the trend.
3. **Risk Assessment**:
   - Accounts with a decline of 30% or more are flagged as "AT RISK."
   - Accounts with a decline between 15% and 30% are flagged as "WATCH."
   - Accounts with a decline less than 15% or stable/increasing trends are flagged as "HEALTHY."
   - Accounts with fewer than 8 weeks of data are flagged as "INSUFFICIENT HISTORY."
4. **Output**: For each account, the program outputs the status, trend percentage, recent and previous averages, and a plain-English explanation.

## Why We Use 8 Weeks of History
- A minimum of 8 weeks ensures sufficient data to calculate trends over two 4-week windows.
- Shorter histories may lead to unreliable or misleading trend calculations.

## Why We Compare the Latest 4 Weeks vs Previous 4 Weeks
- A 4-week window balances recent activity with historical trends, providing actionable insights.
- Shorter windows may be too volatile, while longer windows may dilute recent changes.

## Why AT RISK is a 30%+ Decline
- A 30% decline represents a significant drop in engagement, strongly indicating potential churn.
- This threshold is a reasonable starting point for identifying high-risk accounts.

## Why WATCH is a 15-30% Decline
- A decline between 15% and 30% suggests moderate risk, warranting monitoring and potential intervention.
- This range captures accounts that may not yet be at high risk but show signs of declining engagement.

## How New Accounts with Insufficient History Are Handled
- Accounts with fewer than 8 weeks of login data are flagged as "INSUFFICIENT HISTORY."
- This ensures that only accounts with reliable data are assessed for churn risk.

## Key Trade-Offs and Limitations
- **Thresholds**: The 30% and 15% thresholds are reasonable assumptions but not scientifically validated.
- **Window Size**: The 4-week window is a balance between recency and stability but may not suit all accounts.
- **Data Quality**: The approach assumes accurate and complete weekly login data.
- **No Contextual Factors**: The model does not account for external factors (e.g., seasonality, promotions).

## Potential Improvements
- **More Historical Data**: Longer histories could enable more robust trend analysis and seasonality adjustments.
- **Actual Churn Labels**: Access to labeled churn data would allow for data-driven threshold optimization and predictive modeling.
- **Advanced Models**: Machine learning models could incorporate additional features (e.g., plan tier, demographics) for more accurate predictions.
- **Dynamic Thresholds**: Thresholds could be tailored to account-specific baselines and variability.

This solution provides a simple, interpretable starting point for churn-risk analysis. With more data and time, it can be refined into a more sophisticated and accurate system.