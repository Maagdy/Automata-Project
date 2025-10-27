import os
import matplotlib.pyplot as plt
import numpy as np

def analyze_department_salary_pattern(df):
    """
    Pattern: Compare salaries across departments
    Identifies: Which departments pay more/less
    """
    print("\n" + "="*60)
    print("🏢 PATTERN 2: DEPARTMENT SALARY COMPARISON")
    print("="*60)
    
    dept_analysis = df.groupby('DEPARTMENT_ID').agg({
        'SALARY': ['mean', 'median', 'min', 'max', 'count'],
        'EMPLOYEE_ID': 'count'
    }).round(2)
    
    dept_analysis.columns = ['Avg_Salary', 'Med_Salary', 'Min_Salary', 'Max_Salary', 'Count', 'Employees']
    dept_analysis = dept_analysis.sort_values('Avg_Salary', ascending=False)
    
    print("\nDepartment Salary Analysis:")
    print(dept_analysis)
    
    # Find highest and lowest paying departments
    highest_dept = dept_analysis['Avg_Salary'].idxmax()
    lowest_dept = dept_analysis['Avg_Salary'].idxmin()
    
    print(f"\n💰 Highest Paying Dept: {highest_dept} (${dept_analysis.loc[highest_dept, 'Avg_Salary']:,.2f})")
    print(f"💸 Lowest Paying Dept: {lowest_dept} (${dept_analysis.loc[lowest_dept, 'Avg_Salary']:,.2f})")
    
    # Visualize
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Bar chart - Average salary
    dept_data = dept_analysis.sort_values('Avg_Salary', ascending=True)
    axes[0].barh(dept_data.index.astype(str), dept_data['Avg_Salary'], color='coral', alpha=0.7)
    axes[0].set_xlabel('Average Salary ($)')
    axes[0].set_ylabel('Department ID')
    axes[0].set_title('Average Salary by Department', fontsize=14, fontweight='bold')
    axes[0].grid(axis='x', alpha=0.3)
    
    # Scatter - Employee count vs avg salary
    axes[1].scatter(dept_analysis['Count'], dept_analysis['Avg_Salary'], 
                   s=200, alpha=0.6, c=dept_analysis['Avg_Salary'], cmap='viridis')
    axes[1].set_xlabel('Number of Employees')
    axes[1].set_ylabel('Average Salary ($)')
    axes[1].set_title('Department Size vs Salary', fontsize=14, fontweight='bold')
    axes[1].grid(alpha=0.3)
    
    for idx, row in dept_analysis.iterrows():
        axes[1].annotate(f'Dept {idx}', 
                        (row['Count'], row['Avg_Salary']),
                        textcoords="offset points", xytext=(5,5), fontsize=8)
    
    plt.tight_layout()
    plt.savefig('data/results/pattern2_department_salary.png', dpi=300, bbox_inches='tight')
    print("\n💾 Saved: data/results/pattern2_department_salary.png")
    plt.show()
    
    return dept_analysis
