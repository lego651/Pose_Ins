from utils.get_pearson import pearson

def get_top_k(M, m, k):
    dict = {}
    m.index = M.index # !这一步很重要，m和M的 index必须都是int[0: 70] 才能跑pearson()...
    ranks = []
    for col in M.columns:
        cor = pearson(M.loc[:, str(col)].astype("float64"), m.loc[:, 'n'].astype("float64"))
        # print(type(M.loc[2, str(col)]))
        # print(m.loc[2, '0'])
        # print(type(m.loc[2,str(0)]))
        # print("pearson get is:", cor)
        dict.update({ col: cor })

    sortedIndex = sorted(dict, key=dict.get, reverse=True)
    for index in sortedIndex:
        nKey = index
        nVal = dict.get(nKey)
        # ranks.update({nKey: nVal})
        ranks.append({nKey: nVal})

    return ranks[:k]
    # return dict
