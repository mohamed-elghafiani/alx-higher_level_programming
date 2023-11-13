#!/usr/bin/node

function callMeMoby (n, funct) {
  for (let i = 0; i < n; i++) {
    funct();
  }
}

module.exports = { callMeMoby };
