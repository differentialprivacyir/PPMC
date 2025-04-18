from sklearn.metrics import mean_squared_error

def findMSE(original_data, perturbed_data):
    """
    Mean squared error regression loss.

    Parameters:
        original_data : array-like of shape (n_samples,) or (n_samples, n_outputs) Ground truth (correct) target values.
        perturbed_data : array-like of shape (n_samples,) or (n_samples, n_outputs) Estimated target values.
    
    Returns:
        loss : float or ndarray of floats
    
    Examples:
        >>> from sklearn.metrics import mean_squared_error
        >>> y_true = [3, -0.5, 2, 7]
        >>> y_pred = [2.5, 0.0, 2, 8]
        >>> mean_squared_error(y_true, y_pred)
        0.375
        >>> y_true = [3, -0.5, 2, 7]
        >>> y_pred = [2.5, 0.0, 2, 8]
        >>> mean_squared_error(y_true, y_pred, squared=False)
        0.612...
        >>> y_true = [[0.5, 1],[-1, 1],[7, -6]]
        >>> y_pred = [[0, 2],[-1, 2],[8, -5]]
        >>> mean_squared_error(y_true, y_pred)
        0.708...
        >>> mean_squared_error(y_true, y_pred, squared=False)
        0.822...  
    """
    return mean_squared_error(original_data, perturbed_data)
