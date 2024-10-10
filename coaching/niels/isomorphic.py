from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Parent:
    def __init__(self, gender: int, children: list[Parent] = None) -> None:
        self.gender: int = gender
        self.children: list[Parent] = children or []

    def add_child(self, child) -> None:
        self.children.append(child)

    def encode_tree(self) -> int:
        hash_: int = 0
        stack: list[Parent] = [self]

        while stack:
            node: Parent = stack.pop()
            hash_ = hash_ * 3 + node.gender

            for child in sorted(node.children, key=lambda c: c.gender):
                stack.append(child)

        return hash_

    def is_isomorphic(self, other: Parent) -> bool:
        return self.encode_tree() == other.encode_tree()


t1: Parent = Parent(
    1,
    [
        Parent(
            1,
            [Parent(0), Parent(0), Parent(0)]
        ),
        Parent(
            2,
            [
                Parent(
                    1,
                    [Parent(0), Parent(0)]
                ),
                Parent(0),
                Parent(
                    1,
                    [Parent(0), Parent(0)]
                )
            ]
        )
    ]
)

t2: Parent = Parent(
    1,
    [
        Parent(
            2,
            [
                Parent(
                    1,
                    [Parent(0), Parent(0)]
                ),
                Parent(
                    1,
                    [Parent(0), Parent(0)]
                ),
                Parent(0)
            ]
        ),
        Parent(
            1,
            [Parent(0), Parent(0), Parent(0)]
        )
    ]
)

print(t1.is_isomorphic(t2))
