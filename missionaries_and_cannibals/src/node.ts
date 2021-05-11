import { NUM_BOAT, NUM_CANN, NUM_MISS } from './constants'

export class Node {
  state: number[]
  action: number[]
  depth: number
  children: Node[]
  parent: Node | undefined
  cost: number

  constructor (state: number[], cost = 0) {
    this.state = state
    this.action = [0, 0, 0]
    this.depth = 0
    this.children = []
    this.cost = cost
  }

  toString (): string {
    return `
      state: ${this.state}
      parent: ${this.parent?.state}
      action: ${this.action}
      depth: ${this.depth}
      traveled: ${this.traveledDistance()}
      children: ${this.children.map(child => child.state)}
    `
  }

  addChild (child: Node, action: number[]): void {
      this.children.push(child)
      child.parent = this
      child.depth = this.depth + 1
      child.action = [...action]
  }

  equal (value: Node): boolean {
    return value.state.every((item, index) => item === this.state[index])
  }

  valid (): boolean {
    const { state } = this

    if (!state.every(value => value >= 0 && value <= 3)) {
      return false
    }

    const right = [...state]
    const left = [3 - right[NUM_MISS], 3 - right[NUM_CANN], state[NUM_BOAT]]

    for (const side of [left, right]) {
      if (side[NUM_MISS] > 0 && side[NUM_CANN] > side[NUM_MISS]) {
        return false
      }
    }

    return true
  }

  getRight (): number[] {
    return [this.state[NUM_MISS], this.state[NUM_CANN]]
  }

  getLeft (): number[] {
    return [3 - this.state[NUM_MISS], 3 - this.state[NUM_CANN]]
  }

  traveledDistance (): number {
    let traveled = this.cost
    let node: Node = this
    while (node) {
      if (!node.parent) break
      traveled += node.parent.cost
      node = node.parent
    }
    return traveled
  }
}