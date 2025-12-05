"""
SaaS MRR Growth Analysis - 2024
Generated with help from an LLM (ChatGPT / Jules).
"""

import numpy as np
import matplotlib.pyplot as plt

# Quarterly MRR growth data for 2024
quarters = ["Q1", "Q2", "Q3", "Q4"]
mrr_growth = [5.97, 8.55, 7.72, 13.1]
industry_target = 15

# Calculate average MRR growth
average_growth = np.mean(mrr_growth)
print(f"Average MRR growth (2024): {average_growth:.2f}")  # should be 8.83

# Simple text insights
below_target = [q for q, val in zip(quarters, mrr_growth) if val < industry_target]
print("\nQuarters below industry target of 15:")
print(", ".join(below_target))

# Visualization 1: Quarterly growth vs industry benchmark
plt.figure()
plt.plot(quarters, mrr_growth, marker="o", label="Company MRR Growth (2024)")
plt.axhline(industry_target, linestyle="--", label="Industry Target (15)")
plt.title("Quarterly MRR Growth vs Industry Target - 2024")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("mrr_growth_vs_target.png")  # saved to file
plt.close()

# Visualization 2: Bar chart highlighting Q4 improvement
plt.figure()
bars = plt.bar(quarters, mrr_growth)
plt.axhline(industry_target, linestyle="--", label="Industry Target (15)")

# Highlight Q4 as a positive signal
q4_index = quarters.index("Q4")
bars[q4_index].set_alpha(0.7)

plt.title("MRR Growth by Quarter (Highlighting Q4 Recovery)")
plt.xlabel("Quarter")
plt.ylabel("MRR Growth (%)")
plt.legend()
plt.grid(True, axis="y")
plt.tight_layout()
plt.savefig("mrr_growth_bars.png")
plt.close()

print("\nGenerated visualizations:")
print("- mrr_growth_vs_target.png")
print("- mrr_growth_bars.png")
