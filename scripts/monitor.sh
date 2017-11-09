#!/usr/bin/env bash

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

source $CURRENT_DIR/shared.sh

main() {
  monitor=$(python ${CURRENT_DIR}/monitor.py)
  printf "${monitor}"
}

main
