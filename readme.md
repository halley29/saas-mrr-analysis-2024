# SaaS Technology Performance Analysis – MRR Growth (2024)

**Prepared by:** 23f1000780@ds.study.iitm.ac.in  
**Assisted by:** LLM (ChatGPT / Jules)

## 1. Business Context

Our SaaS technology company has observed **slowing MRR (Monthly Recurring Revenue) growth**  . 
The **industry benchmark** for healthy growth is **15%**, but internal performance has been below this target.

The goal of this analysis is to:

- Understand the **2024 quarterly MRR growth pattern**
- Compare performance against the **industry target of 15**
- Derive **data-driven recommendations** to close the gap
- Propose a clear direction: **expand into new market segments**

---

## 2. Data Used

**2024 Quarterly MRR Growth (%):**

- **Q1:** 5.97  
- **Q2:** 8.55  
- **Q3:** 7.72  
- **Q4:** 13.10  

**Industry target MRR growth:** 15%

**Average 2024 MRR growth:** **8.83**

> Note: The average value of **8.83** is computed from the quarterly data and is explicitly required for verification.

---

## 3. Analysis Approach

The analysis script (`analysis.py`) was generated with the help of an LLM (ChatGPT / Jules) and includes:

- Storage of quarterly MRR growth data
- Calculation of the **annual average MRR growth**
- Identification of quarters **below the industry benchmark**
- Creation of visualizations to support the data story

### Visualizations

1. **Line Chart: Quarterly MRR Growth vs Industry Target**

   File: `mrr_growth_vs_target.png`  
   - Plots Q1–Q4 MRR growth as a line
   - Shows a horizontal dashed line at **15%** (industry target)
   - Clearly illustrates that every quarter in 2024 is **below** the industry benchmark, though Q4 is closest.

2. **Bar Chart: MRR Growth by Quarter (Highlighting Q4)**

   File: `mrr_growth_bars.png`  
   - Shows each quarter’s growth as a bar
   - Highlights **Q4** as an improvement compared to Q1–Q3
   - Reinforces the narrative that we have **some positive momentum** but still a gap to close

---

## 4. Key Findings

1. **Persistent Underperformance vs Benchmark**

   - All four quarters (Q1–Q4) are **below the 15% industry target**.
   - The annual average MRR growth is **8.83**, which is:
     - **6.17 percentage points** below the target (15 − 8.83).
     - Roughly **41% lower** than the benchmark in relative terms.

2. **Weak Early-Year Performance**

   - **Q1 (5.97%)** and **Q3 (7.72%)** show particularly weak growth.
   - These low quarters drag down the **overall average**, even though Q4 improves.

3. **Q4 Recovery but Not Enough**

   - **Q4 (13.10%)** is a **positive signal** and indicates that some recent initiatives may be working.
   - However, even our best quarter is still **below** the 15% target, indicating that:
     - Internal optimizations alone may not be sufficient.
     - The current market segments may be reaching **saturation**.

---

## 5. Business Implications

1. **Revenue Forecast Risk**

   - If we continue at **8.83% average growth**, long-term revenue and profit projections will be **significantly below plan**.
   - This may limit our ability to:
     - Invest in R&D
     - Expand the sales team
     - Enter strategic partnerships

2. **Market Saturation in Existing Segments**

   - The gap between Q4 performance and the industry benchmark suggests:
     - Our current target customers and regions may be approaching **maturity or saturation**.
     - We may be competing heavily on price and discounts, which is not sustainable.

3. **Strategic Misalignment**

   - Continuing to focus only on existing segments risks:
     - Flat or declining growth
     - Increased churn if competitors offer better value propositions
   - Executives need to reconsider **where** and **how** growth will be generated.

---

## 6. Recommendations to Reach the Target of 15

Based on the data and trend, here are **specific recommendations**:

1. **Expand into New Market Segments (Primary Recommendation)**

   To close the gap between **8.83%** and the **15%** target, the company should **expand into new market segments**. This includes:

   - **New customer profiles**  
     - Mid-market or enterprise customers if we currently serve mostly SMBs  
     - Industry-specific verticals (e.g., healthcare, finance, education) where our product can be tailored

   - **New geographies**  
     - High-growth regions where SaaS adoption is increasing
     - Localized offerings (language, currency, compliance)

   - **New use-cases / products**  
     - Adjacent features or modules that can be upsold to existing customers  
     - Bundled offerings to increase ARPU (Average Revenue Per User)

2. **Strengthen Q1–Q3 Pipeline**

   - Use insights from Q4 (13.10% improvement) to:
     - Replicate successful campaigns earlier in the year
     - Launch demand-generation initiatives **before** Q1 to avoid a weak start
   - Align marketing and sales incentives toward **new segments**, not just existing ones.

3. **Data-Driven Experimentation**

   - Run **A/B tests** on:
     - Pricing models for new segments
     - Market positioning (e.g., “all-in-one suite” vs “lightweight plug-in”)
   - Measure:
     - Conversion rate
     - Customer acquisition cost (CAC)
     - Payback period

4. **Executive KPIs**

   To ensure focus, track:

   - Quarterly MRR growth vs **15% target**
   - Contribution of **new segments** to total new MRR
   - Expansion MRR vs churn MRR  
   This will show whether segment expansion is truly moving the needle.

---

## 7. Evidence of LLM Assistance

This repository (including `analysis.py` and this `README.md`) was created with assistance from an LLM (ChatGPT / Jules).  
Commit messages and/or comments reference this to provide transparency of AI involvement.

