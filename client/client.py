from internal.haar_transform import *
from internal.normalizer import *
from internal.perturbations import *

class Client:
    def __init__(self, epsilon, random_seed):
        self.epsilon = epsilon
        np.random.seed(random_seed)
        random.seed(random_seed)
    
    def send_perturbed_avg_eigenvector(self, data):
        """
        Parameters:
            data (list): input row

        Returns:
            (list, float): new_eignevector, new_avg
        """

        # haar transform
        haar_transform_obj= HaarTransform()
        avg, eigenvector = haar_transform_obj.transnform(data)

        # perturbations
        new_eignevector = perturbation_eigenvector_GPM(eigenvector, self.epsilon)
        new_avg = perturbation_average_PDP(avg, self.epsilon, 0.3, 0.1)

        return new_eignevector, new_avg
