class invalidAccountException(Exception):
    def __init__(selfs,str):
        super().__init__(str)

__all__=['invalidAccountException']