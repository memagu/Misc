import pandas as pd


def plot_data(dataframe: pd.DataFrame, save_path: Path, width: int = 1920, height: int = 1080) -> None:
    px = 1 / plt.rcParams["figure.dpi"]
    plt.rcParams["figure.figsize"] = [width * px, height * px]

    plt.title(
        f"The annual returns of the top {len(dataframe)} funds, picked according to their performance over the last 12 months.")
    plt.grid()
    # plt.axhline(0, color="black")
    # plt.axvline(0, color="black")
    plt.xlabel("Annual return % last X months (see legend)")
    plt.ylabel("Annual return % last 12 months")

    plt.scatter(dataframe["ReturnM36"], dataframe["ReturnM12"], label="36 months", marker=".", color="green")
    plt.scatter(dataframe["ReturnM60"], dataframe["ReturnM12"], label="60 months", marker=".", color="orange")
    plt.scatter(dataframe["ReturnM120"], dataframe["ReturnM12"], label="120 months", marker=".", color="red")

    plt.legend()

    # for i, row in dataframe.iterrows():
    #     plt.annotate(row["Isin"], (row["ReturnM36"], row["ReturnM12"]), fontsize=8)
    #     plt.annotate(row["Isin"], (row["ReturnM60"], row["ReturnM12"]), fontsize=8)
    #     plt.annotate(row["Isin"], (row["ReturnM120"], row["ReturnM12"]), fontsize=8)

    plt.savefig(save_path)