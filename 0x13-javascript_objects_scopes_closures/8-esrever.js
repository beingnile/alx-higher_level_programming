#!/usr/bin/node

// Return reversed version of list
exports.esrever = function (list) {
  const rev = [];
  list.forEach(item => rev.unshift(item));
  return rev;
};
