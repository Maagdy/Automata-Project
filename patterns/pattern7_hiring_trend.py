import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime

def analyze_hiring_trend_pattern(df):
    """
    Pattern: Analyze hiring trends over time
    Identifies: When most employees were hired, hiring patterns
    """
    print("\n" + "="*60)
    print("📅 PATTERN 7: HIRING TREND ANALYSIS")
    print("="*60)
    
    # Extract year and month
    df['HIRE_YEAR'] = df['HIRE_DATE'].dt.year
    df['HIRE_MONTH'] = df['HIRE_DATE'].dt.month
    
    # Hiring by year
    yearly_hires = df['HIRE_YEAR'].value_counts().sort_index()
    
    print("\nHiring by Year:")
    print(yearly_hires)
    
    peak_year = yearly_hires.idxmax()
    print(f"\n📈 Peak Hiring Year: {peak_year} ({yearly_hires.max()} employees)")
    
    # Recent hires (last 2 years)
    current_year = datetime.datetime.now().year
    recent_hires = df[df['HIRE_YEAR'] >= current_year - 2]
    print(f"\n🆕 Recent Hires (last 2 years): {len(recent_hires)}")
    
    # Visualize
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))
    
    # Hiring by year
    axes[0].plot(yearly_hires.index, yearly_hires.values, marker='o', 
                linewidth=2, markersize=8, color='teal')
    axes[0].fill_between(yearly_hires.index, yearly_hires.values, alpha=0.3, color='teal')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Number of Hires')
    axes[0].set_title('Hiring Trend by Year', fontsize=14, fontweight='bold')
    axes[0].grid(alpha=0.3)
    
    # Hiring by month (all time)
    monthly_hires = df['HIRE_MONTH'].value_counts().sort_index()
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    axes[1].bar(monthly_hires.index, monthly_hires.values, color='orange', alpha=0.7)
    axes[1].set_xticks(range(1, 13))
    axes[1].set_xticklabels(month_names)
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Number of Hires')
    axes[1].set_title('Hiring Pattern by Month (All Years)', fontsize=14, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('data/results/pattern7_hiring_trend.png', dpi=300, bbox_inches='tight')
    print("\n💾 Saved: data/results/pattern7_hiring_trend.png")
    plt.show()
    
    return yearly_hires

