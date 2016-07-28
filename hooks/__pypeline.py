import tank
import sys
import os


# ----------------------------------------------------------------------------------------------------------------------

def init_pypeline():
    engine = tank.platform.current_engine()
    if 'Dev' == engine.sgtk.pipeline_configuration.get_name():
        root = r'E:\workspace\python\Pypeline2'
    else:
        root = r'Y:\MatrixStudio\Pypeline2'

    mx_path = r'%s\lib' % root
    if mx_path not in sys.path:
        sys.path.append(mx_path)

        from mx.app import MxAppSetting, MxAppLauncherFactory

        MxAppLauncherFactory.init()

        app_setting = MxAppSetting.get()
        app_setting.load(r'%s\bin' % root)
        app_setting.load_workbench()

init_pypeline()


# ----------------------------------------------------------------------------------------------------------------------

def get_and_set_environment(app_name):
    from mx.app import MxAppSetting, MxAppLauncherFactory

    app_setting = MxAppSetting.get()
    workbench = app_setting.workbench()
    app = workbench.app(app_name)
    launcher = MxAppLauncherFactory.create_launcher(app, app_setting)

    env = launcher.get_environment()
    for n, v in env.iteritems():
        os.environ[n] = v
