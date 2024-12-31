# -*- coding: utf-8 -*-
"""univariate_analysis

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13_ufwQ1jMpynHQbYHBkqd5kEt9YgtQYC
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def countplot(df: pd.DataFrame) -> None:
  """
  Generates count plots for all columns in the DataFrame.
  """

  cols = df.columns
  num_cols = len(cols)

  fig, axes = plt.subplots(6, 5, figsize=(30,30))
  fig.tight_layout(pad=5.0)

  for ax, feature in zip(axes.flatten(), cols):
      # Sort the value counts
      value_counts_sorted = df[feature].value_counts().sort_values(ascending=False)

      sns.countplot(x=feature, data=df, order=value_counts_sorted.index, ax=ax)
      ax.set_title(f'Countplot of {feature}')
      ax.set_xticklabels(ax.get_xticklabels())

      # Add value labels
      for i, count in enumerate(value_counts_sorted):
          ax.text(i, count, str(count), ha='center', va='bottom')

  for ax in axes[num_cols:]:
        fig.delaxes(ax)

  plt.savefig('Countplot_feature.png')

def boxplot(df: pd.DataFrame) -> None:
  """
  Generates box plots for all columns in the DataFrame.
  """

  cols = df.columns
  num_cols = len(cols)

  fig, axes = plt.subplots(6,5, figsize=(20, 15))
  fig.tight_layout(pad=5.0)

  for ax, feature in zip(axes.flatten(), cols):
      sns.boxplot(x=feature, data=df, ax=ax)
      ax.set_title(f'Boxplot of {feature}')

  for ax in axes[num_cols:]:
        fig.delaxes(ax)

  plt.savefig('Boxplot_feature.png')

def univariate_analysis(df: pd.DataFrame) -> None:
    """
    Master function that calls countplot and boxplot.
    """
    countplot(df)
    boxplot(df)

if __name__ == "__main__":
    path = "data/transformed_diabetic_data.csv"
    df = pd.read_csv(path)

    # Generate plots
    univariate_analysis(df)