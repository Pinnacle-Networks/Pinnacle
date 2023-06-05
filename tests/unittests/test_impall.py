import impall


class ImpAllTest(impall.ImpAllTest):
    # Do not reload modules for each file tested
    CLEAR_SYS_MODULES = False

    EXCLUDE = (
        'pinnacledb/apis/openai/wrapper',
        'pinnacledb/cluster/ray/predict',
        'pinnacledb/cluster/ray/predict_one',
    )
