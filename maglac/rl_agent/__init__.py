from .maglac import MAGLACAgent

def make_agent(algo: str, **kwargs):
    if algo == 'MAGLAC':
        return MAGLACAgent(**kwargs)
    else:
        raise ValueError(f'Unknown algorithm: {algo}')
    


def get_train(algo: str):
    if 'GA2C' in algo:
        from .maglac import train as train
    
    else:
        raise ValueError(f'Unknown algorithm: {algo}')
    return train