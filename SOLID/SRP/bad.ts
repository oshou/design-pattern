class Employee {
  public name: string
  public department: string

  constructor(name: string, department: string) {
    this.name = name
    this.department = department
  }

  // 経理部門がアクター
  calculatePay() {
    this.getRegularHours()
    console.log(`${this.name}の給与を計算しました`)
  }

  // 人事部門がアクター
  reportHours() {
    this.getRegularHours()
    console.log(`${this.name}の労働時間をレポートしました`)
  }

  // データベース管理者がアクター
  save() {
    console.log(`${this.name}を保存しました`)
  }

  private getRegularHours() {
    // 仕様変更前
    // console.log(`人事・経理部門の共通ロジック`)

    // 仕様変更後
    console.log(`経理部門依頼で仕様変更済`)
  }
}

function run() {
  const emp = new Employee('山田', '開発')

  console.log('経理部門')
  emp.calculatePay()

  console.log('人事部門')
  emp.reportHours()
}

run()
