"""A Python Pulumi program"""

from pulumi import ResourceHookArgs, ResourceOptions, StackReference, ResourceHookBinding, get_project, get_stack, export
from components.stack_reference import StackReferenceUpdate, StackReferenceUpdateInputs
import requests

def hook_create(args: ResourceHookArgs):
    # get esc environment and trigger updates
    requests.get(f"https://xmcyber.com/update-stacks?env={args.new_inputs["esc_environment_name"]}")

    return

def hook_update(args: ResourceHookArgs):
    # get esc environment and trigger updates
    if(stack_ref_value has been updated):
        requests.get(f"https://xmcyber.com/update-stacks?env={args.new_inputs["esc_environment_name"]}")

    return

stack_ref_value = "foo"

stack_ref_update = StackReferenceUpdate(
    name="stackref",
    args=StackReferenceUpdateInputs(
        esc_environment_name="project/environment",
        stack_name=get_stack(),
        project_name=get_project(),
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