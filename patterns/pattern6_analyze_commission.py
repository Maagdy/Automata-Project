import os
import matplotlib.pyplot as plt
import numpy as np


def analyze_commission_pattern(df):
    """
    Pattern: Analyze commission structure
    Identifies: Who gets commission and commission rates
    """
    print("\n" + "="*60)
    print("💰 PATTERN 6: COMMISSION ANALYSIS")
    print("="*60)
    
    has_commission = df[df['COMMISSION_PCT'].notna()].copy()
    no_commission = df[df['COMMISSION_PCT'].isna()].copy()
    
    print(f"\nEmployees with Commission: {len(has_commission)}")
    print(f"Employees without Commission: {len(no_commission)}")
    print(f"Commission Coverage: {len(has_commission)/len(df)*100:.1f}%")
    
    if len(has_commission) > 0:
        print(f"\nCommission Statistics:")
        print(f"  Average Rate: {has_commission['COMMISSION_PCT'].mean():.2%}")
        print(f"  Min Rate: {has_commission['COMMISSION_PCT'].min():.2%}")
        print(f"  Max Rate: {has_commission['COMMISSION_PCT'].max():.2%}")
        
        print("\nEmployees with Commission:")
        comm_display = has_commission[['FULL_NAME', 'JOB_ID', 'SALARY', 
                                       'COMMISSION_PCT']].sort_values('COMMISSION_PCT', ascending=False)
        print(comm_display.to_string(index=False))
        
        # Commission by job role
        comm_by_job = has_commission.groupby('JOB_ID')['COMMISSION_PCT'].agg(['mean', 'count'])
        print("\nCommission by Job Role:")
        print(comm_by_job)
        
        # Visualize
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        
        # Commission distribution
        axes[0].hist(has_commission['COMMISSION_PCT']*100, bins=10, 
                    color='purple', alpha=0.7, edgecolor='black')
        axes[0].set_xlabel('Commission Rate (%)')
        axes[0].set_ylabel('Frequency')
        axes[0].set_title('Commission Rate Distribution', fontsize=14, fontweight='bold')
        axes[0].grid(alpha=0.3)
        
        # Salary vs Commission
        axes[1].scatter(has_commission['SALARY'], has_commission['COMMISSION_PCT']*100,
                       s=100, alpha=0.6, color='purple')
        axes[1].set_xlabel('Salary ($)')
        axes[1].set_ylabel('Commission Rate (%)')
        axes[1].set_title('Salary vs Commission Rate', fontsize=14, fontweight='bold')
        axes[1].grid(alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('data/results/pattern6_commission.png', dpi=300, bbox_inches='tight')
        print("\n💾 Saved: data/results/pattern6_commission.png")
        plt.show()
    else:
        print("\n⚠️  No commission data available in dataset")
    
    return has_commission

