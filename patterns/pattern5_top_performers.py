import os
import matplotlib.pyplot as plt
import numpy as np

def analyze_top_performers_pattern(df):
    """
    Pattern: Identify and analyze top earners
    Identifies: Top 10% earners and their characteristics
    """
    print("\n" + "="*60)
    print("🏆 PATTERN 5: TOP PERFORMERS ANALYSIS")
    print("="*60)
    
    # Top 10% threshold
    top_10_threshold = df['SALARY'].quantile(0.90)
    top_performers = df[df['SALARY'] >= top_10_threshold].copy()
    
    print(f"\nTop 10% Salary Threshold: ${top_10_threshold:,.2f}")
    print(f"Number of Top Performers: {len(top_performers)}")
    
    print("\nTop Performers:")
    top_display = top_performers[['FULL_NAME', 'JOB_ID', 'DEPARTMENT_ID', 
                                   'SALARY', 'TENURE_YEARS']].sort_values('SALARY', ascending=False)
    print(top_display.to_string(index=False))
    
    # Characteristics analysis
    print("\nTop Performers Characteristics:")
    print(f"  Average Salary: ${top_performers['SALARY'].mean():,.2f}")
    print(f"  Average Tenure: {top_performers['TENURE_YEARS'].mean():.2f} years")
    print(f"  Most Common Department: {top_performers['DEPARTMENT_ID'].mode().values[0]}")
    print(f"  Most Common Job: {top_performers['JOB_ID'].mode().values[0]}")
    
    # Visualize
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Top 10 earners
    top_10 = df.nlargest(10, 'SALARY')
    axes[0].barh(range(len(top_10)), top_10['SALARY'], color='gold', alpha=0.8)
    axes[0].set_yticks(range(len(top_10)))
    axes[0].set_yticklabels(top_10['FULL_NAME'].values, fontsize=9)
    axes[0].set_xlabel('Salary ($)')
    axes[0].set_title('Top 10 Earners', fontsize=14, fontweight='bold')
    axes[0].invert_yaxis()
    axes[0].grid(axis='x', alpha=0.3)
    
    # Department distribution of top performers
    dept_dist = top_performers['DEPARTMENT_ID'].value_counts()
    axes[1].pie(dept_dist.values, labels=dept_dist.index, autopct='%1.1f%%',
               startangle=90, colors=plt.cm.Set3.colors)
    axes[1].set_title('Top Performers by Department', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('data/results/pattern5_top_performers.png', dpi=300, bbox_inches='tight')
    print("\n💾 Saved: data/results/pattern5_top_performers.png")
    plt.show()
    
    return top_performers

