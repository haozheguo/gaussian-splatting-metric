import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

def get_label(csv_path):
    filename = os.path.basename(csv_path)
    target_suffix = "_gaussians.csv"
    
    if filename.endswith(target_suffix):
        label = filename[:-len(target_suffix)]
    else:
        label = "curve1"
        
    return label
def plot_curve(csv_path):
    # Existence check
    if not os.path.exists(csv_path):
        print(f"Error: File '{csv_path}' not found.")
        return

    # Read data
    print(f"Reading data from {csv_path}...")
    try:
        df = pd.read_csv(csv_path)
    except Exception as e:
        print(f"Error: Could not read CSV. {e}")
        return

    # Validate required columns
    if 'iteration' not in df.columns or 'gaussian_count' not in df.columns:
        print("Error: CSV must contain 'iteration' and 'gaussian_count' columns.")
        return

    plt.style.use('seaborn-v0_8-muted') # or use 'ggplot'
    fig, ax = plt.subplots(figsize=(12, 7))

    # Draw the curve
    scene_name = os.path.basename(csv_path).split('_3dgs')[0]
    curve_label = get_label(csv_path)
    ax.plot(df['iteration'], df['gaussian_count'], 
            color='#1f77b4', linewidth=2, label=curve_label)
    ax.set_title(f'Gaussian Growth Curve', fontsize=16, pad=20)
    ax.set_xlabel('Iterations', fontsize=12)
    ax.set_ylabel('Gaussian Count', fontsize=12)
    
    # Format big numbers on y-axis
    ax.ticklabel_format(style='plain', axis='y')
    ax.get_yaxis().set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend(loc='upper left')

    output_png = csv_path.replace('.csv', '_curve.png')
    
    # Save image
    plt.tight_layout()
    plt.savefig(output_png, dpi=300)
    print(f"Successfully saved plot to: {output_png}")

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description="Plot Gaussian count curve from a 3DGS training CSV.")
    parser.add_argument("--csv_path", type=str, required=True, help="Path to the 3dgs_gaussians.csv file")
    
    args = parser.parse_args()

    plot_curve(args.csv_path)
