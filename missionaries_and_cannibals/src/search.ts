import { NUM_BOAT, NUM_MISS, NUM_CANN, WRONGSIDE } from './constants'
import { Node } from './node'

export class Search {
  protected explored: Node[] = []

  protected getNextState (currentState: number[], action: number[]): number[] {
    return currentState[NUM_BOAT] === WRONGSIDE ? [
      currentState[NUM_MISS] - action[NUM_MISS],
      currentState[NUM_CANN] - action[NUM_CANN],
      currentState[NUM_BOAT] - action[NUM_BOAT]
    ] : [
      currentState[NUM_MISS] + action[NUM_MISS],
      currentState[NUM_CANN] + action[NUM_CANN],
      currentState[NUM_BOAT] + action[NUM_BOAT]
    ]
  }

  protected alreadyExplored (node: Node): boolean {
    for (const item of this.explored) {
      if (node.equal(item)) {
        return true
      }
    }
    return false
  }
}