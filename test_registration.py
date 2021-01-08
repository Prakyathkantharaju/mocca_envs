import gym
import json
from collections import defaultdict

_game_envs = defaultdict(set)

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError



for env in gym.envs.registry.all():
    # TODO: solve this with regexes
    env_type = env.entry_point.split(':')[0].split('.')[-1]
    [print(c) for c in env.id if 'mocca' in c]
    _game_envs[env_type].add(env.id)

with open('env_file.json', 'w') as f:
    # print(json.dumps(_game_envs,default = set_default, indent=4))
    json.dump(_game_envs,f,default = set_default)

