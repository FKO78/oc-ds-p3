def similar_movies(movie_df, ttid, n): 
    res = {}  
    res['_input'] = {}
    res['_result'] = []
    try: 
        title = movie_df[movie_df.titleID == ttid].movie_title.values[0]
        nclust = movie_df[movie_df['titleID'] == ttid].cluster.fillna('').values[0]
        res['_input'] = { 'id' : ttid, 'title' : title}
        if nclust == '': 
            res['_result'] = { 'ERR' : 'Partitionnement incomplet'}
        else: 
            mask = (movie_df.cluster.values == movie_df[movie_df['titleID'] == ttid]['cluster'].values) & (movie_df.titleID != ttid) 
            n_films = movie_df[mask].cluster.value_counts().values[0]
            if n_films == 0 : 
                res['_result'] = {"WNG" : "Pas d'autre film similaire".format(title)} 
            else: 
                n_films = min(n, n_films) 
                res['_result'] = []
                for i, k in movie_df[mask][['titleID', 'movie_title', 'imdb_score']]\
                                    .sort_values(by=['imdb_score'], ascending=False).iloc[:n_films, :].iterrows(): 
                    res['_result'].append({ 'id' : k['titleID'], 'title' : k['movie_title']})
    except IndexError: 
        res['_result'] = {'ERR' : 'ID non trouvé en base'} 
        res['_input']['title'] = '' 
        res['_input']['id'] = ttid 
    return res 
    
def similar_movies2(movie_df, ttid, n, cosine): 
    res = {}  
    res['_input'] = {}
    res['_result'] = []
    try: 
        similar_movies =  list(enumerate(cosine.toarray()[movie_df[movie_df.titleID == ttid].index.values[0]]))
        title = movie_df[movie_df.titleID == ttid].movie_title.values[0]
        res['_input'] = { 'id' : ttid, 'title' : title}
        
        for i in sorted(similar_movies, key=lambda x:x[1], reverse=True)[1:n+1]: 
            res['_result'].append({ 'id' : movie_df[movie_df.index == i[0]].titleID.values[0], 'title' : movie_df[movie_df.index == i[0]].movie_title.values[0]})
    except IndexError: 
        res['_result'] = {'ERR' : 'ID non trouvé en base'} 
        res['_input']['title'] = '' 
        res['_input']['id'] = ttid 
    return res 