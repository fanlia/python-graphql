import typing
import strawberry

from strawberry.scalars import JSON
from models.test import test

@strawberry.type
class Query:
    @strawberry.field
    def echo(json: JSON) -> JSON:
        return json

    @strawberry.field
    def echo_str(string: str) -> JSON:
        return string

    @strawberry.field
    def test() -> JSON:
        result = test()
        return result

schema = strawberry.Schema(query=Query)
