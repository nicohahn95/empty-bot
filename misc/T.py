import typing as ty

_base_types = ty.Union[str, int, float, bool]

class _Embed(ty.TypedDict):
    Color: ty.Dict[str, str]
    Emoji: ty.Dict[str, str]
    Icon: ty.Dict[str, str]

class Config(ty.TypedDict):
    Embed: _Embed

class _Embed(ty.TypedDict):
    Color: ty.Dict[str, str]
    Emoji: ty.Dict[str, str]
    Image: ty.Dict[str, str]

class _HostServer(ty.TypedDict):
    ID: int

class Config(ty.TypedDict):
    Embed: _Embed
    HostServer: _HostServer

