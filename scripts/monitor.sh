#!/usr/bin/env bash

main() {
  CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
  monitor=$(python ${CURRENT_DIR}/monitor.py)
  printf $(python ${CURRENT_DIR}/monitor.py) "bla"
}

main
