from classiq import construct_combinatorial_optimization_model, set_execution_preferences, write_qmod
from classiq.applications.combinatorial_optimization import OptimizerConfig, QAOAConfig
from mypyomo import mvc
from classiq.execution import ClassiqBackendPreferences, ExecutionPreferences

qaoa_config = QAOAConfig(num_layers=1)
optimizer_config = OptimizerConfig(max_iteration=60, alpha_cvar=0.9)

qmod = construct_combinatorial_optimization_model(
    pyo_model=mvc,
    qaoa_config=qaoa_config,
    optimizer_config=optimizer_config,
)

backend_preferences = ExecutionPreferences(
    backend_preferences=ClassiqBackendPreferences(backend_name='aer_simulator')
)

write_qmod(qmod, 'patch_min_vertex_cover')