import sys

LIB_PATH = "C:\\Program Files\\DIgSILENT\\PowerFactory 2016 SP4\\Python\\3.4"
PROJECT_PATH = "\gurkov_lo.IntUser\Богучанская ГЭС.IntPrj"

sys.path.append(LIB_PATH)


class PowerFactory:
    @staticmethod
    def pf_app():
        import powerfactory

        app = powerfactory.GetApplication()
        if app is None:
            raise Exception("getting PoerFactory application failure")

        app.ActivateProject(PROJECT_PATH)
        return app, powerfactory
