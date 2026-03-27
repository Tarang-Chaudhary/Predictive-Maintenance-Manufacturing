from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import rolling_window
import remove_constant
import matplotlib.pyplot as plt
# Create one feature vector per engine (aggregate sensor stats)
engine_profiles = rolling_window.train_df.groupby('unit_id')[remove_constant.selected_sensors].agg(
    ['mean', 'std', 'max', 'min']).reset_index()
engine_profiles.columns = ['_'.join(c).strip('_') for c in engine_profiles.columns]
engine_profiles = engine_profiles.fillna(0)

X_eng = engine_profiles.drop('unit_id', axis=1, errors='ignore')

# Find optimal k using elbow method
inertias = []
for k in range(2, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_eng)
    inertias.append(km.inertia_)

plt.figure(figsize=(6, 4))
plt.plot(range(2, 8), inertias, marker='o')
plt.title('Elbow Method — Optimal Clusters')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.tight_layout()
plt.savefig('elbow_plot.png', dpi=150)
plt.show()

# Apply KMeans (k=3)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
engine_profiles['cluster'] = kmeans.fit_predict(X_eng)

# PCA for 2D visualization
pca = PCA(n_components=2)
pca_coords = pca.fit_transform(X_eng)

plt.figure(figsize=(8, 5))
colors = ['steelblue', 'crimson', 'forestgreen']
for c in range(3):
    idx = engine_profiles['cluster'] == c
    plt.scatter(pca_coords[idx, 0], pca_coords[idx, 1],
                color=colors[c], label=f'Cluster {c}', s=70, alpha=0.8)
plt.title('Engine Degradation Clusters (PCA Projection)')
plt.xlabel('PC1'); plt.ylabel('PC2')
plt.legend(); plt.tight_layout()
plt.savefig('engine_clusters.png', dpi=150)
plt.show()