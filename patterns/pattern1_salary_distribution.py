import os
import matplotlib.pyplot as plt
import numpy as np

def analyze_salary_distribution(df):
    print("\n" + "="*60)
    print("📊 PATTERN 1: SALARY DISTRIBUTION ANALYSIS")
    print("="*60)
    
    stats = {
        'Mean': df['SALARY'].mean(),
        'Median': df['SALARY'].median(),
        'Std Dev': df['SALARY'].std(),
        'Min': df['SALARY'].min(),
        'Max': df['SALARY'].max(),
        'Range': df['SALARY'].max() - df['SALARY'].min()
    }

    for key, val in stats.items():
        print(f"{key:10s}: ${val:,.2f}")

    q1, q3 = df['SALARY'].quantile([0.25, 0.75])
    iqr = q3 - q1
    lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outliers = df[(df['SALARY'] < lower) | (df['SALARY'] > upper)]
    print(f"\n🔍 Outliers: {len(outliers)}")

    os.makedirs('data/results', exist_ok=True)
    plt.figure(figsize=(12,5))
    plt.hist(df['SALARY'], bins=20, color='skyblue', edgecolor='black')
    plt.axvline(stats['Mean'], color='r', linestyle='--', label='Mean')
    plt.axvline(stats['Median'], color='g', linestyle='--', label='Median')
    plt.title('Salary Distribution')
    plt.xlabel('Salary ($)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig('data/results/pattern1_salary_distribution.png', dpi=300)
    plt.show()

    return stats, outliers
