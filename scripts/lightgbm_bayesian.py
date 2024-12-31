from model_tuning_functions import lightgbm_pipeline, bayesian_optimization_tuning
import pandas as pd
from skopt.space import Integer, Real, Categorical

# Load datasets
X_train = pd.read_csv('data/X_train.csv')
y_train = pd.read_csv('data/y_train.csv')

# Bayesian Optimization parameter spaces
lightgbm_bayesian_param_space = {
    'classifier__max_depth': Integer(4, 10),
    'classifier__learning_rate': Real(0.01, 0.3, prior='log-uniform'),
    'classifier__n_estimators': Integer(100, 1000),
    'classifier__num_leaves': Integer(20, 150),
    'classifier__min_child_samples': Integer(10, 100),
    'classifier__subsample': Real(0.5, 1),
    'classifier__colsample_bytree': Real(0.5, 1),
    'classifier__reg_alpha': Real(0, 1),
    'classifier__reg_lambda': Real(0, 1),
    'classifier__scale_pos_weight': Categorical([1, 5, 10])
}

lightgbm_bayes = bayesian_optimization_tuning(lightgbm_pipeline, lightgbm_bayesian_param_space, X_train, y_train)

print(lightgbm_bayes)