'''
Compute another common metric used in binary classification - the area under the curve ("auc").
'''

# Import the necessary modules
import xgboost as xgb
from measuring_accuracy import params, churn_dmatrix

# Perform cross_validation: cv_results
cv_results = xgb.cv(
    dtrain=churn_dmatrix, 
    params=params, 
    nfold=3,
    num_boost_round=5, 
    metrics="auc", 
    as_pandas=True, 
    seed=123)

# Print cv_results
print(cv_results)

# Print the AUC
print((cv_results["test-auc-mean"]).iloc[-1])
