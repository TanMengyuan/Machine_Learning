from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
import pandas as pd


seed_df = pd.read_csv(
    'https://raw.githubusercontent.com/vihar/unsupervised-learning-with-python/master/seeds-less-rows.csv'
)

print(seed_df)

varieties = list(seed_df.pop('grain_variety'))

samples = seed_df.values

mergings = linkage(samples, method='complete')

dendrogram(mergings,
           labels=varieties,
           leaf_rotation=90,
           leaf_font_size=6
           )

plt.show()