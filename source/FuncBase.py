import abc  # 提供抽象函式定義


class FuncBase:

    @property
    @abc.abstractproperty
    def Description():
        return NotImplemented

    @abc.abstractmethod
    def Run():
        return NotImplemented
