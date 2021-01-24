def plot_embedding(data, label, title):
    x_min, x_max = np.min(data, 0), np.max(data, 0)
    data = (data - x_min) / (x_max - x_min)
    np.random.seed(0)

    length = data.shape[0]
    R = np.random.rand(np.max(label))
    G = np.random.rand(np.max(label))
    B = np.random.rand(np.max(label))

    fig = plt.figure()
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
