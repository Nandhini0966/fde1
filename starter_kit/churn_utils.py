"""
Small utility module provided as an optional starting point for the
churn-risk flagging case study.

Feel free to use, modify, replace, or ignore this entirely -- it is not
guaranteed to be complete or bug-free.
"""
import json

def load_accounts(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("accounts", [])

def compute_trend_pct(weekly_logins, window=4):
    """
    Compare the average of the most recent `window` weeks against the
    average of the `window` weeks before that. Returns a percentage
    change (negative = declining usage).
    """
    if len(weekly_logins) < window * 2:
        return None, None, None  # Insufficient history

    recent = weekly_logins[-window:]
    previous = weekly_logins[-window * 2:-window]

    recent_avg = sum(recent) / len(recent)
    previous_avg = sum(previous) / len(previous)

    if previous_avg == 0:
        return None, recent_avg, previous_avg  # Avoid division by zero

    trend_pct = (recent_avg - previous_avg) / previous_avg * 100
    return trend_pct, recent_avg, previous_avg

def assess_risk(account, window=4, decline_threshold_pct=-30.0, watch_threshold_pct=-15.0):
    """Assess the churn risk of an account based on its weekly logins."""
    weekly_logins = account.get("weekly_logins", [])

    if len(weekly_logins) < window * 2:
        return {
            "account_id": account["account_id"],
            "account_name": account["account_name"],
            "status": "INSUFFICIENT HISTORY",
            "trend_pct": None,
            "recent_avg": None,
            "previous_avg": None,
            "reason": "Not enough weekly login data (minimum 8 weeks required)."
        }

    trend_pct, recent_avg, previous_avg = compute_trend_pct(weekly_logins, window)

    if trend_pct is None:
        return {
            "account_id": account["account_id"],
            "account_name": account["account_name"],
            "status": "INSUFFICIENT HISTORY",
            "trend_pct": None,
            "recent_avg": recent_avg,
            "previous_avg": previous_avg,
            "reason": "Zero usage or invalid data in previous period."
        }

    if trend_pct <= decline_threshold_pct:
        status = "AT RISK"
        reason = "Significant decline in usage (30% or more)."
    elif trend_pct <= watch_threshold_pct:
        status = "WATCH"
        reason = "Moderate decline in usage (15% to less than 30%)."
    else:
        status = "HEALTHY"
        reason = "Stable or increasing usage."

    return {
        "account_id": account["account_id"],
        "account_name": account["account_name"],
        "status": status,
        "trend_pct": trend_pct,
        "recent_avg": recent_avg,
        "previous_avg": previous_avg,
        "reason": reason
    }

if __name__ == "__main__":
    accounts = load_accounts("data/account_usage.json")
    results = []

    for account in accounts:
        result = assess_risk(account)
        results.append(result)

    for result in results:
        print(f"Account {result['account_id']} ({result['account_name']}):")
        print(f"  Status: {result['status']}")
        print(f"  Trend: {result['trend_pct']}%")
        print(f"  Recent Avg: {result['recent_avg']}")
        print(f"  Previous Avg: {result['previous_avg']}")
        print(f"  Reason: {result['reason']}")
        print()



def load_accounts(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("accounts", [])


def compute_trend_pct(weekly_logins, window=4):
    """
    Compare the average of the most recent `window` weeks against the
    average of the `window` weeks before that. Returns a percentage
    change (negative = declining usage).
    """
    recent = weekly_logins[-window:]
    previous = weekly_logins[-window * 2:-window]
    recent_avg = sum(recent) / len(recent)
    if len(previous) == 0:
        return 0.0
    previous_avg = sum(previous) / len(previous)
    if previous_avg == 0:
        return 0.0
    return (recent_avg - previous_avg) / previous_avg * 100


def flag_at_risk(account, window=4, decline_threshold_pct=-30.0):
    """Return True if the account's usage trend looks like a churn risk."""
    trend = compute_trend_pct(account["weekly_logins"], window)
    return trend <= decline_threshold_pct

if __name__ == "__main__":
    accounts = load_accounts("data/account_usage.json")
    for account in accounts:
        is_at_risk = flag_at_risk(account)
        print(f"Account {account['account_id']} ({account['account_name']}) at risk: {is_at_risk}")
