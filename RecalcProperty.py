class ChemComponent:
    Mr = 0     # молекулярная масса
    CapacityABCD = [0, 0, 0, 0]     # коэффициенты в уравнении зависимости теплоемкости от температуры
    Dencity = 0         # плотность вещества


class Flow:

    MolRate = 0  # мольный расход, моль/сек
    VolumeRate = 0  # объемный расход, м3/сек
    CountChemComponents = 0   # количество компонентов в потоке
    ChemComponents = [ChemComponent]*CountChemComponents    # набор компонентов

    MassRateComponents = [0]*CountChemComponents      # массовые расходы компонентов
    MolRateComponents = [0] * CountChemComponents  # мольные расходы компонентов
    VolRateComponents = [0] * CountChemComponents  # объемные расходы компонентов

    MassConcComponents = [0] * CountChemComponents  # массовые концентрации компонентов
    MolConcComponents = [0] * CountChemComponents  # мольные концентрации компонентов
    VolConcComponents = [0] * CountChemComponents  # объемные концентрации компонентов

    # расходы
    def GetMassRate(self):      # массовый расход, кг/сек

        sum = 0
        for i in range(self.CountChemComponents):
            sum += self.MassRateComponents[i]

        return sum

    def GetMolRate(self):  # мольный расход, моль/сек

        sum = 0
        for i in range(self.CountChemComponents):
            sum += self.MolRateComponents[i]

        return sum

    def GetVolRate(self):  # объемный расход, м3/сек

        sum = 0
        for i in range(self.CountChemComponents):
            sum += self.VolRateComponents[i]

        return sum



    # свойства
    def GetMolarMass(self):  # молекулярная масса, г/моль

        sum = 0
        for i in range(self.CountChemComponents):
            sum += self.ChemComponents[i].Mr*self.MolConcComponents[i]

        return sum

    # концентрации
    def GetMassConcFromMol(self):  # массовые концентрации, %мас.

        sum = 0
        for i in range(self.CountChemComponents):
            sum += self.ChemComponents[i].Mr*self.MolConcComponents[i]

        return sum
