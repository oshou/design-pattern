export class Employee {
  constructor(public name: string, public grade: 'junior' | 'middle' | 'senior' | 'expert') {}
}

export class BonusCalculator {
  constructor(public base: number) {}

  getBonus(employee: Employee): number {
    switch (employee.grade) {
      case 'junior':
        return Math.floor(this.base * 1.1)
      case 'middle':
        return Math.floor(this.base * 1.2)
      case 'senior':
        return Math.floor(this.base * 1.3)
      case 'expert':
        return Math.floor(this.base * 1.5)
      default:
        return Math.floor(this.base * 1.0)
    }
  }
}

function run() {
  const emp1 = new Employee('Yamada', 'junior')
  const emp2 = new Employee('Suzuki', 'middle')
  const emp3 = new Employee('Tanaka', 'senior')
  const emp4 = new Employee('Koyama', 'expert')

  const bonusCalculator = new BonusCalculator(100)
  console.log(`emp1: ${bonusCalculator.getBonus(emp1)}`)
  console.log(`emp2: ${bonusCalculator.getBonus(emp2)}`)
  console.log(`emp3: ${bonusCalculator.getBonus(emp3)}`)
  console.log(`emp4: ${bonusCalculator.getBonus(emp4)}`)
}

run()
