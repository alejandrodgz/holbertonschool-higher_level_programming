#!/usr/bin/node

import { Rectangle } from './5-square';
export class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        console.log(`${c}`.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
}
