from typing_extensions import Literal

implementation: str
null: Literal[b""]

def from_bytes(octets, signed: bool = ...): ...
def to_bytes(value, signed: bool = ..., length: int = ...): ...
def bitLength(number): ...
