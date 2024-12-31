"""bivariate_analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SlkTDqDIam9Pmw7HIC9-AjkrT-_9QtXm
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def distribution_age_analysis(df: pd.DataFrame) -> None:
    """
    Plots count and percentage stacked bar charts to analyze readmissions based on age.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 14))

    # First plot: Count plot
    sns.countplot(x='age', hue='readmission_in_30days', data=df, palette='coolwarm', ax=ax1)
    ax1.set_title('Readmission Depend on Age')
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, ['No', 'Yes'], title='Readmitted')
    xtick_labels = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
    ax1.set_xticklabels(xtick_labels, rotation=45)
    ax1.set_ylabel('Count')

    # Annotate bars with count
    for p in ax1.patches:
        height = int(p.get_height())
        if height > 0:
            ax1.annotate(f'{height}', (p.get_x() + p.get_width() / 2., height), ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    # Second plot: Stacked bar plot with percentages
    # Create a DataFrame with counts
    count_df = df.groupby(['age', 'readmission_in_30days']).size().unstack(fill_value=0)

    # Calculate percentages
    percent_df = count_df.div(count_df.sum(axis=1), axis=0) * 100

    # Plot stacked bar plot
    percent_df.plot(kind='bar', stacked=True, ax=ax2, color=["#b5caf3", "#ecbca7"])
    ax2.set_title('Percentage of Readmission Based on Age')
    ax2.set_ylabel('Percentage')
    ax2.set_xticklabels(xtick_labels, rotation=0)
    ax2.legend(title='Readmitted', labels=['No', 'Yes'], bbox_to_anchor=(1.05, 1), loc='upper left')

    # Annotate bars with percentages
    for p in ax2.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        if height > 0:
            ax2.annotate(f'{height:.1f}%', (x + width / 2., y + height / 2.), ha='center', va='center', color='black')

    plt.tight_layout()
    plt.savefig('Distribution of Readmission Based on Age.png')

def insulin_readmission_analysis(df: pd.DataFrame) -> None:
    """
    Plots count and percentage stacked bar charts to analyze readmissions based on insulin prescription and dosage changes.
    """
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 14))

    # First plot: Count plot
    sns.countplot(x='insulin', hue='readmission_in_30days', data=df, palette='coolwarm', ax=ax1)
    ax1.set_title('Readmission Depend on Insulin Prescribed and Change in Dosage')
    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles, ['No', 'Yes'], title='Readmitted')
    xtick_labels = ['No', 'Up', 'Steady', 'Down']
    ax1.set_xticklabels(xtick_labels, rotation=45)
    ax1.set_ylabel('Count')

    # Annotate bars with count
    for p in ax1.patches:
        height = int(p.get_height())
        if height > 0:
            ax1.annotate(f'{height}', (p.get_x() + p.get_width() / 2., height), ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    # Second plot: Stacked bar plot with percentages
    count_df = df.groupby(['insulin', 'readmission_in_30days']).size().unstack(fill_value=0)
    percent_df = count_df.div(count_df.sum(axis=1), axis=0) * 100
    percent_df.plot(kind='bar', stacked=True, ax=ax2, color=["#b5caf3", "#ecbca7"])
    ax2.set_title('Percentage of Readmission Based on Insulin Prescribed and Change in Dosage')
    ax2.set_ylabel('Percentage')
    ax2.set_xticklabels(xtick_labels, rotation=0)
    ax2.legend(title='Readmitted', labels=['No', 'Yes'], bbox_to_anchor=(1.05, 1), loc='upper left')

    # Annotate bars with percentages
    for p in ax2.patches:
        width, height = p.get_width(), p.get_height()
        x, y = p.get_xy()
        if height > 0:
            ax2.annotate(f'{height:.1f}%', (x + width / 2., y + height / 2.), ha='center', va='center', color='black')

    plt.tight_layout()
    plt.savefig('insulin_readmission_analysis.png')

def bivariate_analysis(df: pd.DataFrame) -> None:
    """
    Plots count and percentage stacked bar charts to analyze readmissions based on insulin prescription and dosage changes.
    """
    distribution_age_analysis(df)
    insulin_readmission_analysis(df)

if __name__ == "__main__":
    path = "data/transformed_diabetic_data.csv"
    df = pd.read_csv(path)

    # Perform analyses
    bivariate_analysis(df)