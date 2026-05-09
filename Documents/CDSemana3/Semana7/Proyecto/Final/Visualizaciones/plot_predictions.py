import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import argparse


def _choose_columns(df):
    if {'price_true', 'price_pred'}.issubset(df.columns):
        return 'price_true', 'price_pred', 'Precio real', 'Precio estimado', 'Predicción vs precio real'
    if {'log_price_true', 'log_price_pred'}.issubset(df.columns):
        return 'log_price_true', 'log_price_pred', 'log(price) real', 'log(price) estimado', 'Predicción vs log(precio)'
    if {'y_test', 'y_pred'}.issubset(df.columns):
        return 'y_test', 'y_pred', 'Real', 'Predicción', 'Predicción vs Real'
    raise ValueError('CSV must contain prediction columns.')


def plot_predictions(pred_csv, out_dir='.'):
    df = pd.read_csv(pred_csv)
    true_col, pred_col, x_label, y_label, title = _choose_columns(df)

    plt.figure(figsize=(7,7))
    sns.scatterplot(x=true_col, y=pred_col, data=df, alpha=0.6)
    min_val = min(df[true_col].min(), df[pred_col].min())
    max_val = max(df[true_col].max(), df[pred_col].max())
    plt.plot([min_val, max_val], [min_val, max_val], 'r--')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f'{out_dir}/predicted_vs_actual.png')
    plt.close()

    df['residual'] = df[true_col] - df[pred_col]
    plt.figure(figsize=(8,4))
    sns.histplot(df['residual'], kde=True)
    plt.title('Distribución de residuos')
    plt.tight_layout()
    plt.savefig(f'{out_dir}/residuals.png')
    plt.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot predictions')
    parser.add_argument('--pred', required=True, help='CSV with y_test and y_pred')
    parser.add_argument('--out', default='.', help='Output directory for plots')
    args = parser.parse_args()
    plot_predictions(args.pred, args.out)
