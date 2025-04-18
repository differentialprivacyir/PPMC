import numpy as np

def normalize(x, domain):
    max_domain = np.max(domain)
    min_domain = np.min(domain)
    return ((2*(x-min_domain)) / (max_domain-min_domain)) - 1


def denormalize(y, domain):
    max_domain = np.max(domain)
    min_domain = np.min(domain)
    return (((max_domain - min_domain) * (y + 1)) / 2) + min_domain

###
# dataset, domains are list of rows
# output also is list of rows
def normalize_dataset(dataset, domains):
    print("Normaizing dataset to [-1,1]")
    normalized_data = []
    for row in dataset:
        normalized_row = [normalize(element, domains[index]) for index, element in enumerate(row)]
        normalized_data.append(normalized_row)

    return normalized_data
