import { Node } from './node'
import { GOAL, START } from './constants'
import { AStarSearch } from './a-star-search'

const printPath = (node: Node | undefined): void => {
  if (node) {
    printPath(node.parent)
    console.log(`action -> ${[node.action[0], node.action[1]]}, state: ${node.getLeft()} - ${node.getRight()},  depth: ${node.depth}`)
  }
}

const start = new Node(START)
const goal = new Node(GOAL)
const ass = new AStarSearch(start, goal)

printPath(ass.search())
