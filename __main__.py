"""A Python Pulumi program"""

from pulumi import ResourceOptions, ResourceHookBinding, get_project, get_stack, export
from components.stack_reference import StackReferenceUpdate, StackReferenceUpdateInputs
from hooks import hook_create, hook_update

stack_ref_value = "foo"

stack_ref_update = StackReferenceUpdate(
    name="stackref",
    args=StackReferenceUpdateInputs(
        value=stack_ref_value
    ),
    opts=ResourceOptions(
        hooks=ResourceHookBinding(
            after_create=[hook_create],
            after_update=[hook_update],
            # before_create=
            # before_delete=
            # before_update=
            # after_delete=
        )
    )
)

export("value", stack_ref_value)