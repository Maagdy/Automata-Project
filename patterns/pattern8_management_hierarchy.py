import os
import matplotlib.pyplot as plt
import numpy as np


def analyze_management_hierarchy_pattern(df):
    """
    Pattern: Analyze management structure
    Identifies: Manager distribution, span of control
    """
    print("\n" + "="*60)
    print("👥 PATTERN 8: MANAGEMENT HIERARCHY")
    print("="*60)
    
    # Top level (no manager)
    top_level = df[df['MANAGER_ID'].isna()]
    print(f"\nTop-Level Employees (no manager): {len(top_level)}")
    
    if len(top_level) > 0:
        print("\nTop-Level Employees:")
        print(top_level[['FULL_NAME', 'JOB_ID', 'SALARY']].to_string(index=False))
    
    # Manager analysis
    if df['MANAGER_ID'].notna().any():
        manager_counts = df[df['MANAGER_ID'].notna()]['MANAGER_ID'].value_counts()
        
        print(f"\n📊 Total Unique Managers: {len(manager_counts)}")
        print(f"📈 Average Team Size: {manager_counts.mean():.1f} direct reports")
        
        print("\nManager Workload (Direct Reports):")
        for manager_id, count in manager_counts.head(10).items():
            manager_name = df[df['EMPLOYEE_ID'] == manager_id]['FULL_NAME'].values
            name = manager_name[0] if len(manager_name) > 0 else f"Manager {int(manager_id)}"
            print(f"  {name}: {count} reports")
        
        # Visualize
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Manager workload
        top_managers = manager_counts.head(10)
        axes[0].barh(range(len(top_managers)), top_managers.values, color='steelblue', alpha=0.7)
        axes[0].set_yticks(range(len(top_managers)))
        axes[0].set_yticklabels([f'Manager {int(mid)}' for mid in top_managers.index])
        axes[0].set_xlabel('Number of Direct Reports')
        axes[0].set_title('Top Managers by Team Size', fontsize=14, fontweight='bold')
        axes[0].invert_yaxis()
        axes[0].grid(axis='x', alpha=0.3)
        
        # Distribution of team sizes
        axes[1].hist(manager_counts.values, bins=10, color='lightblue', 
                    edgecolor='black', alpha=0.7)
        axes[1].axvline(manager_counts.mean(), color='red', linestyle='--', 
                       linewidth=2, label=f'Average: {manager_counts.mean():.1f}')
        axes[1].set_xlabel('Number of Direct Reports')
        axes[1].set_ylabel('Frequency')
        axes[1].set_title('Distribution of Team Sizes', fontsize=14, fontweight='bold')
        axes[1].legend()
        axes[1].grid(alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('data/results/pattern8_management.png', dpi=300, bbox_inches='tight')
        print("\n💾 Saved: data/results/pattern8_management.png")
        plt.show()
    else:
        print("\n⚠️  No manager data available")
    
    return manager_counts if df['MANAGER_ID'].notna().any() else None

