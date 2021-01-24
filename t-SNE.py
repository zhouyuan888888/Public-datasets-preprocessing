from sklearn.manifold import TSNE
import numpy as np

def plot_embedding(data, label, title):
    x_min, x_max = np.min(data, 0), np.max(data, 0)
    data = (data - x_min) / (x_max - x_min)
    np.random.seed(0)

    length = data.shape[0]
    R = np.random.rand(np.max(label))
    G = np.random.rand(np.max(label))
    B = np.random.rand(np.max(label))

    fig = plt.figure()
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    ax = plt.subplot(111)
    for i in range(length):
        if i < length*0.8:
            plt.text(data[i, 0], data[i, 1], str(label[i]),color=(R[label[i]-1], G[label[i]-1], B[label[i]-1]), fontdict={'weight': 'bold', 'size': 9})
        else:
            plt.text(data[i, 0], data[i, 1], str(label[i]), color="red", fontdict={'weight': 'bold', 'size': 9})
    #plt.xticks([])
    #plt.yticks([])
    plt.title(title)
    return fig

if __name__ == "__main__":
    tsne = TSNE(n_components=2, init="pca", random_state=0)
    feats = np.zeros(100, 256)
    feats_tsne = tsne.fit_transform(feats_tsne)
    labels = np.ones(100)
    fig = plot_embedding(feats_tsne, labels, 't-SNE')
    plt.savefig("/home/zhouyuan/Desktop/hand" + str(args.missing_rate).split(".")[-1])
