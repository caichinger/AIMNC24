"""
Utilities to simplify live coding.
"""
from itertools import product

from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


COLORS = {
    'TV': '#1b9e77',
    'radio': '#d95f02',
    'newspaper': '#7570b3',
}
XNAMES = ['TV', 'radio', 'newspaper']
YNAME = 'sales'


def plot_coefficients(coef, names):
    importance = pd.Series(coef, index=names, name='coef')
    fig, ax = plt.subplots()
    importance.plot.bar(ax=ax)
    ax.set_title('Coefficients')
    return fig


def create_model_explorer(df, model):

    def explore_budget_plan(tv_budget=140, radio_budget=20, newspaper_budget=30):
        planned_budget = pd.DataFrame([[tv_budget, radio_budget, newspaper_budget]], columns=XNAMES)
        
        sales_pred = model.predict(planned_budget)

        fig, axs = plt.subplots(figsize=(14, 6), ncols=3, sharey=True)
        for xname, ax in zip(XNAMES, axs):
            df.plot.scatter(ax=ax, x=xname, y=YNAME, color=COLORS[xname])

        for xname, ax in zip(XNAMES, axs):
            ax.scatter(planned_budget[xname][0], sales_pred, color='k', s=800, marker='+')
            # TODO add vlines and hlines
        return fig
        
    return explore_budget_plan  
 

def generate_valid_budget_allocations(total_budget):
    
    budget_options = range(0, total_budget + 1, 2)
    
    budget_allocations = []
    for budget_allocation in product(budget_options, budget_options, budget_options):
        if sum(budget_allocation) != total_budget:
            continue
        budget_allocations.append(budget_allocation)
    return pd.DataFrame(budget_allocations, columns=XNAMES)


def generate_budget_plans(reference, extra):
    budget_plans = reference[XNAMES].values + extra
    return budget_plans


def predict_sales_and_compare_plans(model, reference, budget_plans):
    sales_pred = model.predict(budget_plans)

    plan = budget_plans.copy()
    plan['predicted_sales'] = sales_pred
    
    absolute_difference = (plan - reference.values).sort_values('predicted_sales', ascending=False)

    relative_difference = ((plan - reference.values)/reference.values).sort_values('predicted_sales', ascending=False)

    return absolute_difference, relative_difference