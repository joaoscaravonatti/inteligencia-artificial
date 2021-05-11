import { Search } from './search'
import { Node } from './node'
import { ACTIONS, START } from './constants'

export class AStarSearch extends Search {
  private start: Node
  private goal: Node
  private solution: Node | undefined
  private stack: Node[]

  constructor (start: Node, goal: Node) {
    super()
    this.start = new Node(start.state)
    this.goal = new Node(goal.state)
    this.stack = [start]
  }

  private getBits (state: number[]): string {
    const [miss, cann, boat] = state
    let bits = ''

    for (const value of [miss, cann]) {
      if (value === 3) {
        bits += '111'
      } else if (value === 2) {
        bits += '011'
      } else if (value === 1) {
        bits += '001'
      } else if (value === 0) {
        bits += '000'
      }
    }

    return bits + boat.toString()
  }

  private hammingDistance (a: number[], b: number[]): number {
    const aBits = this.getBits(a)
    const bBits = this.getBits(b)

    let distance = 0

    for (let i = 0; i < aBits.length; i++) {
      if (aBits[i] !== bBits[i]) {
        distance++
      }
    }

    return distance
  }

  search (): Node | undefined {
    console.log('A* Search')

    while (this.stack.length) {
      const node = this.stack.pop()

      if (!node) continue

      if (node.equal(this.goal)) {
        this.solution = node
        break
      }

      this.explored.push(node)

      for (const action of ACTIONS) {
        const newState = this.getNextState(node.state, action)
        const cost = this.hammingDistance(node.state, newState)
        const newChild = new Node(newState, cost)
        if (newChild.valid() && !this.alreadyExplored(newChild)) {
          node.addChild(newChild, action)
        }
      }

      if (node.children.length) {
        let minValue = node.children[0]

        for (const child of node.children) {

          let minAStarValue = this.hammingDistance(this.goal.state, minValue.state) + minValue.traveledDistance()
          let childAStarValue = this.hammingDistance(this.goal.state, child.state) + child.traveledDistance()

          if (childAStarValue <= minAStarValue) {
            minValue = child
          }
        }
        this.stack.push(minValue)
      }
    }

    return this.solution
  }
}
