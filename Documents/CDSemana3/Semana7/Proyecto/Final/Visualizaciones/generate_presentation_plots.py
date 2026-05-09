import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib


def ensure_dir(d):
    os.makedirs(d, exist_ok=True)


def _presentation_target(df):
    if 'price' in df.columns:
        return 'price'
    if 'log_price' in df.columns:
        return 'log_price'
    return df.select_dtypes(include=[np.number]).columns[0]


def _select_relevant_numeric(df, target, max_features=5):
    numeric = df.select_dtypes(include=[np.number]).copy()
    if target not in numeric.columns:
        return [col for col in numeric.columns[:max_features] if col != 'id']

    numeric = numeric.drop(columns=['id'], errors='ignore')
    corr = numeric.corr(numeric_only=True)[target].abs().sort_values(ascending=False)
    features = [col for col in corr.index if col != target][:max_features]
    return [target] + features


def pairplot(df, cols, out_path):
    sns.pairplot(df[cols])
    plt.suptitle('Pairplot de variables relevantes', y=1.02)
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()


def corr_heatmap(df, cols, out_path):
    corr = df[cols].corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    plt.figure(figsize=(9,7))
    sns.heatmap(corr, mask=mask, annot=True, fmt='.2f', cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Matriz de correlación')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def target_dist(df, target, out_path):
    plt.figure(figsize=(6,4))
    sns.histplot(df[target], kde=True)
    plt.title(f'Distribución de {target}')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def coef_barplot(model_path, feature_names, out_path):
    pipe = joblib.load(model_path)
    try:
        coefs = pipe.named_steps['lr'].coef_
    except Exception:
        # fallback for direct estimator
        coefs = pipe.coef_
    coef_df = pd.DataFrame({'feature': feature_names, 'coef': coefs})
    coef_df['abs'] = coef_df['coef'].abs()
    coef_df = coef_df.sort_values('abs', ascending=False)
    coef_df = coef_df.head(15)

    plt.figure(figsize=(9,6))
    colors = np.where(coef_df['coef'] < 0, '#d62728', '#1f77b4')
    plt.axvline(0, color='black', linewidth=1)
    plt.barh(coef_df['feature'], coef_df['coef'], color=colors)
    plt.title('Coeficientes del modelo')
    plt.xlabel('Coeficiente')
    plt.ylabel('Característica')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def scatter_pred_actual(pred_csv, out_path):
    df = pd.read_csv(pred_csv)
    if {'price_true', 'price_pred'}.issubset(df.columns):
        true_col, pred_col, x_label, y_label, title = 'price_true', 'price_pred', 'Precio real', 'Precio estimado', 'Precio real vs precio estimado'
    elif {'log_price_true', 'log_price_pred'}.issubset(df.columns):
        true_col, pred_col, x_label, y_label, title = 'log_price_true', 'log_price_pred', 'log(precio) real', 'log(precio) estimado', 'log(precio) real vs log(precio) estimado'
    else:
        true_col, pred_col, x_label, y_label, title = 'y_test', 'y_pred', 'Real', 'Predicción', 'Predicción vs Real'

    plt.figure(figsize=(6,6))
    sns.scatterplot(x=true_col, y=pred_col, data=df, alpha=0.6)
    min_val = min(df[true_col].min(), df[pred_col].min())
    max_val = max(df[true_col].max(), df[pred_col].max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def residuals_plot(pred_csv, out_path):
    df = pd.read_csv(pred_csv)
    if {'price_true', 'price_pred'}.issubset(df.columns):
        df['residual'] = df['price_true'] - df['price_pred']
    elif {'log_price_true', 'log_price_pred'}.issubset(df.columns):
        df['residual'] = df['log_price_true'] - df['log_price_pred']
    else:
        df['residual'] = df['y_test'] - df['y_pred']
    plt.figure(figsize=(8,4))
    sns.histplot(df['residual'], kde=True)
    plt.title('Distribución de residuos')
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base, '..'))
    data_dir = os.path.join(project_root, 'Datos')
    vis_dir = os.path.join(base)
    ensure_dir(vis_dir)

    cleaned = os.path.join(data_dir, 'cleaned.csv')
    model_file = os.path.join(project_root, 'model.joblib')
    pred_csv = os.path.join(project_root, 'predictions.csv')

    if not os.path.exists(cleaned):
        raise FileNotFoundError(f'Cleaned data not found at {cleaned}')

    df = pd.read_csv(cleaned)

    target = _presentation_target(df)
    sel_pair = _select_relevant_numeric(df, target, max_features=5)

    pairplot(df, sel_pair, os.path.join(vis_dir, 'pairplot.png'))
    corr_cols = _select_relevant_numeric(df, target, max_features=8)
    corr_heatmap(df, corr_cols, os.path.join(vis_dir, 'correlation_heatmap.png'))

    if target in df.columns:
        target_dist(df, target, os.path.join(vis_dir, 'target_distribution.png'))

    if os.path.exists(model_file):
        pipe = joblib.load(model_file)
        try:
            model_features = pipe.named_steps['preprocessor'].get_feature_names_out().tolist()
        except Exception:
            model_features = []
        if model_features:
            coef_barplot(model_file, model_features, os.path.join(vis_dir, 'feature_coefficients.png'))

    if os.path.exists(pred_csv):
        scatter_pred_actual(pred_csv, os.path.join(vis_dir, 'predicted_vs_actual_present.png'))
        residuals_plot(pred_csv, os.path.join(vis_dir, 'residuals_present.png'))

    print('Gráficas de presentación creadas en', vis_dir)
