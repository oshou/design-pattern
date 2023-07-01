class EmployeeData {
  public name: string
  public department: string

  constructor(name: string, department: string) {
    this.name = name
    this.department = department
  }
}

class PayCalculator {
  calculatePay(employeeData: EmployeeData): void {
    this.getRegularHours()
    console.log(`${employeeData.name}の給与を計算しました`)
  }

  private getRegularHours(): void {
    console.log('給与計算用の労働時間計算ロジック')
  }
}

class HourReporter {
  reportHours(employeeData: EmployeeData): void {
    this.getRegularHours()
    console.log(`${employeeData.name}の労働時間を計算しました`)
  }
  private getRegularHours(): void {
    console.log('労働時間レポート用の労働時間計算ロジック')
  }
}

class EmployeeRepository {
  save(): void {}
}

function run() {
  const employeeData = new EmployeeData('鈴木', '開発')
  const payCalculator = new PayCalculator()
  const hourReporter = new HourReporter()

  console.log('経理部門')
  payCalculator.calculatePay(employeeData)

  console.log('人事部門')
  hourReporter.reportHours(employeeData)
}

run()
