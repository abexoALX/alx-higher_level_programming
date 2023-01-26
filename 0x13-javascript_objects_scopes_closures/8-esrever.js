#!/usr/bin/node

exports.esrever = function (list) {
  const result = [];
  for (let i = list.length - 1; i >= 0; i--) {
    result.push(list[i]);
  }
  return (result);
};
