export interface IVehicle {
  name: string;
  color: string;

  start(): void;
  stop(): void;
  fly(): void;
}

export class Car implements IVehicle {
  constructor(public name: string, public color: string) {}

  start(): void {
    console.log("start");
  }

  stop(): void {
    console.log("stop");
  }

  fly(): void {
    throw new Error("car can't fly!");
  }
}

export class Airplane implements IVehicle {
  constructor(public name: string, public color: string) {}

  start(): void {
    console.log("start");
  }

  stop(): void {
    console.log("stop");
  }

  fly(): void {
    throw new Error("car can't fly!");
  }
}

function run() {
  const v1: IVehicle = new Airplane("AirBus", "white");
  const v2: IVehicle = new Car("Prius", "black");

  v1.fly();
  v2.fly();
}

run();
