import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def analyze_tenure_salary_correlation(df):
    """
    Pattern: Relationship between tenure and salary
    Identifies: Does longer tenure correlate with higher pay?
    """
    print("\n" + "="*60)
    print("⏰ PATTERN 4: TENURE vs SALARY CORRELATION")
    print("="*60)
    
    # Calculate correlation
    correlation = df['TENURE_YEARS'].corr(df['SALARY'])
    
    print(f"\nCorrelation Coefficient: {correlation:.3f}")
    if correlation > 0.7:
        strength = "Strong Positive"
    elif correlation > 0.3:
        strength = "Moderate Positive"
    elif correlation > -0.3:
        strength = "Weak"
    elif correlation > -0.7:
        strength = "Moderate Negative"
    else:
        strength = "Strong Negative"
    
    print(f"Relationship: {strength}")
    
    # Tenure categories
    df['TENURE_CATEGORY'] = pd.cut(df['TENURE_YEARS'], 
                                   bins=[0, 5, 10, 15, 100],
                                   labels=['0-5 yrs', '5-10 yrs', '10-15 yrs', '15+ yrs'])
    
    tenure_salary = df.groupby('TENURE_CATEGORY')['SALARY'].agg(['mean', 'count']).round(2)
    
    print("\nAverage Salary by Tenure:")
    print(tenure_salary)
    
    # Visualize
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Scatter plot with trend line
    axes[0].scatter(df['TENURE_YEARS'], df['SALARY'], alpha=0.6, s=80, color='green')
    
    # Add trend line
    z = np.polyfit(df['TENURE_YEARS'], df['SALARY'], 1)
    p = np.poly1d(z)
    axes[0].plot(df['TENURE_YEARS'], p(df['TENURE_YEARS']), 
                "r--", linewidth=2, label=f'Trend (r={correlation:.2f})')
    
    axes[0].set_xlabel('Tenure (Years)')
    axes[0].set_ylabel('Salary ($)')
    axes[0].set_title('Salary vs Tenure Correlation', fontsize=14, fontweight='bold')
    axes[0].legend()
    axes[0].grid(alpha=0.3)
    
    # Box plot by tenure category
    tenure_data = [df[df['TENURE_CATEGORY'] == cat]['SALARY'].values 
                   for cat in ['0-5 yrs', '5-10 yrs', '10-15 yrs', '15+ yrs']]
    
    bp = axes[1].boxplot(tenure_data, labels=['0-5 yrs', '5-10 yrs', '10-15 yrs', '15+ yrs'],
                         patch_artist=True)
    for patch in bp['boxes']:
        patch.set_facecolor('lightgreen')
        patch.set_alpha(0.7)
    
    axes[1].set_xlabel('Tenure Category')
    axes[1].set_ylabel('Salary ($)')
    axes[1].set_title('Salary Distribution by Tenure', fontsize=14, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('data/results/pattern4_tenure_salary.png', dpi=300, bbox_inches='tight')
    print("\n💾 Saved: data/results/pattern4_tenure_salary.png")
    plt.show()
    
    return correlation, tenure_salary

