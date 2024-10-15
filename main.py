'''
coucou
'''

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        data = [list(map(int, line.strip().split(';'))) for line in lines]
    return data

def get_list_k(data, k):
    '''
    coucou
    '''
    return data[k]

def get_first(l):
    '''
    coucou
    '''
    return l[0]

def get_last(l):
    '''
    coucou
    '''
    return l[-1]

def get_max(l):
    '''
        coucou
    '''
    return max(l)

def get_min(l):
    '''
    coucou
    '''
    return min(l)

def get_sum(l):
    '''
    coucou
    '''
    return sum(l)

def main():
    '''
    coucou
    '''
    filename = 'listes.csv'
    data = read_data(filename)

    print("Data:", data)
    print("3rd list (index 2):", get_list_k(data, 2))
    print("First element of 3rd list:", get_first(get_list_k(data, 2)))
    print("Last element of 3rd list:", get_last(get_list_k(data, 2)))
    print("Max of 3rd list:", get_max(get_list_k(data, 2)))
    print("Min of 3rd list:", get_min(get_list_k(data, 2)))
    print("Sum of 3rd list:", get_sum(get_list_k(data, 2)))

if __name__ == "__main__":
    main()
