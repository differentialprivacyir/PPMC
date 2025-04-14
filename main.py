from haar_transform import *

def main():
    haar_transform_obj= HaarTransform()
    data = [9,7,3,5,8,4,5,7]
    print('input data:', data)
    avg, eigenvector = haar_transform_obj.transnform(data)
    retrieval_data = haar_transform_obj.inverse_transform(avg, eigenvector, len(data))
    print('retrieval data:', retrieval_data)

if __name__ == "__main__":
    main()
