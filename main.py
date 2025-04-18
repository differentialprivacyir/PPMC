from internal.initialize_data import *
from client.client import *
from server.server import *

EPSILON = 10
RADNOM_SEED = 10

def main():
    # initialize
    dataset = read_dataset("dataset/Data2-coarse.dat")
    domains = attributes_domain("dataset/Data2-coarse.domain")

    # normalize to [-1,1]
    normalized_dataset = normalize_dataset(dataset, domains)

    # Client
    client_obj = Client(EPSILON, RADNOM_SEED)
    new_eigenvector, new_avg = client_obj.send_perturbed_avg_eigenvector(normalized_dataset[0])

    # Server
    server_obj = Server(domains)
    retrieval_data = server_obj.received_avg_eigenvector(new_avg, new_eigenvector)


    # denormalizing
    nor = []
    nor.append(retrieval_data)
    de = denormalize_dataset(nor, domains)

    print('original data:', dataset[0])
    print('retrieval data:', de[0])

    print('MSE is', findMSE(dataset[0], de[0]))


if __name__ == "__main__":
    main()
