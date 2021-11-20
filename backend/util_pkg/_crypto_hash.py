import hashlib, json

def crypto_hash(*args):
    """
    Returns a sha-256 hash of the given data
    """
    # sorted to produces a hash based on a sorted order of data
    stringified_args = sorted(map(lambda data: json.dumps(data), args))
    
    joined_data = ''.join(stringified_args)
    
    return hashlib.sha256(joined_data.encode('utf8')).hexdigest()

def main():
    print(f"crypto_hash(1, 'two', [3]): {crypto_hash(1, 'two', [3])}")

if __name__ == '__main__':
    main()