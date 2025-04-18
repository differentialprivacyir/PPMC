from internal.haar_transform import *
from internal.initialize_data import *
from internal.helper import *

def test_haar_transform():
    haar_transform_obj= HaarTransform()
    data = [9,7,3,5,8,4,5,7,1]
    print('input data:', data)
    avg, eigenvector = haar_transform_obj.transnform(data)
    retrieval_data = haar_transform_obj.inverse_transform(avg, eigenvector, len(data))
    print('retrieval data:', retrieval_data)


def main():
    # initialize
    dataset = read_dataset("dataset/Data2-coarse.dat")
    domains = attributes_domain("dataset/Data2-coarse.domain")

    # normalize to [-1,1]
    normalized_dataset = normalize_dataset(dataset, domains)

    test_haar_transform()

if __name__ == "__main__":
    main()
