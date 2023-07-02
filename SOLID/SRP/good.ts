export class Employee {
  public name: string
  public department: string

  constructor(name: string, department: string) {
    this.name = name
    this.department = department
  }
}

export class PayCalculator {
  calculatePay(employee: Employee): void {
    this.getRegularHours()
    console.log(`${employee.name}の給与を計算しました`)
  }

  private getRegularHours(): void {
    console.log('給与計算用の労働時間計算ロジック')
  }
}

export class HourReporter {
  reportHours(employee: Employee): void {
    this.getRegularHours()
    console.log(`${employee.name}の労働時間を計算しました`)
  }
  private getRegularHours(): void {
    console.log('労働時間レポート用の労働時間計算ロジック')
  }
}

export class EmployeeRepository {
  save(): void {}
}

function run() {
  const employeeData = new Employee('鈴木', '開発')
  const payCalculator = new PayCalculator()
  const hourReporter = new HourReporter()

  console.log('経理部門')
  payCalculator.calculatePay(employeeData)

  console.log('人事部門')
  hourReporter.reportHours(employeeData)
}

run()
