import os
import matplotlib.pyplot as plt
import numpy as np

def analyze_job_role_pattern(df):
    """
    Pattern: Salary distribution across job roles
    Identifies: Highest/lowest paying roles, role frequency
    """
    print("\n" + "="*60)
    print("💼 PATTERN 3: JOB ROLE ANALYSIS")
    print("="*60)
    
    job_analysis = df.groupby('JOB_ID').agg({
        'SALARY': ['mean', 'min', 'max', 'count'],
        'TENURE_YEARS': 'mean'
    }).round(2)
    
    job_analysis.columns = ['Avg_Salary', 'Min_Salary', 'Max_Salary', 'Count', 'Avg_Tenure']
    job_analysis = job_analysis.sort_values('Avg_Salary', ascending=False)
    
    print("\nJob Role Analysis:")
    print(job_analysis)
    
    print(f"\n🎯 Total Unique Roles: {len(job_analysis)}")
    print(f"👔 Highest Paying Role: {job_analysis.index[0]} (${job_analysis['Avg_Salary'].iloc[0]:,.2f})")
    print(f"📋 Most Common Role: {job_analysis['Count'].idxmax()} ({job_analysis['Count'].max()} employees)")
    
    # Visualize
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))
    
    # Top roles by salary
    top_roles = job_analysis.head(10)
    axes[0].barh(range(len(top_roles)), top_roles['Avg_Salary'], color='gold', alpha=0.7)
    axes[0].set_yticks(range(len(top_roles)))
    axes[0].set_yticklabels(top_roles.index)
    axes[0].set_xlabel('Average Salary ($)')
    axes[0].set_title('Top 10 Highest Paying Job Roles', fontsize=14, fontweight='bold')
    axes[0].invert_yaxis()
    axes[0].grid(axis='x', alpha=0.3)
    
    # Role frequency
    role_counts = job_analysis.sort_values('Count', ascending=False)
    axes[1].bar(range(len(role_counts)), role_counts['Count'], color='steelblue', alpha=0.7)
    axes[1].set_xticks(range(len(role_counts)))
    axes[1].set_xticklabels(role_counts.index, rotation=45, ha='right')
    axes[1].set_ylabel('Number of Employees')
    axes[1].set_title('Employee Distribution by Job Role', fontsize=14, fontweight='bold')
    axes[1].grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('data/results/pattern3_job_role.png', dpi=300, bbox_inches='tight')
    print("\n💾 Saved: data/results/pattern3_job_role.png")
    plt.show()
    
    return job_analysis

