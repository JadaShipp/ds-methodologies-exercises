def prep_iris(iris_df):
    iris_df = iris_df.drop(columns=['species_id'])
    iris_df = iris_df.rename(columns={'species_name': 'species'})
    return iris_df


def prep_titanic(titanic_df):
    titanic_df = titanic_df.drop(columns=['deck'])
    return titanic_df