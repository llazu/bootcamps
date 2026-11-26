"""
class Surgeon {
  constructor(name, department) {
    this._name = name;
    this._department = department;
    this._remainingVacationDays = 20;
  }
  get name() {
    return this._name;
  }
  get department() {
    return this._department;
  }
  get remainingVacationDays() {
    return this._remainingVacationDays;
  }
  takeVacationDays(daysOff) {
    this._remainingVacationDays -= daysOff;
  }
}
"""

# avoided @property on purpose
class Surgeon:
    def __init__(self, name, department):
        self._name = name
        self._department = department
        self._remaining_vacations_days = 20

    def get_name(self):
        return self._name
    
    def get_department(self):
        return self._department

    def get_remaining_vacation_daya(self):
        return self._remaining_vacation_days

    def take_vacation_days(self, days_off):
        self._remaining_vacations_days -= days_off

surgeonRomero = Surgeon("Francisco Romer", "Cardiovascular")
surgeonJackson = Surgeon("Ruth Jackson", "Orthopedics")
