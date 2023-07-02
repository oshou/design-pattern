export interface Movable {
  start(): void;
  stop(): void;
}

export interface Flyable {
  fly(): void;
}

export class Car implements Movable {
  constructor(public name: string, public color: string) {}

  start() {
    console.log("start");
  }

  stop() {
    console.log("start");
  }
}

export class Airplane implements Movable, Flyable {
  constructor(public name: string, public color: string) {}

  start() {
    console.log("start");
  }

  stop() {
    console.log("start");
  }

  fly() {
    console.log("fly");
  }
}

function run() {
  const v1: Airplane = new Airplane("AirBus", "white");
  const v2: Car = new Car("Prius", "black");

  v1.fly();
  v2.start();
}

run();
