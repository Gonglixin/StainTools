from sklearn.linear_model import Lasso

from staintools.utils.optical_density_conversion import convert_RGB_to_OD


def get_concentrations(I, stain_matrix, regularizer=0.01):
    """
    Estimate concentration matrix given an image and stain matrix.

    :param I:
    :param stain_matrix:
    :param regularizer:
    :return:
    """

    OD = convert_RGB_to_OD(I).reshape((-1, 3))

    lasso = Lasso(alpha=regularizer, positive=True)

    return lasso.fit(stain_matrix.T, OD.T)
