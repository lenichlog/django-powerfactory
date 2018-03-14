import sys

sys.path.append("C:\\Program Files\\DIgSILENT\\PowerFactory 2016 SP4\\Python\\3.4")


class PowerFactory:
    @staticmethod
    def pf_app():
        import powerfactory

        app = powerfactory.GetApplication()
        if app is None:
            raise Exception("getting PoerFactory application failure")

        app.ActivateProject("\gurkov_lo.IntUser\Богучанская ГЭС.IntPrj")
        return app, powerfactory
