export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  set size(value) {
    if (typeof value !== 'number') {
      throw new TypeError('size must be a number');
    }
    this._size = value;
  }

  get size() {
    return this._size;
  }

  set location(value) {
    if (typeof value !== 'string') {
      throw new TypeError('size must be a string');
    }
    this._code = value;
  }

  get location() {
    return this._location;
  }

  [Symbol.toPrimitive](cast) {
    if (cast === 'number') return this.size;
    if (cast === 'string') return this.location;
    return null;
  }
}
