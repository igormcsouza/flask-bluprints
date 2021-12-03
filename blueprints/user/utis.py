from typing import ByteString, Dict


def decode_query_string(query_string: ByteString) -> Dict[str, str]:
    query_string = query_string.decode('ascii')
    
    return {params.split('=')[0]: params.split('=')[1] for params in query_string.split('&')}
