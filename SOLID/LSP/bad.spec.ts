import { Rectangle, Square, f } from "./bad";

describe("Rectangle Test", () => {
  test("Reactangle getArea", () => {
    const r1 = new Rectangle();
    expect(f(r1, 3, 4)).toBe(12);
  });
  test("Square getArea", () => {
    const r1 = new Square();
    expect(f(r1, 3, 4)).toBe(12);
  });
});
