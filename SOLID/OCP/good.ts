interface IEmployee {
  name: string
  getBonus(base: number): number
}

class JuniorEmployee implements IEmployee {
  constructor(public name: string) {}

  getBonus(base: number): number {
    return Math.floor(base * 1.1)
  }
}

class MiddleEmployee implements IEmployee {
  constructor(public name: string) {}

  getBonus(base: number): number {
    return Math.floor(base * 1.2)
  }
}

class SeniorEmployee implements IEmployee {
  constructor(public name: string) {}

  getBonus(base: number): number {
    return Math.floor(base * 1.3)
  }
}

class ExpertEmployee implements IEmployee {
  constructor(public name: string) {}

  getBonus(base: number): number {
    return Math.floor(base * 1.5)
  }
}

function run() {
  const emp1 = new JuniorEmployee('Yamada')
  const emp2 = new MiddleEmployee('Suzuki')
  const emp3 = new SeniorEmployee('Tanaka')
  const emp4 = new ExpertEmployee('Koyama')

  console.log(`emp1: ${emp1.getBonus(100)}`)
  console.log(`emp2: ${emp2.getBonus(100)}`)
  console.log(`emp3: ${emp3.getBonus(100)}`)
  console.log(`emp4: ${emp4.getBonus(100)}`)
}

run()
