from sklearn.base import BaseEstimator, TransformerMixin
# All sklearn Transforms must have the `transform` and `fit` methods
class Arreglarkoi_score(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data=X.copy()
        if 'koi_pdisposition' in data.columns.values:
            data['koi_score'][data['koi_pdisposition']=='FALSE POSITIVE']=-1*X[X['koi_pdisposition']=='FALSE POSITIVE']['koi_score']     
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data
