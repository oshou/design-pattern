export class Rectangle {
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

export class Square extends Rectangle {
  setWidth(width: number) {
    super.setWidth(width);
    super.setHeight(width);
  }

  setHeight(height: number) {
    super.setWidth(height);
    super.setHeight(height);
  }
}

export function f(r: Rectangle, width: number, height: number) {
  r.setWidth(width);
  r.setHeight(height);
  return r.getArea();
}

function run() {
  const r1: Rectangle = new Rectangle();
  const r2: Rectangle = new Square();

  console.log(f(r1, 3, 4));
  console.log(f(r2, 3, 4));
}

run();
