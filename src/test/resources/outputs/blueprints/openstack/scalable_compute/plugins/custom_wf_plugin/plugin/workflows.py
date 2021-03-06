from cloudify.decorators import workflow
from cloudify.workflows import ctx
from cloudify.workflows import tasks as workflow_tasks
from utils import set_state_task
from utils import operation_task
from utils import link_tasks
from utils import CustomContext
from utils import generate_native_node_workflows
from utils import _get_all_nodes
from utils import _get_all_nodes_instances
from utils import _get_all_modified_node_instances
from utils import is_host_node
from workflow import WfStartEvent
from workflow import build_pre_event


# subworkflow 'install' for host 'NonScaledCompute'
def install_host_nonscaledcompute(ctx, graph, custom_context):
    custom_context.register_native_delegate_wf_step('NonScaledCompute', 'NonScaledCompute_install')
    generate_native_node_workflows(ctx, graph, custom_context, 'install')


# subworkflow 'install' for host 'AnotherScaleCompute'
def install_host_anotherscalecompute(ctx, graph, custom_context):
    custom_context.register_native_delegate_wf_step('AnotherScaleCompute', 'AnotherScaleCompute_install')
    generate_native_node_workflows(ctx, graph, custom_context, 'install')


# subworkflow 'install' for host 'Compute'
def install_host_compute(ctx, graph, custom_context):
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    set_state_task(ctx, graph, 'FileSystem', 'starting', 'FileSystem_starting', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'configuring', 'FileSystem_configuring', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'configured', 'FileSystem_configured', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'created', 'FileSystem_created', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'creating', 'FileSystem_creating', custom_context)
    operation_task(ctx, graph, 'FileSystem', 'cloudify.interfaces.lifecycle.configure', 'configure_FileSystem', custom_context)
    custom_context.register_native_delegate_wf_step('Compute', 'Compute_install')
    operation_task(ctx, graph, 'FileSystem', 'cloudify.interfaces.lifecycle.start', 'start_FileSystem', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'started', 'FileSystem_started', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'initial', 'FileSystem_initial', custom_context)
    operation_task(ctx, graph, 'FileSystem', 'cloudify.interfaces.lifecycle.create', 'create_FileSystem', custom_context)
    generate_native_node_workflows(ctx, graph, custom_context, 'install')
    link_tasks(graph, 'start_FileSystem', 'FileSystem_starting', custom_context)
    link_tasks(graph, 'configure_FileSystem', 'FileSystem_configuring', custom_context)
    link_tasks(graph, 'FileSystem_starting', 'FileSystem_configured', custom_context)
    link_tasks(graph, 'FileSystem_configuring', 'FileSystem_created', custom_context)
    link_tasks(graph, 'create_FileSystem', 'FileSystem_creating', custom_context)
    link_tasks(graph, 'FileSystem_configured', 'configure_FileSystem', custom_context)
    link_tasks(graph, 'FileSystem_initial', 'Compute_install', custom_context)
    link_tasks(graph, 'FileSystem_started', 'start_FileSystem', custom_context)
    link_tasks(graph, 'FileSystem_creating', 'FileSystem_initial', custom_context)
    link_tasks(graph, 'FileSystem_created', 'create_FileSystem', custom_context)


# subworkflow 'uninstall' for host 'NonScaledCompute'
def uninstall_host_nonscaledcompute(ctx, graph, custom_context):
    custom_context.register_native_delegate_wf_step('NonScaledCompute', 'NonScaledCompute_uninstall')
    generate_native_node_workflows(ctx, graph, custom_context, 'uninstall')


# subworkflow 'uninstall' for host 'AnotherScaleCompute'
def uninstall_host_anotherscalecompute(ctx, graph, custom_context):
    custom_context.register_native_delegate_wf_step('AnotherScaleCompute', 'AnotherScaleCompute_uninstall')
    generate_native_node_workflows(ctx, graph, custom_context, 'uninstall')


# subworkflow 'uninstall' for host 'Compute'
def uninstall_host_compute(ctx, graph, custom_context):
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    set_state_task(ctx, graph, 'FileSystem', 'deleting', 'FileSystem_deleting', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'deleted', 'FileSystem_deleted', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'stopped', 'FileSystem_stopped', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'stopping', 'FileSystem_stopping', custom_context)
    operation_task(ctx, graph, 'FileSystem', 'cloudify.interfaces.lifecycle.delete', 'delete_FileSystem', custom_context)
    operation_task(ctx, graph, 'FileSystem', 'cloudify.interfaces.lifecycle.stop', 'stop_FileSystem', custom_context)
    custom_context.register_native_delegate_wf_step('Compute', 'Compute_uninstall')
    generate_native_node_workflows(ctx, graph, custom_context, 'uninstall')
    link_tasks(graph, 'delete_FileSystem', 'FileSystem_deleting', custom_context)
    link_tasks(graph, 'Compute_uninstall', 'FileSystem_deleted', custom_context)
    link_tasks(graph, 'FileSystem_deleting', 'FileSystem_stopped', custom_context)
    link_tasks(graph, 'stop_FileSystem', 'FileSystem_stopping', custom_context)
    link_tasks(graph, 'FileSystem_deleted', 'delete_FileSystem', custom_context)
    link_tasks(graph, 'FileSystem_stopped', 'stop_FileSystem', custom_context)


def install_host(ctx, graph, custom_context, compute):
    options = {}
    options['NonScaledCompute'] = install_host_nonscaledcompute
    options['AnotherScaleCompute'] = install_host_anotherscalecompute
    options['Compute'] = install_host_compute
    options[compute](ctx, graph, custom_context)


def uninstall_host(ctx, graph, custom_context, compute):
    options = {}
    options['NonScaledCompute'] = uninstall_host_nonscaledcompute
    options['AnotherScaleCompute'] = uninstall_host_anotherscalecompute
    options['Compute'] = uninstall_host_compute
    options[compute](ctx, graph, custom_context)


@workflow
def a4c_install(**kwargs):
    graph = ctx.graph_mode()
    nodes = _get_all_nodes(ctx)
    instances = _get_all_nodes_instances(ctx)
    custom_context = CustomContext(ctx, instances, nodes)
    ctx.internal.send_workflow_event(event_type='a4c_workflow_started', message=build_pre_event(WfStartEvent('install')))
    _a4c_install(ctx, graph, custom_context)
    return graph.execute()


@workflow
def a4c_uninstall(**kwargs):
    graph = ctx.graph_mode()
    nodes = _get_all_nodes(ctx)
    instances = _get_all_nodes_instances(ctx)
    custom_context = CustomContext(ctx, instances, nodes)
    ctx.internal.send_workflow_event(event_type='a4c_workflow_started', message=build_pre_event(WfStartEvent('uninstall')))
    _a4c_uninstall(ctx, graph, custom_context)
    return graph.execute()


def _a4c_install(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.register_native_delegate_wf_step('BlockStorage', 'BlockStorage_install')
    set_state_task(ctx, graph, 'FileSystem', 'starting', 'FileSystem_starting', custom_context)
    custom_context.register_native_delegate_wf_step('NetPub', 'NetPub_install')
    set_state_task(ctx, graph, 'FileSystem', 'configuring', 'FileSystem_configuring', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'configured', 'FileSystem_configured', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'created', 'FileSystem_created', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'creating', 'FileSystem_creating', custom_context)
    operation_task(ctx, graph, 'FileSystem', 'cloudify.interfaces.lifecycle.configure', 'configure_FileSystem', custom_context)
    custom_context.register_native_delegate_wf_step('Compute', 'Compute_install')
    operation_task(ctx, graph, 'FileSystem', 'cloudify.interfaces.lifecycle.start', 'start_FileSystem', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'started', 'FileSystem_started', custom_context)
    custom_context.register_native_delegate_wf_step('AnotherScaleCompute', 'AnotherScaleCompute_install')
    set_state_task(ctx, graph, 'FileSystem', 'initial', 'FileSystem_initial', custom_context)
    custom_context.register_native_delegate_wf_step('BlockStorage2', 'BlockStorage2_install')
    custom_context.register_native_delegate_wf_step('NonScaledCompute', 'NonScaledCompute_install')
    operation_task(ctx, graph, 'FileSystem', 'cloudify.interfaces.lifecycle.create', 'create_FileSystem', custom_context)
    generate_native_node_workflows(ctx, graph, custom_context, 'install')
    link_tasks(graph, 'FileSystem_starting', 'FileSystem_configured', custom_context)
    link_tasks(graph, 'FileSystem_configuring', 'FileSystem_created', custom_context)
    link_tasks(graph, 'FileSystem_configured', 'configure_FileSystem', custom_context)
    link_tasks(graph, 'FileSystem_created', 'create_FileSystem', custom_context)
    link_tasks(graph, 'FileSystem_creating', 'FileSystem_initial', custom_context)
    link_tasks(graph, 'configure_FileSystem', 'FileSystem_configuring', custom_context)
    link_tasks(graph, 'start_FileSystem', 'FileSystem_starting', custom_context)
    link_tasks(graph, 'FileSystem_started', 'start_FileSystem', custom_context)
    link_tasks(graph, 'FileSystem_initial', 'BlockStorage_install', custom_context)
    link_tasks(graph, 'FileSystem_initial', 'BlockStorage2_install', custom_context)
    link_tasks(graph, 'FileSystem_initial', 'Compute_install', custom_context)
    link_tasks(graph, 'create_FileSystem', 'FileSystem_creating', custom_context)


@workflow
def a4c_scale(ctx, node_id, delta, scale_compute, **kwargs):
    scaled_node = ctx.get_node(node_id)
    if not scaled_node:
        raise ValueError("Node {0} doesn't exist".format(node_id))
    if not is_host_node(scaled_node):
        raise ValueError("Node {0} is not a host. This workflow can only scale hosts".format(node_id))
    if delta == 0:
        ctx.logger.info('delta parameter is 0, so no scaling will take place.')
        return

    curr_num_instances = scaled_node.number_of_instances
    planned_num_instances = curr_num_instances + delta
    if planned_num_instances < 1:
        raise ValueError('Provided delta: {0} is illegal. current number of'
                         'instances of node {1} is {2}'
                         .format(delta, node_id, curr_num_instances))

    modification = ctx.deployment.start_modification({
        scaled_node.id: {
            'instances': planned_num_instances
        }
    })
    ctx.logger.info(
        'Deployment modification started. [modification_id={0} : {1}]'.format(modification.id, dir(modification)))
    try:
        if delta > 0:
            ctx.logger.info('Scaling host {0} adding {1} instances'.format(node_id, delta))
            added_and_related = _get_all_nodes(modification.added)
            added = _get_all_modified_node_instances(added_and_related, 'added')
            graph = ctx.graph_mode()
            ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('scale', 'install')))
            custom_context = CustomContext(ctx, added, added_and_related)
            install_host(ctx, graph, custom_context, node_id)
            try:
                graph.execute()
            except:
                ctx.logger.error('Scale failed. Uninstalling node {0}'.format(node_id))
                graph = ctx.internal.task_graph
                for task in graph.tasks_iter():
                    graph.remove_task(task)
                try:
                    custom_context = CustomContext(ctx, added, added_and_related)
                    uninstall_host(ctx, graph, custom_context, node_id)
                    graph.execute()
                except:
                    ctx.logger.error('Node {0} uninstallation following scale failure has failed'.format(node_id))
                raise
        else:
            ctx.logger.info('Unscaling host {0} removing {1} instances'.format(node_id, delta))
            removed_and_related = _get_all_nodes(modification.removed)
            removed = _get_all_modified_node_instances(removed_and_related, 'removed')
            graph = ctx.graph_mode()
            ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('scale', 'uninstall')))
            custom_context = CustomContext(ctx, removed, removed_and_related)
            uninstall_host(ctx, graph, custom_context, node_id)
            try:
                graph.execute()
            except:
                ctx.logger.error('Unscale failed.')
                raise
    except:
        ctx.logger.warn('Rolling back deployment modification. [modification_id={0}]'.format(modification.id))
        try:
            modification.rollback()
        except:
            ctx.logger.warn('Deployment modification rollback failed. The '
                            'deployment model is most likely in some corrupted'
                            ' state.'
                            '[modification_id={0}]'.format(modification.id))
            raise
        raise
    else:
        try:
            modification.finish()
        except:
            ctx.logger.warn('Deployment modification finish failed. The '
                            'deployment model is most likely in some corrupted'
                            ' state.'
                            '[modification_id={0}]'.format(modification.id))
            raise


@workflow
def a4c_heal(
        ctx,
        node_instance_id,
        diagnose_value='Not provided',
        **kwargs):
    """Reinstalls the whole subgraph of the system topology

    The subgraph consists of all the nodes that are hosted in the
    failing node's compute and the compute itself.
    Additionally it unlinks and establishes appropriate relationships

    :param ctx: cloudify context
    :param node_id: failing node's id
    :param diagnose_value: diagnosed reason of failure
    """

    ctx.logger.info("Starting 'heal' workflow on {0}, Diagnosis: {1}"
                    .format(node_instance_id, diagnose_value))
    failing_node = ctx.get_node_instance(node_instance_id)
    host_instance_id = failing_node._node_instance.host_id
    failing_node_host = ctx.get_node_instance(host_instance_id)
    node_id = failing_node_host.node_id
    subgraph_node_instances = failing_node_host.get_contained_subgraph()
    added_and_related = _get_all_nodes(ctx)
    try:
      graph = ctx.graph_mode()
      ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                               message=build_pre_event(WfStartEvent('heal', 'uninstall')))
      custom_context = CustomContext(ctx, subgraph_node_instances, added_and_related)
      uninstall_host(ctx, graph, custom_context, node_id)
      graph.execute()
    except:
      ctx.logger.error('Uninstall while healing failed.')
    graph = ctx.internal.task_graph
    for task in graph.tasks_iter():
      graph.remove_task(task)
    ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('heal', 'install')))
    custom_context = CustomContext(ctx, subgraph_node_instances, added_and_related)
    install_host(ctx, graph, custom_context, node_id)
    graph.execute()


def _a4c_uninstall(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    custom_context.add_customized_wf_node('FileSystem')
    set_state_task(ctx, graph, 'FileSystem', 'deleting', 'FileSystem_deleting', custom_context)
    custom_context.register_native_delegate_wf_step('AnotherScaleCompute', 'AnotherScaleCompute_uninstall')
    custom_context.register_native_delegate_wf_step('BlockStorage', 'BlockStorage_uninstall')
    set_state_task(ctx, graph, 'FileSystem', 'deleted', 'FileSystem_deleted', custom_context)
    custom_context.register_native_delegate_wf_step('NonScaledCompute', 'NonScaledCompute_uninstall')
    set_state_task(ctx, graph, 'FileSystem', 'stopped', 'FileSystem_stopped', custom_context)
    set_state_task(ctx, graph, 'FileSystem', 'stopping', 'FileSystem_stopping', custom_context)
    operation_task(ctx, graph, 'FileSystem', 'cloudify.interfaces.lifecycle.delete', 'delete_FileSystem', custom_context)
    operation_task(ctx, graph, 'FileSystem', 'cloudify.interfaces.lifecycle.stop', 'stop_FileSystem', custom_context)
    custom_context.register_native_delegate_wf_step('Compute', 'Compute_uninstall')
    custom_context.register_native_delegate_wf_step('NetPub', 'NetPub_uninstall')
    custom_context.register_native_delegate_wf_step('BlockStorage2', 'BlockStorage2_uninstall')
    generate_native_node_workflows(ctx, graph, custom_context, 'uninstall')
    link_tasks(graph, 'FileSystem_deleting', 'FileSystem_stopped', custom_context)
    link_tasks(graph, 'BlockStorage_uninstall', 'FileSystem_deleted', custom_context)
    link_tasks(graph, 'FileSystem_deleted', 'delete_FileSystem', custom_context)
    link_tasks(graph, 'FileSystem_stopped', 'stop_FileSystem', custom_context)
    link_tasks(graph, 'delete_FileSystem', 'FileSystem_deleting', custom_context)
    link_tasks(graph, 'stop_FileSystem', 'FileSystem_stopping', custom_context)
    link_tasks(graph, 'Compute_uninstall', 'FileSystem_deleted', custom_context)
    link_tasks(graph, 'BlockStorage2_uninstall', 'FileSystem_deleted', custom_context)


@workflow
def a4c_scale(ctx, node_id, delta, scale_compute, **kwargs):
    scaled_node = ctx.get_node(node_id)
    if not scaled_node:
        raise ValueError("Node {0} doesn't exist".format(node_id))
    if not is_host_node(scaled_node):
        raise ValueError("Node {0} is not a host. This workflow can only scale hosts".format(node_id))
    if delta == 0:
        ctx.logger.info('delta parameter is 0, so no scaling will take place.')
        return

    curr_num_instances = scaled_node.number_of_instances
    planned_num_instances = curr_num_instances + delta
    if planned_num_instances < 1:
        raise ValueError('Provided delta: {0} is illegal. current number of'
                         'instances of node {1} is {2}'
                         .format(delta, node_id, curr_num_instances))

    modification = ctx.deployment.start_modification({
        scaled_node.id: {
            'instances': planned_num_instances
        }
    })
    ctx.logger.info(
        'Deployment modification started. [modification_id={0} : {1}]'.format(modification.id, dir(modification)))
    try:
        if delta > 0:
            ctx.logger.info('Scaling host {0} adding {1} instances'.format(node_id, delta))
            added_and_related = _get_all_nodes(modification.added)
            added = _get_all_modified_node_instances(added_and_related, 'added')
            graph = ctx.graph_mode()
            ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('scale', 'install')))
            custom_context = CustomContext(ctx, added, added_and_related)
            install_host(ctx, graph, custom_context, node_id)
            try:
                graph.execute()
            except:
                ctx.logger.error('Scale failed. Uninstalling node {0}'.format(node_id))
                graph = ctx.internal.task_graph
                for task in graph.tasks_iter():
                    graph.remove_task(task)
                try:
                    custom_context = CustomContext(ctx, added, added_and_related)
                    uninstall_host(ctx, graph, custom_context, node_id)
                    graph.execute()
                except:
                    ctx.logger.error('Node {0} uninstallation following scale failure has failed'.format(node_id))
                raise
        else:
            ctx.logger.info('Unscaling host {0} removing {1} instances'.format(node_id, delta))
            removed_and_related = _get_all_nodes(modification.removed)
            removed = _get_all_modified_node_instances(removed_and_related, 'removed')
            graph = ctx.graph_mode()
            ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('scale', 'uninstall')))
            custom_context = CustomContext(ctx, removed, removed_and_related)
            uninstall_host(ctx, graph, custom_context, node_id)
            try:
                graph.execute()
            except:
                ctx.logger.error('Unscale failed.')
                raise
    except:
        ctx.logger.warn('Rolling back deployment modification. [modification_id={0}]'.format(modification.id))
        try:
            modification.rollback()
        except:
            ctx.logger.warn('Deployment modification rollback failed. The '
                            'deployment model is most likely in some corrupted'
                            ' state.'
                            '[modification_id={0}]'.format(modification.id))
            raise
        raise
    else:
        try:
            modification.finish()
        except:
            ctx.logger.warn('Deployment modification finish failed. The '
                            'deployment model is most likely in some corrupted'
                            ' state.'
                            '[modification_id={0}]'.format(modification.id))
            raise


@workflow
def a4c_heal(
        ctx,
        node_instance_id,
        diagnose_value='Not provided',
        **kwargs):
    """Reinstalls the whole subgraph of the system topology

    The subgraph consists of all the nodes that are hosted in the
    failing node's compute and the compute itself.
    Additionally it unlinks and establishes appropriate relationships

    :param ctx: cloudify context
    :param node_id: failing node's id
    :param diagnose_value: diagnosed reason of failure
    """

    ctx.logger.info("Starting 'heal' workflow on {0}, Diagnosis: {1}"
                    .format(node_instance_id, diagnose_value))
    failing_node = ctx.get_node_instance(node_instance_id)
    host_instance_id = failing_node._node_instance.host_id
    failing_node_host = ctx.get_node_instance(host_instance_id)
    node_id = failing_node_host.node_id
    subgraph_node_instances = failing_node_host.get_contained_subgraph()
    added_and_related = _get_all_nodes(ctx)
    try:
      graph = ctx.graph_mode()
      ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                               message=build_pre_event(WfStartEvent('heal', 'uninstall')))
      custom_context = CustomContext(ctx, subgraph_node_instances, added_and_related)
      uninstall_host(ctx, graph, custom_context, node_id)
      graph.execute()
    except:
      ctx.logger.error('Uninstall while healing failed.')
    graph = ctx.internal.task_graph
    for task in graph.tasks_iter():
      graph.remove_task(task)
    ctx.internal.send_workflow_event(event_type='a4c_workflow_started',
                                             message=build_pre_event(WfStartEvent('heal', 'install')))
    custom_context = CustomContext(ctx, subgraph_node_instances, added_and_related)
    install_host(ctx, graph, custom_context, node_id)
    graph.execute()


#following code can be pasted in src/test/python/workflows/context.py for simulation
#def _build_nodes(ctx):
    #types = []
    #types.append('alien.nodes.openstack.ScalableCompute')
    #types.append('alien.nodes.openstack.Compute')
    #types.append('tosca.nodes.Compute')
    #types.append('tosca.nodes.Root')
    #node_NonScaledCompute = _build_node(ctx, 'NonScaledCompute', types, 1)
    #types = []
    #types.append('alien.nodes.openstack.ScalableCompute')
    #types.append('alien.nodes.openstack.Compute')
    #types.append('tosca.nodes.Compute')
    #types.append('tosca.nodes.Root')
    #node_AnotherScaleCompute = _build_node(ctx, 'AnotherScaleCompute', types, 1)
    #types = []
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node__a4c_BlockStorage2 = _build_node(ctx, '_a4c_BlockStorage2', types, 1)
    #types = []
    #types.append('fastconnect.nodes.SoftwareTest4HSS')
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node_FileSystem = _build_node(ctx, 'FileSystem', types, 1)
    #types = []
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node__a4c_BlockStorage = _build_node(ctx, '_a4c_BlockStorage', types, 1)
    #types = []
    #types.append('alien.nodes.openstack.ScalableCompute')
    #types.append('alien.nodes.openstack.Compute')
    #types.append('tosca.nodes.Compute')
    #types.append('tosca.nodes.Root')
    #node_Compute = _build_node(ctx, 'Compute', types, 1)
    #_add_relationship(node__a4c_BlockStorage2, node_Compute)
    #_add_relationship(node_FileSystem, node__a4c_BlockStorage2)
    #_add_relationship(node_FileSystem, node_Compute)
    #_add_relationship(node_FileSystem, node__a4c_BlockStorage)
    #_add_relationship(node__a4c_BlockStorage, node_Compute)
