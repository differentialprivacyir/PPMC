from internal.initialize_data import *
from client.client import *
from server.server import *

EPSILON = 1
RADNOM_SEED = 50

def main():
    # initialize
    dataset = read_dataset("dataset/Data2-coarse.dat")
    domains = attributes_domain("dataset/Data2-coarse.domain")

    # normalize to [-1,1]
    normalized_dataset = normalize_dataset(dataset, domains)

    # Client
    client_obj = Client(EPSILON, RADNOM_SEED)
    # Server
    server_obj = Server(domains)

    # loop on data
    retrieval_dataset = wheel_of_differential(server_obj, client_obj, normalized_dataset)

    # denormalizing
    # denormalized = denormalize_dataset(retrieval_dataset, domains)

    # evaulation
    print('MSE is', findMSE(normalized_dataset, retrieval_dataset))



def wheel_of_differential(server_obj, client_obj, normalized_dataset):
    print('Wheel of Differential ...')
    retrieval_dataset = []
    for data in normalized_dataset:
        new_eigenvector, new_avg = client_obj.send_perturbed_avg_eigenvector(data)
        retrieval_data = server_obj.received_avg_eigenvector(new_avg, new_eigenvector)
        retrieval_dataset.append(retrieval_data)

    return retrieval_dataset

if __name__ == "__main__":
    main()
