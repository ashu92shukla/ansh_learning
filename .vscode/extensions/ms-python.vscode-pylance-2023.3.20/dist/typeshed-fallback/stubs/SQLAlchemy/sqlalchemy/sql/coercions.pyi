from _typeshed import Incomplete
from typing import Any

from . import roles

elements: Any
lambdas: Any
schema: Any
selectable: Any
sqltypes: Any
traversals: Any

def expect(
    role,
    element,
    apply_propagate_attrs: Incomplete | None = ...,
    argname: Incomplete | None = ...,
    post_inspect: bool = ...,
    **kw,
): ...
def expect_as_key(role, element, **kw): ...
def expect_col_expression_collection(role, expressions) -> None: ...

class RoleImpl:
    name: Any
    def __init__(self, role_class) -> None: ...

class _Deannotate: ...
class _StringOnly: ...
class _ReturnsStringKey: ...
class _ColumnCoercions: ...
class _NoTextCoercion: ...
class _CoerceLiterals: ...
class LiteralValueImpl(RoleImpl): ...
class _SelectIsNotFrom: ...
class HasCacheKeyImpl(RoleImpl): ...
class ExecutableOptionImpl(RoleImpl): ...
class ExpressionElementImpl(_ColumnCoercions, RoleImpl): ...
class BinaryElementImpl(ExpressionElementImpl, RoleImpl): ...
class InElementImpl(RoleImpl): ...
class OnClauseImpl(_CoerceLiterals, _ColumnCoercions, RoleImpl): ...
class WhereHavingImpl(_CoerceLiterals, _ColumnCoercions, RoleImpl): ...
class StatementOptionImpl(_CoerceLiterals, RoleImpl): ...
class ColumnArgumentImpl(_NoTextCoercion, RoleImpl): ...
class ColumnArgumentOrKeyImpl(_ReturnsStringKey, RoleImpl): ...
class StrAsPlainColumnImpl(_CoerceLiterals, RoleImpl): ...
class ByOfImpl(_CoerceLiterals, _ColumnCoercions, RoleImpl, roles.ByOfRole): ...
class OrderByImpl(ByOfImpl, RoleImpl): ...
class GroupByImpl(ByOfImpl, RoleImpl): ...
class DMLColumnImpl(_ReturnsStringKey, RoleImpl): ...
class ConstExprImpl(RoleImpl): ...
class TruncatedLabelImpl(_StringOnly, RoleImpl): ...
class DDLExpressionImpl(_Deannotate, _CoerceLiterals, RoleImpl): ...
class DDLConstraintColumnImpl(_Deannotate, _ReturnsStringKey, RoleImpl): ...
class DDLReferredColumnImpl(DDLConstraintColumnImpl): ...
class LimitOffsetImpl(RoleImpl): ...
class LabeledColumnExprImpl(ExpressionElementImpl): ...
class ColumnsClauseImpl(_SelectIsNotFrom, _CoerceLiterals, RoleImpl): ...
class ReturnsRowsImpl(RoleImpl): ...
class StatementImpl(_CoerceLiterals, RoleImpl): ...
class SelectStatementImpl(_NoTextCoercion, RoleImpl): ...
class HasCTEImpl(ReturnsRowsImpl): ...
class IsCTEImpl(RoleImpl): ...
class JoinTargetImpl(RoleImpl): ...
class FromClauseImpl(_SelectIsNotFrom, _NoTextCoercion, RoleImpl): ...
class StrictFromClauseImpl(FromClauseImpl): ...
class AnonymizedFromClauseImpl(StrictFromClauseImpl): ...
class DMLTableImpl(_SelectIsNotFrom, _NoTextCoercion, RoleImpl): ...
class DMLSelectImpl(_NoTextCoercion, RoleImpl): ...
class CompoundElementImpl(_NoTextCoercion, RoleImpl): ...

cls: Any
name: Any
impl: Any