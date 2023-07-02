interface IShape {
  getArea(): number;
}

class Rectangle implements IShape {
  constructor(public width: number = 0, public height: number = 0) {}

  setWidth(width: number) {
    this.width = width;
  }

  setHeight(height: number) {
    this.height = height;
  }

  getArea(): number {
    return this.width * this.height;
  }
}

class Square implements IShape {
  constructor(public length: number = 0) {}

  setLength(length: number) {
    this.length = length;
  }

  getArea(): number {
    return this.length * this.length;
  }
}

function f(shape: IShape) {
  console.log(shape.getArea());
}

function run() {
  const s1 = new Rectangle();
  s1.setWidth(3);
  s1.setHeight(4);
  f(s1);

  const s2 = new Square();
  s2.setLength(4);
  f(s2);
}

run();
