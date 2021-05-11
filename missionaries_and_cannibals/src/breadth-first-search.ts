import { Node } from './node'
import { ACTIONS, GOAL, NUM_BOAT, NUM_CANN, NUM_MISS, WRONGSIDE } from './constants'
import { Search } from './search'

export class BreadthFirstSearch extends Search {
  private goal: Node
  private queue: Node[] = []
  private solution: Node | undefined

  constructor (start: Node, goal: Node) {
    super()
    this.goal = goal
    this.queue = [start]
  }

  search (): Node | undefined {
    console.log('Breadth First Search')

    while (this.queue.length > 0) {
      let node = this.queue.shift()

      if (!node) continue

      if (!node.valid()) continue

      this.explored.push(node)

      if (node.equal(this.goal)) {
        this.solution = node
        break
      }

      for (const action of ACTIONS) {
        const newState = this.getNextState(node.state, action)
        const newChild = new Node(newState)
        if (newChild.valid() && !this.alreadyExplored(newChild)) {
          node.addChild(newChild, action)
          this.queue.push(newChild)
        }
      }
    }

    return this.solution
  }
}
