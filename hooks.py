from pulumi import ResourceHookArgs

def hook_create(args: ResourceHookArgs):
    print("Trigger updates to downstream stacks")
    return

def hook_update(args: ResourceHookArgs):
    # get esc environment and trigger updates
    if (
        args.old_inputs is not None and
        args.new_inputs is not None and
        args.old_inputs.get("value") != args.new_inputs.get("value")
    ):
        print("Trigger updates to downstream stacks")
    return