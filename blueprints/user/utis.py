from typing import ByteString, Dict


def decode_query_string(query_string: ByteString) -> Dict[str, str]:
    """
    Get the query string from url.
    
    Exemple:
    
    Get to the url /endpoint/something?key=value&key2=value2 and
    will return a dictionary like {key: value, key2: value2} being all the
    values as strings.
    """
    query_string = query_string.decode('ascii')
    
    return {params.split('=')[0]: params.split('=')[1] for params in query_string.split('&')}
