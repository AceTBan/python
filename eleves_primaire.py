def section(age):
    categories = {"CP": 6, "CE1": 7, "CE2": 8, "CM1": 9, "CM2": 10}
    return categories.keys()[list(categories.values()).index(age)]


class eleve:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self._section=section(age)

    def annif(self,age):
        self.age+=1
        self._section=section(age)

    def _changerDeSection(self,section):
        self._section=section

    def _getSection(self):
        return self._section

    def _setSection(self):
        self._section=section

    def _removeSection(self):
        del self._section

    Section = property(_changerDeSection,_getSection,_setSection,_removeSection)