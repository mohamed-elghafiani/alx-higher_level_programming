#!/usr/bin/node

exports.esrever = function (list) {
  const list_ = [];
  for (let i = list.length - 1; i >= 0; i--) {
    list_.push(list[i]);
  }
  return list_;
};
