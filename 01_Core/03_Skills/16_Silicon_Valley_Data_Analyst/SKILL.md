---
name: silicon-valley-data-analyst
description: Advanced data analysis skill that transforms raw data into executive-level insights, strategic recommendations, and predictive models. Follows Silicon Valley best practices for data storytelling, cohort analysis, and actionable intelligence. Use when analyzing business metrics, user behavior, revenue trends, or any dataset that requires strategic interpretation.
author: sebas@thinkdifferent
version: 1.0.0
tags: [data-analysis, analytics, business-intelligence, metrics, insights, cohorts, predictive, executive-reporting]
triggers:
  - "analyze data"
  - "data analysis"
  - "analisis de datos"
  - "cohort analysis"
  - "user behavior"
  - "revenue metrics"
  - "business intelligence"
  - "generate insights"
  - "data storytelling"
  - "predictive analysis"
  - "executive summary"
  - "SILICON VALLEY"
  - "SV-analytics"
---

# Silicon Valley Data Analyst

## Esencia Original

> Original purpose of this skill. This section preserves WHY this skill exists.

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Presentar aggregate metrics sin segmentación
  - **Por qué**: Los promedios ocultan patrones importantes
  - **Solución**: Siempre segmentar por cohort, fuente, o comportamiento

- **[ERROR]**: No reportar statistical significance
  - **Por qué**: Sin p-values, no sabemos si la diferencia es real o ruido
  - **Solución**: Incluir p-value o confidence interval en cada comparación

- **[ERROR]**: Análisis sin recomendación de acción
  - **Por qué**: Insight sin acción es inútil
  - **Solución**: Terminar siempre con "we should do X"



> Level: **TOP TOP** — Executive-Grade Analytics

This skill transforms raw data into strategic insights that drive business decisions. It follows the same rigor used at leading tech companies: data-backed storytelling, cohort analysis, predictive modeling, and actionable recommendations.

---

## When to Use This Skill

- Analyzing CSV, Excel, or JSON datasets
- Understanding user behavior patterns
- Revenue, churn, or growth metrics analysis
- Cohort analysis and retention studies
- Building predictive models or forecasts
- Creating executive-level presentations
- A/B test results interpretation
- Any data-to-insights pipeline

---

## Core Philosophy

### 1. Data → Insight → Action

Raw data is worthless. Every analysis must answer:
- **What happened?** (Descriptive)
- **Why did it happen?** (Diagnostic)
- **What will happen?** (Predictive)
- **What should we do?** (Prescriptive)

### 2. Cohort > Aggregate

Aggregates lie. Cohorts reveal truth. Always segment by:
- Time (daily, weekly, monthly cohorts)
- Source (acquisition channel)
- Behavior (users who performed action X)
- Size (power users vs casual)

### 3. Storytelling > Tables

A table with 50 rows is useless. A chart with ONE insight is priceless.
- Lead with the insight
- Support with evidence
- Recommend action

### 4. Silicon Valley Standards

- **Sample size awareness**: Never trust n < 30
- **Statistical significance**: Always report p-values or confidence intervals
- **Segment or die**: Never present aggregate metrics without segmentation
- **Time context**: "Growth" means nothing without timeframe
- **Comparative baseline**: Every metric needs a comparison (vs last period, vs benchmark)

---

## Analysis Workflow

### Phase 1: Data Ingestion & Cleaning

```python
# Load data with type inference
import pandas as pd
import numpy as np

def load_data(path: str) -> pd.DataFrame:
    """Load and auto-detect data types."""
    if path.endswith('.csv'):
        df = pd.read_csv(path)
    elif path.endswith('.xlsx'):
        df = pd.read_excel(path)
    elif path.endswith('.json'):
        df = pd.read_json(path)
    else:
        raise ValueError(f"Unsupported format: {path}")
    
    # Auto-clean
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df
```

### Phase 2: Exploratory Analysis (The 5-Minute Drill)

```python
def quick_analysis(df: pd.DataFrame) -> dict:
    """Get quick stats for initial assessment."""
    return {
        "shape": df.shape,
        "columns": df.dtypes.to_dict(),
        "missing": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe().to_dict(),
        "categorical_counts": {col: df[col].nunique() 
                               for col in df.select_dtypes(include='object').columns}
    }
```

### Phase 3: Cohort Analysis

```python
def cohort_retention(df: pd.DataFrame, 
                     cohort_col: str, 
                     period_col: str,
                     user_col: str) -> pd.DataFrame:
    """
    Build retention cohort matrix.
    
    Args:
        df: DataFrame
        cohort_col: Column with cohort identifier (e.g., 'signup_date')
        period_col: Column with period (e.g., 'activity_date')
        user_col: Unique user identifier
    """
    # Create period buckets
    df['cohort_period'] = (pd.to_datetime(df[period_col]).dt.to_period('M') - 
                           pd.to_datetime(df[cohort_col]).dt.to_period('M')).apply(lambda x: x.n)
    
    # Group by cohort and period
    cohort_data = df.groupby(['cohort_period', user_col]).size().reset_index(name='activity')
    cohort_counts = cohort_data.groupby('cohort_period')[user_col].apply(lambda x: x.nunique()).unstack()
    
    # Calculate retention
    cohort_sizes = cohort_counts.iloc[:, 0]
    retention = cohort_counts.divide(cohort_sizes, axis=0) * 100
    
    return retention.round(2)
```

### Phase 4: Statistical Significance

```python
from scipy import stats

def significant_difference(group_a: pd.Series, 
                          group_b: pd.Series,
                          alpha: float = 0.05) -> dict:
    """Test if difference is statistically significant."""
    t_stat, p_value = stats.ttest_ind(group_a, group_b)
    
    return {
        "significant": p_value < alpha,
        "p_value": round(p_value, 4),
        "confidence": f"{(1-alpha)*100}%",
        "effect_size": abs(group_a.mean() - group_b.mean()) / group_a.std(),
        "interpretation": "Statistically significant" if p_value < alpha else "Not significant"
    }
```

### Phase 5: Predictive Modeling

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def predict_outcome(df: pd.DataFrame, 
                    target_col: str, 
                    feature_cols: list) -> dict:
    """Build predictive model for target outcome."""
    X = df[feature_cols].fillna(0)
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    return {
        "accuracy": model.score(X_test, y_test),
        "feature_importance": dict(zip(feature_cols, model.feature_importances_)),
        "classification_report": classification_report(y_test, predictions),
        "recommendation": "Model ready for production" if model.score(X_test, y_test) > 0.8 else "Need more data"
    }
```

---

## Output Templates

### Template 1: Executive Summary (The One-Pager)

```
## 📊 Executive Summary: [Project Name]

### TL;DR
[One sentence: What did we find and what should we do?]

### Key Metrics
| Metric | Current | vs Last Period | Target | Status |
|--------|---------|----------------|--------|--------|
| [Metric 1] | [Value] | [+X%] | [Target] | ✅/⚠️/❌ |
| [Metric 2] | [Value] | [+X%] | [Target] | ✅/⚠️/❌ |

### What Worked
- [Insight 1] — [Impact: $X or X%]
- [Insight 2] — [Impact: $X or X%]

### What Didn't Work
- [Insight 1] — [Impact: -X% or $-X]
- [Insight 2] — [Impact: -X% or $-X]

### Recommendations
1. **[Priority 1]**: [Action] → [Expected Impact]
2. **[Priority 2]**: [Action] → [Expected Impact]
3. **[Priority 3]**: [Action] → [Expected Impact]

### Next Steps
- [ ] [Action] — [Owner] — [Date]
- [ ] [Action] — [Owner] — [Date]
```

### Template 2: Cohort Analysis Report

```
## 👥 Cohort Analysis: [Behavior Under Study]

### Retention Curve
[Chart: X-axis = Periods, Y-axis = Retention %]

### Key Findings
- **Cohort Size**: [N] users
- **Best Performing Cohort**: [Month] — [X]% retention at Day 30
- **Worst Performing Cohort**: [Month] — [X]% retention at Day 30
- **Trend**: [Improving/Stable/Declining]

### Segmentation Insights
| Segment | Retention | Revenue/User | Notes |
|---------|-----------|--------------|-------|
| [Segment A] | 45% | $X | [Note] |
| [Segment B] | 32% | $X | [Note] |
| [Segment C] | 18% | $X | [Note] |

### Action Items
- [ ] Target [Segment] for [Campaign]
- [ ] Improve [Factor] for [Cohort]
```

### Template 3: A/B Test Results

```
## 🧪 A/B Test: [Experiment Name]

### Test Setup
- **Control**: [Description]
- **Variant**: [Description]
- **Duration**: [X] days
- **Sample Size**: [N] per variant
- **Statistical Confidence**: [X]%

### Results
| Metric | Control | Variant | Lift | p-value | Significant? |
|--------|---------|---------|------|---------|---------------|
| [Metric 1] | [X]% | [X]% | +[X]% | 0.0X | ✅ Yes |
| [Metric 2] | [X]% | [X]% | +[X]% | 0.XX | ❌ No |

### Recommendation
[Ship / Don't Ship / Need More Data]

### Follow-up Questions
- [ ] Why did [Metric] move?
- [ ] What about [Segment] users?
- [ ] Long-term impact?
```

---

## Best Practices

### 1. Always Start with Questions

Before touching data, ask:
- What decision does this analysis inform?
- Who will act on these insights?
- What would change their mind?

### 2. The 80/20 Rule

Spend 20% of time on data cleaning, 80% on insight extraction.
If data cleaning takes more, your data pipeline is broken.

### 3. Visualize Last, Not First

Don't start with charts. Start with:
1. Questions
2. Hypotheses
3. The ONE insight that matters
4. Then visualize to prove it

### 4. Segments Are Mandatory

NEVER present aggregate metrics without answering:
- "Does it differ by [segment]?"
- "Is this true for [cohort]?"

### 5. Time Intelligence

Every trend needs context:
- Seasonality (weekend vs weekday, holiday vs normal)
- Year-over-year comparison
- Recent vs historical average

### 6. Correlation ≠ Causation

Always ask:
- "Could there be a confounding variable?"
- "Is this correlation or causation?"
- "What would break this insight?"

### 7. Action-Oriented Output

If your analysis doesn't end with "we should do X", it's incomplete.

### 8. Reproducibility

Code should be clean enough that someone else can run it.
Add comments explaining the "why", not just the "what".

---

## Common Pitfalls

| Pitfall | Why It Fails | Fix |
|---------|--------------|-----|
| Aggregates only | Hides outliers, obscures patterns | Always segment |
| No baseline | "10% growth" means nothing | Compare to prior period |
| Ignoring sample size | n=5 is not data | Require n>30 minimum |
| No statistical test | "Looks different" isn't proof | Run t-test or chi-square |
| Analysis without action | Waste of time | End with recommendations |
| Overcomplicating | Decision paralysis | One insight > 50 tables |

---

## Tools & Libraries

### Python Stack (Recommended)

```bash
# Core
pandas numpy scipy sklearn

# Visualization
matplotlib seaborn plotly altair

# Advanced
lifelines      # Survival analysis
prophet        # Time series forecasting
statsmodels    # Statistical modeling
scikit-posthocs # Post-hoc tests

# Data Apps
streamlit      # Quick dashboards
gradio         # ML demos
```

### SQL Patterns

```sql
-- Cohort query
WITH cohorts AS (
    SELECT 
        DATE_TRUNC('month', created_at) AS cohort_month,
        user_id,
        MIN(DATE_TRUNC('month', event_date)) AS first_activity
    FROM events
    GROUP BY 1, 2
)
SELECT 
    cohort_month,
    DATE_TRUNC('month', first_activity) AS cohort_period,
    COUNT(DISTINCT user_id) AS users
FROM cohorts
GROUP BY 1, 2
ORDER BY 1, 2
```

---

## Example Prompts

### Example 1: Revenue Analysis
```
Analyze the revenue data in data/revenue.csv. 
Show me:
1. Monthly trend with YoY comparison
2. Top 20% customers contributing X% of revenue (Pareto)
3. Revenue by acquisition source
4. Predicted next quarter revenue
End with 3 actionable recommendations.
```

### Example 2: Churn Analysis
```
Build a churn analysis for data/users.csv.
Include:
1. Monthly cohort retention matrix
2. Top 5 indicators of churn (feature importance)
3. Churn rate by segment (plan type, source, activity level)
4. Predicted churners for next month
Give me an executive summary I can present to the CEO.
```

### Example 3: A/B Test
```
Analyze the A/B test results in data/ab_test.csv.
Calculate:
1. Statistical significance for each metric
2. Lift and confidence intervals
3. Segment performance (mobile vs desktop)
4. Recommended action with reasoning
```

---

## Quality Checklist

Before presenting any analysis:

- [ ] Did I answer "So What?" in the first sentence?
- [ ] Is every metric compared to something?
- [ ] Did I segment by at least one dimension?
- [ ] Is statistical significance reported?
- [ ] Are there clear recommendations?
- [ ] Would a CEO understand this in 30 seconds?
- [ ] Can someone reproduce this analysis from the code?

---

## Advanced Topics

### Survival Analysis

For time-to-event data (churn, lifetime, time to purchase):

```python
from lifelines import KaplanMeierFitter

kmf = KaplanMeierFitter()
kmf.fit(df['duration'], event_observed=df['churned'])
kmf.plot()
```

### Attribution Modeling

For understanding which channels drive conversions:

```python
# First-touch attribution
first_touch = df.groupby('first_channel')['converted'].mean()

# Last-touch attribution  
last_touch = df.groupby('last_channel')['converted'].mean()

# Linear attribution
linear = df.groupby('all_channels')['converted'].mean() / df['channels'].str.len()
```

### Anomaly Detection

For finding unexpected patterns:

```python
from sklearn.ensemble import IsolationForest

iso = IsolationForest(contamination=0.01)
df['anomaly'] = iso.fit_predict(df[numeric_features])
anomalies = df[df['anomaly'] == -1]
```

---

## Summary

This skill transforms you into a **Silicon Valley-grade data analyst**:

1. **Ask the right questions** before analyzing
2. **Segment or die** — aggregates lie
3. **Test significance** — intuition isn't enough
4. **Predict, don't just describe** — be forward-looking
5. **Recommend action** — insight without action is worthless
6. **Tell a story** — one insight > 50 tables

**Your job isn't to show data. It's to change behavior.**

---

*Skill Version: 1.0.0*
*Author: sebas@thinkdifferent*
*Framework: Anthropic Skill Creator v2.0*
*Level: TOP TOP — Executive Grade*

