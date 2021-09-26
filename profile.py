import pandas as pd

# name of dataset to be imported here
movies = pd.read_csv('data/rotten_tomatoes_top_movies_2019-01-15.csv')


metadata = [
    'datatype',
    'number of items',
    'smallest string',
    'biggest string',
    'average string',
    'smallest number',
    'biggest number',
    'average number',
    'most common bool'
]

dtypes = {
    'object': 3,
    'float64': 1,
    'int64': 1,
    'bool': 2
}

rows = 9
cols = len(movies.columns)

result = pd.DataFrame(index=metadata, columns=range(cols))

i = 0
for column in movies:
    # data type
    result.at['datatype', i] = dtypes[str(movies[column].dtype)]
    # number of items
    result.at['number of items', i] = movies[column].count()

    if(movies[column].dtype == 'object'):
        # smalles string
        min = movies[column].map(lambda x: len(str(x))).min()
        result.at['smallest string', i] = min

        # biggest string
        max = movies[column].map(lambda x: len(str(x))).max()
        result.at['biggest string', i] = max

        # average string
        avg = movies[column].map(lambda x: len(str(x))).sum() / movies[column].count()
        result.at['average string', i] = avg

    if(movies[column].dtype == 'float64' or movies[column].dtype == 'int64'):

        # smallest number
        result.at['smallest number', i] = movies[column].min()

        # biggest number
        result.at['biggest number', i] = movies[column].max()

        # average number
        result.at['average number', i] = movies[column].mean()

    if(movies[column].dtype == 'bool'):

        # most common bool
        result.at['most common bool', i] = movies.mode(axis = 1)[i]

    i += 1

finalResult = pd.DataFrame(index=metadata, columns=[0])

for ind in result.index:
    if(ind == 'datatype' or ind == 'most common bool'):
        if len(result.loc[ind, :].mode()):
            finalResult.at[ind, 0] = result.loc[ind, :].mode()[0]
    else:
        finalResult.at[ind, 0] = result.loc[ind, :].mean()

# name of output file
finalResult.to_csv('trees.csv')
